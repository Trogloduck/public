*Log system activity to Windows event log, most commonly used in conjunction with SIEM*
### Table of contents
- [[#Overview]]
- [[#Installation]]
- [[#Configuration]]
- [[#Monitor logs]]
- [[#Config file]]
- [[#Event IDs]]
- [[#Best practices]]
- [[#Hunting Metasploit]]

https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon
https://github.com/microsoft/SysmonForLinux

___
### Overview
[[#Table of contents|Back to the top]]

Sysmon includes **29** different types of **Event IDs**

Events within Sysmon stored in `Applications and Services Logs/Microsoft/Windows/Sysmon/Operational`

___
### Installation
[[#Table of contents|Back to the top]]

**Kali installation** (Debian 12)

Register Microsoft key and feed:
```bash
wget -q https://packages.microsoft.com/config/debian/12/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb
```

Installation:
```bash
sudo apt-get update
sudo apt-get install apt-transport-https
sudo apt-get update
sudo apt-get install sysmonforlinux
```

___
### Configuration
[[#Table of contents|Back to the top]]

*Determines which events to include/exclude, will vary depending on SOC team*

**Config by SwiftOnSecurity**

https://github.com/SwiftOnSecurity/sysmon-config

```bash
sysmon -accepteula -i sysmonconfig-export.xml
```

**Custom config**

Save config in sysmonconfig.xml file, then

```bash
# 1. stop sysmon
sudo systemctl stop sysmon
# 2. update config
sudo sysmon -c /PATH_TO/sysmonconfig.xml
# 3. start sysmon
sudo systemctl start sysmon
```

___
### Monitor logs
[[#Table of contents|Back to the top]]

For robots
```bash
sudo journalctl -u sysmon
```

For humans
```bash
sudo journalctl -u sysmon | sudo /opt/sysmon/sysmonLogView -X
```

___
### Config file
[[#Table of contents|Back to the top]]

Schema version: `sysmon -s`
```xml
<Sysmon schemaversion="4.90">
    <!-- Specify hash algorithm -->
    <HashAlgorithms>sha256</HashAlgorithms>
    <!-- Check if certificate used for signing has been revoked -->
    <CheckRevocation />
    <!-- Name of directory to store logs -->
    <ArchiveDirectory>%SystemRoot%\Sysmon</ArchiveDirectory>
    <!-- Size of fields for Sysmon on Linux -->
    <FieldSizes>CommandLine:50,Image:50</FieldSizes>
    <!-- Perform DNS lookup for network connection events -->
    <DnsLookup>true|false</DnsLookup>
    <EventFiltering>
    …
    </EventFiltering>
</Sysmon>
```

___
### Event IDs
[[#Table of contents|Back to the top]]

##### 1: Process Creation
$\rightarrow$ Look for suspicious processes / processes with typos
- XML tags: CommandLine, Image
##### 3: Network Connection
$\rightarrow$ Files, sources, suspicious binaries, opened ports
- XML tags: Image, DestinationPort
##### 7: Image Loaded
$\rightarrow$ **DLLs** loaded by processes $\rightarrow$ [[DLL]] injection, DLL hijacking. Caution: this event ID causes a high system load
- XML tags: Image, Signed, ImageLoaded, Signature
##### 8: CreateRemoteThread
$\rightarrow$ Processes injecting code into other processes
- XML tags: SourceImage, TargetImage, StartAddress, StartFunction
##### 11: File Created
$\rightarrow$ Created or overwritten
- XML tags: TargetFilename
##### 12/13/14: Registry Event
$\rightarrow$ Changes in registry $\rightarrow$ persistence, credential abuse
- XML tags: TargetObject
##### 15: FileCreateStreamHash
$\rightarrow$ Files created in alternate data stream $\rightarrow$ hide malware
- XML tags: TargetFilename
##### 22: DNS
$\rightarrow$ Exclude trusted domains
- XML tags: QueryName

*Example*:
```xml
<RuleGroup name="" groupRelation="or">  
	<DnsQuery onmatch="exclude">
		<QueryName condition="end with">.microsoft.com</QueryName>  
	</DnsQuery>  
</RuleGroup>
```

___
### Best practices
[[#Table of contents|Back to the top]]

- Exclude > Include
- CLI for more control: `Get-WinEvent`, `wevtutil.exe`
- Know your environment: know normal signals to detect abnormal signals

___
### Hunting Metasploit
[[#Table of contents|Back to the top]]

*Commonly used exploit framework for pentesting, can be used to easily run exploits on machine and connect back to meterpreter shell*

By default, Metasploit uses port **4444** (https://docs.google.com/spreadsheets/d/17pSTDNpa0sf6pHeRhusvWG6rThciE8CsXTSlDUAZDyo)

Start investigation: look at packet captures from date of log to begin looking for further information about adversary

```powershell
get-winevent -path .\Hunting_Metasploit_1609814643558.evtx -filterxpath '*/System/EventID=3 and */EventData/Data[@Name="DestinationPort"] and */EventData/Data=4444'
```
*Look for network event (EventID = 3) on Metasploit port (4444)*

___
### Detecting Mimikatz
[[#Table of contents|Back to the top]]

*Commonly used to dump credentials from memory along with other Windows post-exploitation activity, mainly known for dumping [[LSASS]]*

We can hunt for the file created, execution of the file from an elevated process, creation of a remote thread, and processes Mimikatz creates

[Process Injection](https://attack.mitre.org/techniques/T1055/), [Mimikatz](https://attack.mitre.org/software/S0002/)

##### Detecting File Creation

Looking for files created with name Mimikatz by including this config snippet
```xml
<RuleGroup name="" groupRelation="or">  
	<FileCreate onmatch="include">  
		<TargetFileName condition="contains">mimikatz</TargetFileName>  
	</FileCreate>  
</RuleGroup>
```

##### Hunting Abnormal LSASS Behavior

**ProcessAccess** event ID (10) to hunt for abnormal LSASS behavior

**LSASS** accessed by other process than **svchost.exe**: suspicious $\rightarrow$ investigate

Config snippet
```xml
<RuleGroup name="" groupRelation="or">  
	<ProcessAccess onmatch="include">
		<TargetImage condition="image">lsass.exe</TargetImage>  
	</ProcessAccess>  
</RuleGroup>
```

Practical example of the THM room: *Open `C:\Users\THM-Analyst\Desktop\Scenarios\Practice\Hunting_LSASS.evtx` in Event Viewer to view an attack using an obfuscated version of Mimikatz to dump credentials from memory*
1. Download sysmon
2. Create `sysmon-config.xml` with snippet included, save in same folder as sysmon.exe
```xml
<Sysmon schemaversion="4.90">
  <EventFiltering>
    <RuleGroup name="" groupRelation="or">
      <ProcessAccess onmatch="include">
        <TargetImage condition="image">lsass.exe</TargetImage>
      </ProcessAccess>
    </RuleGroup>
  </EventFiltering>
</Sysmon>   
```
3. Install sysmon with config: `sysmon -accepteula -i sysmon-config.xml`
4. Open Event Viewer and look for event ID 10 (ProcessAcess $\rightarrow$ LSASS)

It's often necessary to exclude normal processes (svchost.exe)
```xml
<ProcessAccess onmatch="exclude">  
	<SourceImage condition="image">svchost.exe</SourceImage>  
</ProcessAccess>
```

##### Detecting LSASS Behavior with PowerShell

```PowerShell
Get-WinEvent -Path C:\Users\THM-Analyst\Desktop\Scenarios\Practice\Hunting_Mimikatz.evtx -FilterXPath '*/System/EventID=10 and */EventData/Data[@Name="TargetImage"] and */EventData/Data="C:\Windows\system32\lsass.exe"'
```
