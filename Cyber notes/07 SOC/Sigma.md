### Table of contents
- [[#Intro]]
- [[#Rule Syntax]]
- 

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
- Make detection methods and signatures shareable alongside IOCs and Yara rules
- Write SIEM searches that avoid vendor lock-in
- Share signatures with threat intelligence communities
- Write custom detection rules for malicious behavior based on specific conditions

More info: https://github.com/SigmaHQ/sigma

___
### Rule Syntax
[[#Table of contents|Back to the top]]

Written in **[[YAML]]**

Mandatory/Optional fields

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

- **Detection:** A required field in the detection rule describes the parameters of the malicious activity we need an alert for. The parameters are divided into two main parts: the search identifiers - the fields and values that the detection should be searching for -  and condition expression - which sets the action to be taken on the detection, such as selection or filtering. More on this is below.

    This rule has a detection modifier that looks for logs with one of Windows Event IDs 19, 20 or 21. The condition informs the detection engine to match and select the identified logs.

```shell-session
detection:
  selection:
    EventID:  # This shows the search identifier value
      - 19    # This shows the search's list value
      - 20
      - 21
  condition: selection
```

- **FalsePositives:** A list of known false positive outputs based on log data that may occur.

- **Level:** Describes the severity with which the activity should be taken under the written rule. The attribute comprises five levels: Informational -> Low -> Medium -> High -> Critical

- **Tags:** Adds information that may be used to categorise the rule. Tags may include values for CVE numbers and tactics and techniques from the MITRE ATT&CK framework. Sigma developers have defined a list of [predefined tags](https://github.com/SigmaHQ/sigma/wiki/Tags)

