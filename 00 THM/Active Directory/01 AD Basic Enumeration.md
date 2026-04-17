https://tryhackme.com/room/adbasicenumeration

### Table of contents
- [[#Mapping Out Network]]
- [[#Network Enumeration with SMB]]
- 

___
### Mapping Out Network
[[#Table of contents|Back to the top]]

VPN access to AD, no credentials yet
Goals: discover AD environment structure, identify hosts, map out network
Scope: `10.211.10.0/24` subnet

##### Host Discovery

**`fping`**
`fping -agq 10.211.10.0/24`
- `a`: alive systems
- `g`: generate list
- `q`: quiet (not verbose)

`10.211.11.1`: gateway
`10.211.11.250`: server
--> don't add these to the results

Add other addresses to `hosts.txt` for subsequent use (one address per line)

**`nmap`**
`nmap -sn 10.211.11.0/24`: ping scan, no port scan

##### Port Scanning

Identify DC (Domain Controller) --> determine which AD-related services are used and can be exploited

Common AD ports-protocols

| Port | Protocol           | What it Means                                 |
| ---- | ------------------ | --------------------------------------------- |
| 88   | Kerberos           | Potential for Kerberos-based enumeration      |
| 135  | MS-RPC             | Potential for RPC enumeration (null sessions) |
| 139  | SMB/NetBIOS        | Legacy SMB access                             |
| 389  | LDAP               | LDAP queries to AD                            |
| 445  | SMB                | Modern SMB access, critical for enumeration   |
| 464  | Kerberos (kpasswd) | Password-related Kerberos service             |

`nmap -p 88,135,139,389,445 -sV -sC -iL hosts.txt`
- `sV`: version detection
- `sC`: NSE (Nmap Scripting Engine) in default category
- `iL`: read target hosts from file

DC will often have 88 (Kerberos), 389 (LDAP), 445 (SMB) open, with banners like "Windows Server" / domain names revealed in nmap output

More exhaustive assessment
`nmap -sS -p- -T3 -iL hosts.txt -oN full_port_scan.txt`
- `sS`: TCP SYN scan, stealthier than full connect scan
- `-p-`: all 65 535 TCP ports
- `-T3`: "normal" timing template
- `-oN full_port_scan.txt`: outputs results to file

___
### Network Enumeration with SMB
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
### 
[[#Table of contents|Back to the top]]



___
### 
[[#Table of contents|Back to the top]]



___
