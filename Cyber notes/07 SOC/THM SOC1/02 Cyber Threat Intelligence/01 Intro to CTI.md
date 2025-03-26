### Table of contents
- [[#Sources of intel]]
- [[#Intel classification]]
- [[#Lifecycle]]
- [[#Frameworks]]: [[#TAXII]], [[#STIX]]

___
Evidence-based knowledge about adversaries: indicators, tactics, motivations, actionable advice against them
$\rightarrow$ Protect assets, inform cyber security teams and management business decisions

- **Data:** ***discrete*** indicators (IP, URLs, hashes, ...)
- **Information:** ***combination*** of multiple data points that answer questions such as “How many times have employees accessed tryhackme.com within the month?”
- **Intelligence:** ***correlation*** of data and information to extract patterns of actions based on contextual analysis

___
### Sources of intel

- **Internal**
    - Corporate security events such as vulnerability assessments and incident response reports
    - Cyber awareness training reports
    - System logs and events
- **Community**
    - Open web forums
    - Dark web communities for cybercriminals
- **External**
    - Threat intel feeds (Commercial & Open-source)
    - Online marketplaces
    - Public sources: government data, publications, social media, financial/industrial assessments

___
### Intel classification

- **Strategic Intel:** high-level intel, org’s threat landscape, risk areas based on trends, patterns, emerging threats
- **Technical Intel:** evidence, artefacts of attack used by adversary $\rightarrow$ baseline attack surface
- **Tactical Intel:** TTPs $\rightarrow$ security controls, real-time investigations
- **Operational Intel:** specific motives/intent $\rightarrow$ org's critical assets -- potential targets (people, processes, technologies)

___
### Lifecycle

1. **Direction**: defining goals (which questions we ask), identifying
	- Assets to be defended
	- Potential impact on asset loss/damage
	- Data/intel sources for defense
	- Defense tools/resources
2. **Collection**: automated data gathering
3. **Processing**: extract, sort, organize, correlate $\rightarrow$ **SIEM**
4. **Analysis**: derive insights $\rightarrow$ specific investigation, defense action plan, security controls, resource reallocation
5. **Dissemination**: share to different stakeholders with appropriate language, focus, level of details
6. **Feedback**: regular interaction between teams to keep lifecycle ongoing

___
### Frameworks

MITRE ATT&CK, Cyber Kill Chain, Diamond Model

#### TAXII
https://oasis-open.github.io/cti-documentation/taxii/intro

Trusted Automated eXchange of Indicator Information: protocols for securely exchanging threat intel to have near real-time detection, prevention, mitigation

2 sharing models:
- **Collection**: threat intel collected and hosted by a producer upon request by users using a request-response model
- **Channel**: threat intel pushed to users from a central server through a publish-subscribe model

#### STIX
https://oasis-open.github.io/cti-documentation/stix/intro

Structured Threat Information Expression: language developed for the "specification, capture, characterization and communication of standardized cyber threat information", provides defined relationships between sets of threat info such as observables, indicators, adversary TTPs, attack campaigns, ...