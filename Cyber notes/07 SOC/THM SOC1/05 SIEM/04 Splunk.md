### Table of contents
- [[#Components]]: [[#Forwarder]], [[#Indexer]], [[#Search Head]]
- 

___
### Components
[[#Table of contents|Back to the top]]

#### Forwarder
Lightweight agent installed on monitored endpoints, collect data and send Splunk instance
- Web server: web traffic
- Windows machine: Windows Event Logs, PowerShell, Sysmon data
- Linux host: host-centric logs
- Database: DB connection requests, responses, errors
#### Indexer
Processing data from Forwarder: normalizes into field-value pairs, determines datatype, stores as events $\rightarrow$ easy to search/analyze
#### Search Head
Splunk Search Processing Language to search indexed logs $\rightarrow$ request sent to Indexer $\rightarrow$ relevant events returned as field-value pairs
Present data as charts (pie, bar, column, ...)

___
### Navigating
[[#Table of contents|Back to the top]]

Bar
- Messages
- Settings
- Activity: jobs progress
- Help
- Find

