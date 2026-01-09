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

**Save Windows Credentials**
List saved credentials: `cmdkey /list`
Test running powershell with elevated privilege without having password:
```Powershell
runas /savecred /user:admin powershell.exe
```

**IIS Configuration**
Internet Information Services: default web browser on Windows installations
`web.config` stores config of websites and credentials
- C:\inetpub\wwwroot\web.config
- C:\Windows\Microsoft.NET\Framework64\v4.0.30319\Config\web.config
Find database connection strings: 
```Powershell
type C:\Windows\Microsoft.NET\Framework64\v4.0.30319\Config\web.config | findstr connectionString
```

**PuTTY**
SSH client
```Powershell
reg query HKEY_CURRENT_USER\Software\SimonTatham\PuTTY\Sessions\ /f "Proxy" /s
```
*Note: Simon Tatham is PuTTY's creator and part of path*

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
