https://tryhackme.com/room/webserverattacks2

### Table of contents
- [[#IIS]]
- [[#Fingerprinting & Enumeration]]
- [[#~Tilde Enumeration]]
- 

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
### 
[[#Table of contents|Back to the top]]



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
