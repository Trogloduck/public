### Table of contents

- [[#Types of logs]]
- [[#Types of events]]
- [[#Event Viewer]]
	- [[#Events (middle pane)]]
	- [[#Actions (right pane)]]
- [[#`wevutil.exe`]]
- [[#`Get-WinEvent`]]
- [[#XPath Queries]]
- [[#Event IDs]]

___
### Types of logs
[[#Table of contents|Back to the top]]

- **System logs:** associated to OS (hardware, device drivers, system changes, ...)
- **Security logs:** logon/logoff activities
- **Application logs:** related to apps (errors, events, warnings)
- **Directory Service Events:** Active Directory changes/activities (mainly domain controllers)
- **File Replication Service Events:** associated to Windows Servers during Group Policies sharing and logon scripts to domain controllers
- **DNS Event logs:** DNS servers use these logs to record domain events and to map out
- **Custom logs:** some apps require custom data storage

### Types of events
[[#Table of contents|Back to the top]]

- **Error:** significant problem (data/functionality loss)
- **Warning:** not necessarily significant, possible future problem (low disk space for instance)
- **Information:** successful operation of app/driver/service
- **Success Audit:** successful audited security access (successful user attempt to log on to system for instance)
- **Failure Audit:** failed audited security access (failed user attempt to access a network drive for instance)

___
### Event Viewer
[[#Table of contents|Back to the top]]
>*Right-click Windows button $\rightarrow$ Event Viewer*

![[eventviewer.png]]

1. Event log **providers** hierarchical tree listing
2. General overview of **events** specific to a selected provider
3. **Actions**

>*Right-click on a provider > Properties > **Clear log** $\rightarrow$ adversaries can use this to **erase** their **tracks***

#### Events (middle pane)

**Top part**
![[top_part.png]]

- **Level:** event type (error, warning, information, ...)
- **Date and Time**
- **Source**
- **Event ID:** maps to operation/event (in above image 40962 is related to PS Console Startup), not unique (same ID will have entirely different meaning in another event log)
- **Task Category:** event category, helps organize and filter events

**Bottom part**
![[Pasted image 20250220101424.png]]
*Provides more details on selected event*

#### Actions (right pane)

- **Open Saved Log:** especially useful if remote machine is inaccessible
- **Create Custom View** and **Filter Current Log**: nearly identical, custom view allows to filter across logs
- ...

___
### `wevutil.exe`
[[#Table of contents|Back to the top]]
*Sift through thousands of events using CLI and scripting*

**`wevtutil.exe [command_name] /?`**: details about usage of command

**`wevtutil qe`**: read events from an event log, log file or using structured query

___
### `Get-WinEvent`
[[#Table of contents|Back to the top]]
*Can combine events from multiple sources and filter using XPath queries, structured XML queries and hash table queries*

https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.diagnostics/get-winevent

NB: replaced Get-EventLog

Use `Get-Help` to obtain info about syntax

**`Get-WinEvent -ListLog *`**: list all **logs**

**`-ListProvider *`**: list all **providers**
![[Pasted image 20250220140038.png]]
Name: Provider
LogLinks: Log where it's written

**Filter**
```powershell
Get-WinEvent -LogName Application | Where-Object { $_.ProviderName -Match 'WLMS' }
```

With large event logs, more efficient to use **`FilterHashtable`**:
```powershell
Get-WinEvent -FilterHashtable @{
  LogName='Application' 
  ProviderName='WLMS' 
}
```

(More about [[Hash tables]])

Accepted key/value pairs for Get-WinEvent FilterHashtable parameter
![[Pasted image 20250221094957.png]]

Recommended to to make hash table one key-value pair at a time

Event Viewer provides info to build hash table:
![[Pasted image 20250221100030.png#center]]
$\downarrow$  $\downarrow$  $\downarrow$  
![[Pasted image 20250221100100.png#center]]

___
### XPath Queries
[[#Table of contents|Back to the top]]

https://learn.microsoft.com/en-us/windows/win32/wes/consuming-events#xpath-10-limitations

https://learn.microsoft.com/en-us/previous-versions/dotnet/netframework-4.0/ms256115(v=vs.100)

wevtutil and Get-WinEvent support XPath for event filtering

Event Viewer > middle pane > bottom half > Details > XML view provides info to build XPath query:
![[Pasted image 20250221104845.png]]
1st tag of query: `*` or `Event`

`Get-WinEvent -LogName Application -FilterXPath '*'`

![[Pasted image 20250221104949.png]]
`Get-WinEvent -LogName Application -FilterXPath '*/System/'`

![[Pasted image 20250221105118.png]]
`Get-WinEvent -LogName Application -FilterXPath '*/System/EventID=100'`

Same command with wevtutil:

`wevtutil.exe qe Application /q:*/System[EventID=100]

Note: `System/EventID=100` is equivalent to `System[EventID=100]`

**`@Name`**: filter by provider: `*/System/Provider[@Name="WLMS"]`

**`and`**: Combine 2 queries: `-FilterXPath '*/System/EventID=101 and */System/Provider[@Name="WLMS"]'`


XPath for elements within **EventData**

![[Pasted image 20250221110331.png]]
Query for TargetUserName: 
```powershell
Get-WinEvent -LogName Security -FilterXPath '*/EventData/Data[@Name="TargetUserName"]="System"'
```

To display a certain property, pipe a `Select-Object`

Example:
```Powershell
Get-WinEvent -LogName Security -FilterXPath '*/EventData/Data[@Name="TargetUserName"]="Sam" and */System/EventID=4720' | Select-Object Message, ProviderName
```

___
### Event IDs
[[#Table of contents|Back to the top]]

Guidelines on which IDs to monitor for different categories (Accounts, Processes, Log Clear, etc.): [[Windows+Logging+Cheat+Sheet_ver_Oct_2016.pdf|Windows Logging Cheat Sheet]] found at https://static1.squarespace.com/static/552092d5e4b0661088167e5c/t/580595db9f745688bc7477f6/1476761074992/Windows+Logging+Cheat+Sheet_ver_Oct_2016.pdf

NSA's [[Spotting-the-Adversary-with-Windows-Event-Log-Monitoring.pdf|Spotting the Adversary with Windows Event Log Monitoring]] found at https://web.archive.org/web/20190115215749/https://apps.nsa.gov/iaarchive/customcf/openAttachment.cfm?FilePath=/iad/library/ia-guidance/security-configuration/applications/assets/public/upload/Spotting-the-Adversary-with-Windows-Event-Log-Monitoring.pdf&WpKes=aF6woL7fQp3dJiqyJL2LenrLxuHC7ztGtVNK3x

MITRE provides event IDs to monitor depending on the kind of attack: https://attack.mitre.org/techniques/T1098/ (look at "Detection")

[Microsoft - Events to Monitor](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/appendix-l--events-to-monitor)

[[Windows 10 and Windows Server 2016 Security Auditing and Monitoring Reference.pdf]] found at https://www.microsoft.com/en-us/download/details.aspx?id=52630

Some events will **not** be **generated by default**, and certain features will need to be enabled/configured on the endpoint, such as PowerShell logging. This feature can be enabled via **Group Policy** (look for it in the searchbar) or the **Registry**.
- [About Logging Windows](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_logging_windows?view=powershell-7.5&viewFallbackFrom=powershell-7.1)
- [Greater visibility through PowerShell Logging](https://cloud.google.com/blog/topics/threat-intelligence/greater-visibility/?hl=en)
- [Configure PowerShell logging to see PowerShell anomalies in Splunk UBA](https://docs.splunk.com/Documentation/UBA/5.0.4/GetDataIn/AddPowerShell)

**Audit Process Creation** must be enabled to generate event ID 4688 $\rightarrow$ **command-line process auditing**

[Explore command line process auditing](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/component-updates/command-line-process-auditing#try-this-explore-command-line-process-auditing)

