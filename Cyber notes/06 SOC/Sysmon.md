*Log system activity to Windows event log, most commonly used in conjunction with SIEM*
### Table of contents
- [[#Overview]]
- [[#Installation]]
- [[#Configuration]]
- [[#Monitor logs]]
- [[#Config file]]

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
<Sysmon schemaversion="4.81">
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
