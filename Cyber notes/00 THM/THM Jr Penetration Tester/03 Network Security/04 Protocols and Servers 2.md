https://tryhackme.com/room/protocolsandservers2

[[Protocols and Servers|Protocols and Servers 1]]


### Table of contents
- [[#Sniffing Attack]]
- [[#MITM]]
- [[#TLS]]
- [[#SSH]]
- [[#Password Attack]]


___
### Sniffing Attack
[[#Table of contents|Back to the top]]

Packet capture tool to collect info about target

- **tcpdump**: open-source CLI tool
- **Wireshark**: open source GUI tool
- **Tshark**: CLI Wireshark

___
### MITM
[[#Table of contents|Back to the top]]

Target T thinks they're communicating with Server S but Attacker A is intercepting T's communication, modifying them and sending them to S

HTTP is vulnerable to such attack --> Tools: **[Ettercap](https://www.ettercap-project.org/)**, **[Bettercap](https://www.bettercap.org/)**

Other cleartext protocols: FTP, SMTP, POP3

___
### TLS
[[#Table of contents|Back to the top]]

Used to integrate encryption into and secure HTTP, FTP, SMTP, POP3, IMAP, ...

| Protocol | Port | Secured Protocol | Port with TLS |
| -------- | ---- | ---------------- | ------------- |
| HTTP     | 80   | HTTPS            | 443           |
| FTP      | 21   | FTPS             | 990           |
| SMTP     | 25   | SMTPS            | 465           |
| POP3     | 110  | POP3S            | 995           |
| IMAP     | 143  | IMAPS            | 993           |

HTTP:
1. Establish TCP connection with web server
2. Send HTTP requests to web server (GET, POST, ...)

HTTPS:
1. Establish TCP connection
2. Establish SSL/TLS connection
3. Send HTTP requests

SSL/TLS handshake
![[Pasted image 20251225151413.png]]
1. `ClientHello` --> : sends client capabilities (supported algorithms)
2. <-- `ServerHello`: selected connection parameters
   <-- `Certificate`: server authentication
   <-- `ServerKeyExchange`: info to generate master key
   <-- `ServerHelloDone`: finished
3. `ClientKeyExchange` --> : info to generate master key
   `[ChangeCipherSpec]` --> : client switches to encryption and informs server
4. <-- `[ChangeCipherSpec]`: server switches to encryption and informs client

Web browser checks certificates for client

**DoT**: DNS over TLS

___
### SSH
[[#Table of contents|Back to the top]]

SSH authentication
- username + password
- private + public keys

`ssh username@IP_OF_SSH_SERVER`

File transfer
- `scp username@IP_OF_SSH_SERVER:/PATH/TO/FILE_TO_COPY /DESTINATION/PATH`: from remote to local
- `scp /PATH/TO/FILE_TO_TRANSFER username@IP_OF_SSH_SERVER:/DESTINATION/PATH`: local to remote

___
### Password Attack
[[#Table of contents|Back to the top]]

Dictionary attack --> `hydra`

`hydra -l username -P wordlist.txt server service` or `service://server`

Options
- `-s PORT`: specify non-default port
- `-V` / `-vV`: verbose
- `-t n`: number of parallel connections (threads)
- `-d`: debugging (more details)

*CAPTCHA: Completely Automated Public Turing test to tell Computers and Humans Apart*