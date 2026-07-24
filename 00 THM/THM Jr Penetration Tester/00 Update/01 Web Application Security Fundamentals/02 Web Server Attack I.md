https://tryhackme.com/room/webserverattacks

### Table of contents
- [[#Identify Web Servers]]
- [[#Python]]
- [[#Apache2]]
- [[#Node.js]]
- [[#Nginx]]

___
### Identify Web Servers
[[#Table of contents|Back to the top]]

Web server software --> which misconfigurations --> vulnerabilities --> effective tools-paths

##### Server Response Header

`curl -sI http://10.128.180.113:80`

NB: **Node.js** doesn't set a default `Server` header --> reliable identifier **`X-Powered-By: Express`**

##### Browser DevTools
\> Inspector > Network > Headers

##### Default Error Pages

`curl -s http://10.128.180.113:PORT/nonexistent`
Trigger error --> most servers return 404 but each server has distinct look
- **Apache** (80): Apache in page **body**
- **Python** (8000): **plain** text
- **Nginx** (8080): version in HTML **footer**

| Port | Server                 | Default Server Header          |
| ---- | ---------------------- | ------------------------------ |
| 80   | **Apache2**            | `Apache/2.4.x (Ubuntu)`        |
| 8000 | **Python** HTTP Server | `SimpleHTTP/0.6 Python/3.xx.x` |
| 8080 | **Nginx**              | `nginx/1.xx.x`                 |
| 3000 | **Node.js Express**    | None (set by application)      |

___
### Python
[[#Table of contents|Back to the top]]

`python3 -m http.server 8000`: start Python web server

No access control, no authentication, no logging beyond what OS captures
--> problem if exposed

##### Serving
Python HTTP server **serves everything** in working directory without restriction
=/= Apache & Nginx disable listing by default, admin can restrict individual paths

##### Listing
No `index.html` in directory --> Python HTTP server generates HTML page listing every file it can see (also dot files)
If `index.html` is served --> try subdirectories or specific paths

##### Downloading & Inspecting Archives
`.zip`, `.tar.gz`, ...
`curl -s http://10.128.180.113:8000/backup.zip -o backup.zip`, `unzip`

___
### Apache2
[[#Table of contents|Back to the top]]

Most widely deployed
Most common findings: directory listing on specific paths, `server-status` module, backup files sitting in document root

##### Version
`curl -SI http://10.128.180.113:80 | grep -i server`

##### Listing
No `index.html` --> display file listing
Browse to `http://10.128.180.113/files/`

##### `mod_status` module
Correct configuration: only accessible from localhost
`http://10.128.180.113:80/server-status`

##### gobuster
Find unlisted files
`gobuster dir -u http://TARGET_IP:80 -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt -x bak,txt,html -t 20`
`-x`: targeted extension sweep

`.bak` backup files are often valuable
`.htpasswd` store usernames and hashed passwords for HTTP Basic Authentication

___
### Node.js
[[#Table of contents|Back to the top]]

Not serving static files from configurent document root like Apache and Python
Running application code, code decides what to return based on requests

Development-mode features left enabled: debug endpoints, verbose error responses, exposed environment variables, ...

##### Framework Fingerprinting
`curl -sI http://10.128.180.113:3000`
**`X-Powered-By: Express`**

##### Application Version
`curl -s http://10.128.180.113:3000`
--> known vulnerabilities, change logs

##### Verbose Errors
`curl -s http://10.129.156.206:3000/api/users | python3 -m json.tool`
`NODE_ENV` set in `production` --> Express suppresses stack traces
In development, passes them through
Devs often write **custom error handlers**, potentially exposing stack traces regardless of `NODE_ENV`'s behavior
Verbose error message can contain error message, stack trace, context about what app was trying to do, ...

##### Enumerating Routes via Debug Endpoints
`curl -s http://10.129.156.206:3000/api/routes`
Endpoint created by devs to list registered routes, forgotten to delete
--> indicates every path app handles

##### Environment Variables
`curl -s http://10.129.156.206:3000/api/debug/env`

##### Static File Serving
`express.static()` middleware often serves front-end assets (JS files, stylesheets, config, ...)
JS files can contain API endpoint URLs, internal hostnames, debug flags embedded as constants
`curl -s http://10.129.156.206:3000/static/config.js`

___
### Nginx
[[#Table of contents|Back to the top]]

Same template, different vocabulary

Commonly uses as reverse proxy, load balancer, high-performance static file server
Often sits in front of application server, handles public-facing traffic

##### Version
`curl -sI http://10.129.156.206:8080 | grep -i server`
--> set `server_tokens` to `off`

##### Listing
Disabled by default, enabled with `autoindex`
*Example*
```nginx
location /files/ {
    autoindex on;
    root /var/www/nginx/;
}
```
Shouldn't be used on path containing sensitive files / on production server without access controls

`curl -s http://10.129.156.206:8080/files/`

##### `nginx_status` endpoint
`stub_status` module exposes real-time connection metrics at configurable URL
```Nginx
location /nginx_status {
	stub_status;
	allow all; # Should be: allow 127.0.0.1; deny all;
}
```
`curl -s http://10.129.156.206:8080/nginx_status`
Returns 3 numbers: total accepted connections, total handled connections, total requests since server started --> info about server load, usage patterns

___
### Security Headers
[[#Table of contents|Back to the top]]

Should be used to protect against wide range of attacks, not sent by default

| Header                      | What It Protects Against                                                            | Example Value                    |
| --------------------------- | ----------------------------------------------------------------------------------- | -------------------------------- |
| `X-Frame-Options`           | Clickjacking (prevents the page from being embedded in an iframe on another domain) | `DENY` or `SAMEORIGIN`           |
| `X-Content-Type-Options`    | MIME sniffing (prevents the browser from guessing content types)                    | `nosniff`                        |
| `Content-Security-Policy`   | Restricts where scripts, stylesheets, and other resources can load from             | `default-src 'self'`             |
| `Referrer-Policy`           | Controls what is sent in the `Referer` header when navigating to another page       | `no-referrer` or `strict-origin` |
| `Strict-Transport-Security` | Forces HTTPS for subsequent requests (only meaningful on HTTPS servers)             | `max-age=31536000`               |

```Shell
for port in 80 8000 3000 8080; do echo "=== Port $port ==="; curl -sI http://10.129.156.206:$port/ | grep -iE "x-frame-options|x-content-type|content-security-policy|strict-transport|referrer-policy" || echo "(no security headers found)"; done
```

___
### Automation - `nikto`
[[#Table of contents|Back to the top]]

`nikto` checks for known misconfigurations, outdated software, exposed admin interfaces, missing security headers

**Generates lots of traffic, not stealthy at all**

`nikto -h http://10.129.156.206:80 -nointeractive`
`-nointeractive` makes scan run without waiting for input

___
### Cross-Servers Misconfigurations
[[#Table of contents|Back to the top]]

| Misconfiguration                 | Apache                             | Python HTTP                       | Node.js                         | Nginx                                   |
| -------------------------------- | ---------------------------------- | --------------------------------- | ------------------------------- | --------------------------------------- |
| Version disclosure in headers    | Yes                                | Yes                               | Partial                         | Yes                                     |
| Directory listing                | `/files/`                          | Root path                         | N/A                             | `/files/`                               |
| Exposed status or debug endpoint | `/server-status`                   | N/A                               | `/api/debug/env`, `/api/routes` | `/nginx_status`                         |
| Sensitive files accessible       | `backup.bak`, `internal-notes.txt` | `.env`, `notes.txt`, `backup.zip` | `config.js`                     | `server-config.txt`, `deploy-notes.txt` |
| Missing security headers         | All                                | All                               | All                             | All                                     |
