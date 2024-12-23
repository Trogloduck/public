#### Integration
##### Standalone
Enabled through plugins accessed through **Copilot portal**
- **MS Defender XDR**
	- Analyze files
	- Generate incident reports
	- Generate guided responses
	- List incidents and related alerts
	- Summarize security state of device
	- ...
- **Natural language to KQL for MS Defender XDR**: convert nat language to KQL query for threat hunting
##### Embedded
Directly in **XDR**, same functionalities
##### Guided responses
Only available for phishing, business email compromise, ransomware
- **Triage**: incident either informational / true positive / false positive
- **Containment**: recommended actions to contain incident
- **Investigation**: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ for further investigation
- **Remediation**:  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ for remediation
___
#### Analyze scripts and codes
___
#### Generate KQL queries
Example: "Give me all the devices that signed in within the last 10 minutes." > Copilot generate KQL query > User adds and runs query
___
#### Incident reports
Eases report writing: collects and compiles from multiple sources, ensuring comprehensive and concise report
___
#### Analyze files
Incident graph: full scope of attack, how it spread over time, origin point, end point; from there show files that were on the path of the attack
___
#### Summarize devices and identities
___
#### Embedded to Standalone
"Open in Security Copilot" from deeper, cross product investigation, all Copilot capabilities