https://tryhackme.com/room/protocolsandservers

### Table of contents
- [[#Telnet]]
- [[#HTTP]]
- [[#FTP]]
- 

___
### Telnet
[[#Table of contents|Back to the top]]

**Port 23**

Connect to virtual terminal of another computer, **not encrypted** --> Secure alternative is **SSH**

1. `telnet [ip address]`
2. Provide login name (username)
3. Password
4. Authentication successful --> welcome message
5. Command prompt, `[username]@[client]:~$` ("`$`" indicates that this is not a root terminal)

___
### HTTP
[[#Table of contents|Back to the top]]

**Port 80**

*Hypertext Transfer Protocol* used to transfer **web pages**, not encrypted --> HTTPS

HTTP web servers
- [Apache](https://www.apache.org/)
- [Internet Information Services (IIS)](https://www.iis.net/)
- [nginx](https://nginx.org/)

Connect to webserver using telnet
1. `telnet [ip address] 80`
2. `GET /[file name] HTTP/1.1` to retrieve \[file name]
   or `GET / HTTP/1.1` to retrieve default page
3. `host: telnet`, Enter **twice**
___
### FTP
[[#Table of contents|Back to the top]]

**Port 21**

*File Transfer Protocol*, not encrypted

