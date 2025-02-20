- [[#Types of logs]]
- [[#Types of events]]
- [[#Event Viewer]]
	- [[#Events (middle pane)]]
	- [[#Actions (right pane)]]
- [[#`wevutil.exe`]]
- [[#`Get-WinEvent`]]

___
### Types of logs

- **System logs:** associated to OS (hardware, device drivers, system changes, ...)
- **Security logs:** logon/logoff activities
- **Application logs:** related to apps (errors, events, warnings)
- **Directory Service Events:** Active Directory changes/activities (mainly domain controllers)
- **File Replication Service Events:** associated to Windows Servers during Group Policies sharing and logon scripts to domain controllers
- **DNS Event logs:** DNS servers use these logs to record domain events and to map out
- **Custom logs:** some apps require custom data storage

### Types of events

- **Error:** significant problem (data/functionality loss)
- **Warning:** not necessarily significant, possible future problem (low disk space for instance)
- **Information:** successful operation of app/driver/service
- **Success Audit:** successful audited security access (successful user attempt to log on to system for instance)
- **Failure Audit:** failed audited security access (failed user attempt to access a network drive for instance)

___
### Event Viewer
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
*Sift through thousands of events using CLI and scripting*

**`wevtutil.exe [command_name] /?`**: details about usage of command

**`wevtutil qe`**: read events from an event log, log file or using structured query

___
### `Get-WinEvent`

