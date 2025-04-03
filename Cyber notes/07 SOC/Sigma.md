### Table of contents
- [[#Intro]]
- [[#Rule Syntax]]
	- [[#Fields]]
	- [[#Search Identifiers and Condition Expressions]]
- [[#Rule Writing & Conversion]]
	- [[#Context]]
	- [[#Writing]]
		- [[#1. Intel Analysis]]
		- [[#2. Rule Identification]]
		- [[#3. Log Source]]
		- [[#4. Detection Description]]
		- [[#5. Rule Metadata]]
	- [[#Conversion]]
		- [[#Sigmac]]
		- [[#undercoder.io]]

___
### Intro
[[#Table of contents|Back to the top]]

*Sigma is for log files as Snort is for network traffic, and Yara is for files*

Open-source generic signature language to describe log events in structured standardized format, allows quick sharing of detection methods

Development process
- **Sigma Rule Format:** generic structured .yml log descriptions
- **Sigma Converter:** python scripts process rules on backend, perform custom field matching based on specified SIEM query language
- **Machine Query:** resulting search query filter out alerts during investigations

Use cases
- Make **detection methods** and **signatures shareable** alongside IOCs and Yara rules
- Write **SIEM searches** that avoid vendor lock-in
- Write **custom detection** rules for malicious behavior based on specific conditions

More info: https://github.com/SigmaHQ/sigma

___
### Rule Syntax

Written in **[[YAML]]**
#### Fields
[[#Table of contents|Back to the top]]

![[Pasted image 20250403105133.png|350]]

- **Title:** what it is supposed to detect

- **ID:** globally unique identifier mainly used by Sigma developers to maintain identification order for publicly published rules, UUID format 
	- ***Related***: references to related rule IDs, form relationships between detections
	    - ***Derived***: rule has sprung from another rule (active or not)
	    - ***Obsolete***: rule is no longer used
	    - ***Merged***: rule combines linked rules
	    - ***Renamed***: rule previously identified under different ID, has been changed due to changes in naming schemes / avoiding collisions 
	    - ***Similar***: points to corresponding rules, same detection content applied to different log sources

- **Status:** stage in which rule maturity is at
	- ***Stable***: rule may be used in production environments and dashboards
	- ***Test***: rule is being tried, could require fine-tuning
	- ***Experimental***: rule is very generic, is being tested, could lead to false results, be noisy, identify interesting events
	- ***Deprecated***: rule has been replaced, would no longer yield accurate results.`related` field creates associations between current rule and deprecated one
	- ***Unsupported***: rule not usable in current state (unique correlation log, homemade fields)

- **Description:** more context about rule, intended purpose  
```YAML
title: WMI Event Subscription
id: 0f06a3a5-6a09-413f-8743-e6cf35561297
status: test
description: Detects creation of WMI event subscription persistence method.
```

- **Logsource:** log data used for detection, optional attributes:
    - ***Product***: selects all log outputs of particular product (Windows, Apache, ...)
    - ***Category***: selects log files written by selected product (firewall, web, antivirus, ...)
    - ***Service***: selects subset of the logs from selected product (sshd on Linux, Security on Windows, ...)
    - ***Definition***: describes log source, applied configurations
```YAML
logsource:
   product: windows    
   category: wmi_event 
```

- **Detection:** parameters of malicious activity we need an alert for. 
	- ***Search identifiers***: fields, values detection should be searching for
	- ***Condition expression***: action to be taken on detection (selection, filtering)
```shell-session
detection:
  selection:
    EventID:  # This shows the search identifier value
      - 19    # This shows the search's list value
      - 20
      - 21
  condition: selection
```
*Detection modifier looks for Windows Event IDs 19-21 logs*
*Condition informs detection engine to match and select identified logs*

- **FalsePositives:** known false positive outputs based on log data that may occur

- **Level:** severity with which the activity should be taken under the written rule. 5 levels: Informational < Low < Medium < High < Critical

- **Tags:** information to categorize rule (CVE numbers, MITRE ATT&CK TTPs). [Predefined tags](https://github.com/SigmaHQ/sigma/wiki/Tags)
```YAML
falsepositives:
- Exclude legitimate (vetted) use of WMI event subscription in your network
 
level: medium
 
tags:
- attack.persistence # Points to the MITRE tactic.
- attack.t1546.003 # Points to the MITRE technique.
```

##### Search Identifiers and Condition Expressions
[[#Table of contents|Back to the top]]

**Search Identifiers**

**List**: follow "***OR***" logical operation
```YAML
detection:
  selection:
    HostApplication|contains:
      - 'powercat'
      - 'powercat.ps1'
  condition: selection
```
*contains 'powercat' OR 'powercat.ps1'*

**Maps**: follow "***AND***" logical operation
```YAML
detection:
  selection:
    Image|endswith:
      - '/rm' # covers /rmdir as well
      - '/shred'
    CommandLine|contains:
      - '/var/log'
      - '/var/spool/mail'
  condition: selection
```
*has to satisfy Image condition AND CommandLine condition*

- **Transformation modifiers:** change values provided, can modify logical operations between values
    - **`contains`**: value matched anywhere in field
    - **`all`**: search condition has to match all listed values (turns OR into AND)
    - **`base64`**: looks at values encoded with Base64
    - **`endswith`**: value expected at end of field
    - **`startswith`**: value at beginning of field

- **Type modifiers:** change type of value or value itself.
	- Currently, only usable type modifier is `re` (supported by Elasticsearch queries): handle value as regular expression


**Condition Expressions**

Supported terms
- `and`, `or`
- `1 of` search-identifiers
- `ALL of` search-identifiers
- `not`

```YAML
detection:
  include1:
    - 'str1'
  include2:
    - 'str2'
  exclude1:
    - 'str3'
  exclude2:
    - 'str4'
 # both include must match
 condition: include1 and include2
 # 1 of include must match
 condition: 1 of include*
 # 1 of include must match and exclude shouldn't matc
 condition: 1 of include* and not ALL of exclude*
```

___
### Rule Writing & Conversion
#### Context
[[#Table of contents|Back to the top]]

https://tryhackme.com/room/sigma

- Administrators use remote tools to configure, patch, maintain devices
- AnyDesk (legitimate remote tool) can be downloaded and installed silently on a user's machine to conduct malicious activity, using the file description below. (Source: [TheDFIRReport](https://twitter.com/TheDFIRReport/status/1423361127472377860))
- As SOC analyst, analyse intel and write Sigma rule to detect AnyDesk installation on Windows devices

SIGMA specification file available in `/root/Rooms/sigma/Sigma_Rule_File.yml`

![[Pasted image 20250403135537.png]]

#### Writing
##### 1. Intel Analysis
[[#Table of contents|Back to the top]]

From file description
- **Source URL**: **`$url`** variable, download source for software
- **Destination File**: **`$file`** variable, destination directory for download
- **Installation Command**: various instances of `CMD.exe` used to install and set user password by the script. Installation attributes: **`--install`**, **`--start-with-win`**, **`--silent`**, ...

- **Persistence**: create user account **`oldadministrator`**, give user elevated privileges to run other tasks
- **Registry Edit**: new user is added to **`SpecialAccounts`** user list.

##### 2. Rule Identification
[[#Table of contents|Back to the top]]

```YAML
title: AnyDesk Installation
status: experimental
description: AnyDesk Remote Desktop installation can be used by attacker to gain remote access.
```

##### 3. Log Source
[[#Table of contents|Back to the top]]

Type of targeted devices, type of events

Here: Windows, process and file creation
```YAML
logsource:
  category: process_creation
  product: windows
```

##### 4. Detection Description
[[#Table of contents|Back to the top]]

From intel, commands contain strings: `install`, `start-with-win`
Directory: `C:\ProgramData\AnyDesk.exe`
```YAML
detection:
  selection:
    CommandLine|contains|all:
      - '--install'
      - '--start-with-win'
    CurrentDirectory|contains:
      - 'C:\ProgramData\AnyDesk.exe'
  condition: selection
```

##### 5. Rule Metadata
[[#Table of contents|Back to the top]]



#### Conversion
##### Sigmac
[[#Table of contents|Back to the top]]



##### undercoder.io
[[#Table of contents|Back to the top]]



___
