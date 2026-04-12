### Table of contents
- [[#Intro]]
- [[#Data Model]]
- [[#Dashboard]]

___
### Intro
[[#Table of contents|Back to the top]]

https://github.com/OpenCTI-Platform/opencti

Storage, analysis, visualisation and presentation of threat campaigns, malware and IOCs

Capitalise on technical and non-technical information while developing relationships between each piece of information and its primary source

Integrates with other intel tools like TheHive and MISP

___
### Data Model
[[#Table of contents|Back to the top]]

**[STIX](https://oasis-open.github.io/cti-documentation/stix/intro)** -- Structured Threat Information Expression: main knowledge schema to structure data

![[Pasted image 20250328122828.png]]

___
### Dashboard
[[#Table of contents|Back to the top]]

#### Activities
Incident reports

- Analysis: reports
- Events: record findings of suspicious/malicious activities, create associations
- Observations: technical elements, detection rules and artefacts

#### Knowledge
Tools, targets, threat actors, campaigns

- Threats 
	- Threat **Actors**
	- Intrusion **Sets**: array of **TTPs**, tools, malware and infrastructure against similar targets. **APTs** and threat groups are listed under this category due to their known pattern of actions.
	- **Campaigns**: **series of attacks** taking place
		- within a given period,
		- against specific victims
		- initiated by advanced persistent threat actors
		- who employ various TTPs
		Campaigns usually have specified objectives and are orchestrated by threat actors from a nation-state/crime syndicate
- Arsenal
	- **Malware:** identification details, mapping
	- **Attack Patterns:** TTPs
	- **Courses of Action:** concepts and technologies to defend against attack technique
	- **Tools:** tools and services developed for network maintenance, monitoring and management
	- **Vulnerabilities:** bugs, weaknesses, exposures, CVEs
- Entities: operational sectors, countries, organisations, individuals

**Arsenal** > Malware tabs
- **Overview**: entity ID, confidence level, description, relations created based on threats, intrusion sets, attack patterns, reports mentioning entity, external references
- **Knowledge**: associated reports, indicators, relations, attack pattern timeline; threats, attack vectors, events, observables
- **Analysis**: reports, guides investigation tasks
- **Indicators**: IOCs
- **Data**: files uploaded/generated for export related to entity
- **History**: element, attributes, relations changes tracking