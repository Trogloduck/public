https://tryhackme.com/room/protocolsandservers

### Table of contents
- [[#Telnet]]
- [[#HTTP]]
- [[#FTP]]
- [[#SMTP]]
- [[#POP3]]
- [[#IMAP]]

___
### Telnet
[[#Table of contents|Back to the top]]

**Port 23**

Connect to virtual **terminal** of another computer, **not encrypted** --> Secure alternative is **SSH**

1. `telnet [ip address]`
2. Provide login name (username)
3. Password
4. Authentication successful --> welcome message
5. Command prompt, `[username]@[client]:~$` ("`$`" indicates that this is not a root terminal)

___
### HTTP
[[#Table of contents|Back to the top]]

**Port 80**

*Hypertext Transfer Protocol* used to transfer **web pages**, **not encrypted** --> HTTPS

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

***File** Transfer Protocol*, **not encrypted**

1. `telnet [ip address] 21`
2. `USER [username]`
3. `PASS [password]`
4. Authenticated
	\> `STAT`: provides added information
	\> `SYST`: system type of target
	\> `TYPE A`: transfer mode to ASCII
	\> `TYPE I`: transfer mode to binary

2 modes
- Active: data sent over **separate channel** originating from FTP server’s **port 20**
- Passive: data sent over **separate channel** originating from FTP client’s port **above port number 1023**

Files cannot be transferred using telnet as a client because FTP creates a separate connection for file transfer

1. `ftp [ip address]`
2. `[username]`
3. `[password]`
4. `ls`
5. `ascii` (in order to transfer text file)
6. `get [file name]`: transfer the file

FTP servers
- [vsftpd](https://security.appspot.com/vsftpd.html)
- [ProFTPD](http://www.proftpd.org/)
- [uFTP](https://www.uftpserver.com/)

FTP clients
- Default client on Linux
- [FileZilla](https://filezilla-project.org/) (has a GUI)

___
### SMTP
[[#Table of contents|Back to the top]]

**Port 25**

*Simple **Mail** Transfer Protocol*, **not encrypted**

Email delivery over the Internet requires the following components:
1. Mail Submission Agent (MSA)
2. Mail Transfer Agent (MTA)
3. Mail Delivery Agent (MDA)
4. Mail User Agent (MUA)

![[Pasted image 20251024100547.png]]

1. **MUA** connects **to MSA** to send message
2. **MSA** receives message, checks for any errors before transferring it **to MTA** server, commonly hosted on same server
3. **MTA** sends email message **to MTA** of recipient. The MTA can also function as an MSA
4. Typical setup would have **MTA** server also functioning as MDA
5. **MUA** collects email **from MTA**

Protocols to communicate with MTA and MDA: SMTP, POP3 and IMAP

1. `telnet [ip address] 25`
2. `helo hostname`
3. `mail from: [email address]`
4. `mail to: [email address]`
5. `data: [email]`

___
### POP3
[[#Table of contents|Back to the top]]

**Port 110**

*Post Office Protocol* download email from MDA, **not encrypted**

1. Connect to POP3 server
2. Download new email messages
3. (Optional) delete new email messages

Connect to POP3 over telnet
1. `telnet [ip address] 110`
2. `USER [username]`
3. `PASS [password]`
4. Authenticated
	\> `STAT`: output: "`+OK nn mm`" where "`nn`" is number of emails, "`mm`" is size of inbox (octets)
	\> `LIST`: list of new emails
	\> `RETR 1`: retrieve 1st message in list

___
### IMAP
[[#Table of contents|Back to the top]]

**Port 143**

*Internet Message Access Protocol*, synchronizes email across multiple devices (and clients), **not encrypted**

Each command must be preceded by random string to track reply: `c1 ...`, `c2 ...`, etc.
1. `telnet [ip address] 143`
2. `c1 LOGIN username password`
3. `c2 LIST "" "*"`: list all email folders
4. `c3 EXAMINE INBOX`: check for new emails