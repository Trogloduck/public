https://tryhackme.com/room/windowsprivesc20

### Table of contents
- [[#Intro]]

___
### Intro
[[#Table of contents|Back to the top]]

Users
- **Administrator** (∈ admin group): full access
- **Standard** (∈ users group): limited access

Built-in accounts used by OS
- **SYSTEM / LocalSystem:** perform internal tasks, higher privilege than admin
- **Local Service:** default account to run Windows services with minimum privilege, anonymous connections over network
- **Network Service:** default account to run Windows services with minimum privilege, computer credentials to authenticate through network

___
### Passwords Harvesting
[[#Table of contents|Back to the top]]

**Unattended Windows Installations**
Installing Windows on large number of hosts, deploying single OS image on several hosts, requires admin account --> might be stored
- C:\Unattend.xml
- C:\Windows\Panther\Unattend.xml
- C:\Windows\Panther\Unattend\Unattend.xml
- C:\Windows\system32\sysprep.inf
- C:\Windows\system32\sysprep\sysprep.xml

**Powershell History**
Retrieve password as part of command line
```cmd
type %userprofile%\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt
```

```PowerShell
type $Env:userprofile\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt
```


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
