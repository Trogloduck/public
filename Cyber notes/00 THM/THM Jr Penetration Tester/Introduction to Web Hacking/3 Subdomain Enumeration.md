*Expand attack surface, more potential points of vulnerability*

### Table of contents
- [[#OSINT]]
- [[#DNS Brute Force]]
- [[#Virtual Hosts]]

___
### OSINT

- SSL/TLS **Certificates**
**https://crt.sh/**: certificate search for particular domain $\rightarrow$ find subdomains

- **Search Engines**
**`site:*.domain.com -site:www.domain.com`**: only include subdomains

- **Sublist3r**
***Automates*** SSL/TLS certificates, search engines and DNS brute force into one tool
**`./sublist3r.py -d target_URL`**

---
### DNS Brute Force
[[#Table of contents|Back to the top]]

Automated requests for commonly used subdomains

dnsrecon

`dnsrecon -t brt -d target_URL`

___
### Virtual Hosts
[[#Table of contents|Back to the top]]

For subdomains not accessible on public DNS server (development version, admin portal, ...)
- Private DNS server
- Developer's machine in `/etc/hosts` or `C:\Windows\System32\Drivers\etc\hosts`: maps domain names to IP addresses

```Shell
ffuf -w /usr/share/wordlists/SecLists/Discovery/DNS/namelist.txt -H "Host: FUZZ.acmeitsupport.thm" -u http://10.10.201.27
```

```Shell
ffuf -w /usr/share/wordlists/SecLists/Discovery/DNS/namelist.txt -H "Host: FUZZ.acmeitsupport.thm" -u http://10.10.201.27 -fs {size}
```
*Add most common size from previous result to filter results*