https://tryhackme.com/room/gobusterthebasics

### Table of contents
- [[#Intro]]
- [[#Directory and File Enumeration]]
- [[#Subdomain Enumeration]]
- [[#Vhost Enumeration]]

___
### Intro
[[#Table of contents|Back to the top]]

Written in Golang
Used in reconnaissance phase: enumerate web directories, subdomains, virtual hosts, Amazon S3 buckets, Google Cloud Storage by brute force, using specific wordlists and handling the incoming responses

https://github.com/OJ/gobuster

`gobuster --help`

Example
`gobuster dir -u "http://www.example.thm/" -w /usr/share/wordlists/dirb/small.txt -t 64`
- `gobuster dir`: directory and file enumeration mode
- `-u "http://www.example.thm/"`: target URL
- `-w /usr/share/wordlists/dirb/small.txt`: wordlist to be used for the brute force. Each entry will be used to try to send a GET request with "`http://www.example.thm/entry`"
- `-t 64`: number of threads, improves performance drastically

___
### Directory and File Enumeration
[[#Table of contents|Back to the top]]

`gobuster dir --help`

`gobuster dir -u "http://www.example.thm" -w /path/to/wordlist`

Example: `gobuster dir -u "http://www.example.thm" -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -r`
*`-r redirect responses and automatically navigate to URL`*

Gobuster doesn't enumerate recursively (inside of a directory inside the domain). So if a directory seems particularly interesting, enumerate inside the directory. 

___
### Subdomain Enumeration
[[#Table of contents|Back to the top]]

`gobuster dns --help`

`gobuster dns -d example.thm -w /path/to/wordlist`

Example: `gobuster dns -d example.thm -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt`

___
### Vhost Enumeration
[[#Table of contents|Back to the top]]

Virtual hosts: different websites on same machine
Look like subdomains but are IP-based and running on same server while subdomains are set up in DNS
- **`vhost`** tries to navigate to **URL** created by combination of hostname (-u flag) with entry of wordlist
- **`dns`** does DNS lookup to **FQDN** created by combination of hostname and entry

`gobuster vhost --help`

`gobuster vhost -u "http://example.thm" -w /path/to/wordlist --append-domain`

`gobuster vhost -u "http://10.80.179.7" --domain example.thm -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt --append-domain --exclude-length 250-320`
- `--exclude-length`: filters responses, filter out false positives. We expect to get a 200 OK response back to have a true positive.