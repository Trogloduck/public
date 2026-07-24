https://tryhackme.com/room/webserverattacks

### Table of contents
- [[#Identify Web Servers]]
- [[#Python]]
- [[#Apache2]]
- [[#Node.js]]
- 

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
`NODE_ENV` set in `production` --> Express suppresses stack traces
In development, passes them through
Devs often write their own error handlers, potentially exposing stack traces regardless of `NODE_ENV`'s behavior



___
### 
[[#Table of contents|Back to the top]]



___
### 
[[#Table of contents|Back to the top]]



___
### 
[[#Table of contents|Back to the top]]



___
