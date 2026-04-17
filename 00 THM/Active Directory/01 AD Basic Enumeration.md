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

Enumerate network shares with SMB (Server Message Block)

##### Services

MS Windows and AD-related ports
- `88` (Kerberos): authentication --> ticket attacks like Pass-the-Ticket and Kerberoasting
- `135` (RPC Endpoint Mapper): Remote Procedure Calls --> identify services for lateral movement / RCE via DCOM
- `139` (NetBIOS Session Service): file sharing in older Windows systems --> null sessions, information gathering
- `389` (LDAP): Lightweight Directory Access Protocol, in plaintext --> enumerating AD objects, users, policies
- `445` (SMB): file sharing, remote admin --> EternalBlue, SMB relay attacks, credential theft
- `636` (LDAPS): Secure LDAP, encrypted, can still expose AD structure if misconfigured --> certificate-based attacks like AD CS exploitation

##### SMB Shares

**1. Enumerate**
*No credentials --> try to connect to a share anonymously ("null session")*

`smbclient -L //10.211.11.10 -N`
- `L`: list shares
- `N`: null session

(smbmap is Python-based)
`PATH/TO/smbmap -H 10.211.11.10`

`nmap -p445 --script smb-enum-shares 10.211.11.10`


**2. Access**
*Shares with READ, WRITE rights should be accessible*

`smbclient //10.211.11.10/share_name -N`: connect to share
`get file_name`: download file to attacker machine

If credentials found --> `--user=username --password=password` or `-U 'username%password`
Domain accounts: specify `-W`

**Other Tools**
`impacket-smbclient`: Python implementation of `smbclient`
[CrackMapExec](https://www.kali.org/tools/crackmapexec/): not only for post-exploitation, also enumeration, SMB modules, listing shares, testing credentials, ...
`enum4linux`/`enum4linux-ng`: extensive SMB enumeration

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
