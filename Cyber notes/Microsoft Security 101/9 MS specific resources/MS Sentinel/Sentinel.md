Cloud-native SIEM/SOAR solution
- Collection
- Detection
- Investigation
- Response
- Proactive hunting
#### Data collection
- **Out of the box connectors**: MS sources
- **Custom connectors**: custom connector to forward data collection from source that doesn't have an out of the box connector
- **Data normalization**: ASIM (Advanced Security Information Model)
#### Threat detection
- **Analytics**: group alerts into incidents
- **MITRE ATT&CK coverage**: accounts for adversary tactics and techniques from MITRE framework
- **Threat intelligence**: integrate various sources
- **Watchlists**: correlate with data from watchlists
- **Workbooks**: interactive visual reports
#### Threat investigation
- **Incidents**: aggregation of relevant evidence
- **Hunts**: proactively hunt for security threats
- **Notebooks**: Jupyter notebooks
	- Custom analytics with Python machine learning features
	- Data visualization
	- Integrate data sources
#### Incident response
- **Automation rules**: centralized small sets of rules
- **Playbooks**: collection of remediation actions that can be run manually or automatically (triggered by automation rule) for specific alerts/incidents
___

MS Sentinel Content Hub: manage built-in solutions

Enabled through Azure portal

Access through Azure portal or MS Defender portal (more unified: MS Sentinel + XDR + Copilot)
___
#### AI integration
Security Copilot plugins
- MS Sentinel: incidents, workspaces
- Natural language to KQL: threat hunting
