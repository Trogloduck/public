https://tryhackme.com/room/adauthenticatedenumeration

### Table of contents
- [[#AS-REP Roasting]]
- 

___
### AS-REP Roasting
[[#Table of contents|Back to the top]]

1. **Enumeration** – Identify Vulnerable Accounts

Accounts that have Kerberos pre-authentication disabled (`UF_DONT_REQUIRE_PREAUTH` flag is set) --> anyone can request Kerberos ticket (specifically AS-REP) --> account passwords encrypted hashes exposed

[Rubeus](https://github.com/GhostPack/Rubeus) (Windows only)
e.g. : `Rubeus.exe asreproast`

[Impacket’s GetNPUsers.py](https://github.com/fortra/impacket) (Linux/Windows)
e.g. : `GetNPUsers.py tryhackme.loc/ -dc-ip 10.211.12.10 -usersfile users.txt -format hashcat -outputfile hashes.txt -no-pass`

2. **Exploitation** - Password Hashes Cracking & Network Access

[Hashcat](https://hashcat.net/hashcat/)

For AS-REP, use 18200 mode
e.g. : `hashcat -m 18200 hashes.txt wordlist.txt`


**Mitigation**
- Enforce pre-authentication
- Strong, complex paswords
- Monitor anomalous AS-REP requests on KDC

___
### Manual Enumeration
[[#Table of contents|Back to the top]]

##### 1. `whoami`

Credentials: asrepuser1:qwerty123!
`ssh asrepuser1@10.211.12.20`

`whoami` (username, domain/pc name), `whoami /all` (groups, privileges, SID)

##### 2. **Check Your Privileges**

- **`SeImpersonatePrivilege`**: impersonate other user's security context after authentication (--> potato attack)
- **`SeAssignPrimaryTokenPrivilege`**: assign other user's primary token to a new process, used in conjunction with SeImpersonatePrivilege
- **`SeBackupPrivilege`**: read any file on system, ignoring file permissions (--> dump sensitive files like SAM or SYSTEM hive)
- **`SeRestorePrivilege`**: write to any file or registry key, ignoring file permissions
- **`SeDebugPrivilege`**: attach a debugger to any process (--> dump memory from LSASS, extract credentials, inject malicious code into privileged processes)

##### 3. System & Domain Info
*Is machine part of AD domain? Hostname, domain, workgroup?*

**`hostname`** --> common for DCs to have "dc" in their hostname, "pc-\[digits]" for pcs joined to domain

**`systeminfo`**: OS version, installed hotfixes, domain & workgroup info
- `systeminfo | findstr /B "OS"`
- `systeminfo | findstr /B "Domain"`

**`set`**: discover info in environment variables (in PowerShell: `Get-ChildItem Env:`/`dir env:`)

##### 4. Enumerate Users & Groups





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
