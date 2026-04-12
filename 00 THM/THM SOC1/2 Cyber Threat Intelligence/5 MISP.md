### Table of contents
- [[#Intro]]
- [[#Event Actions]]
- [[#Feeds & Taxonomies]]

___
### Intro
[[#Table of contents|Back to the top]]

Malware Information Sharing Platform
Collection, storage, distribution of threat intelligence, IOCs related to malware, cyber attacks, financial fraud
Can be fed to NIDS (Network Intrusion Detection System), log analysis tools, SIEM

Functionalities
- **IOC database**
- **Automatic Correlation:** Correlations between malware attributes, indicators, attack campaigns, analysis
- **Data Sharing**
- **Import & Export Features:** integrate other systems (NIDS, HIDS, OpenIOC, ...)
- **Event Graph**
- **API support**

Use cases
- **Malware Reverse Engineering**: Sharing of malware indicators to understand how different malware families function
- **Security Investigations:** Searching, validating, using indicators in investigating security breaches
- **Intelligence Analysis:** Gathering info about adversary groups, capabilities
- **Law Enforcement:** Forensic investigations
- **Risk Analysis:** Researching new threats, their likelihood, occurrences
- **Fraud Analysis:** Financial indicators to detect financial fraud

___
### Event Actions
[[#Table of contents|Back to the top]]
#### Event Creation

Storage of general info about incident
Description, time, risk level
Distribution channels
- Your organisation only
- This Community-only: your org, orgs on this MISP server, orgs running MISP servers that synchronise with this server
- Connected communities: same as above + hosting organisations of servers that are two hops away from yours
- All communities

#### Attributes & Attachments

- **Intrusion Detection System:** attribute used as IDS signature when exporting NIDS data
- **Batch import:** several attributes of same type (e.g. list of IP addresses), join them all into same value field, separated by line breaks

Attachments: malware (check malware checkbox $\rightarrow$ zipped and passworded $\rightarrow$ prevent from accidental download and exe), report files from external analysis, artefacts dropped by malware

#### Publish Event

Org Admin review $\rightarrow$ publish to distribution channel selected during Event Creation

___
### Feeds & Taxonomies
[[#Table of contents|Back to the top]]

#### Feeds

Enabled by Site admin

- Exchange threat information
- Preview events along with associated attributes and objects
- Select, import events to your instance
- Correlate attributes identified between events and feeds

#### Taxonomies

Categorize based on tags

Use cases
- Set events for further processing by external tools (e.g. VirusTotal)
- Ensure events are classified appropriately before Org Admin publishes
- Enrich IDS export values with tags that fit specific deployments

Machine tags
- **Namespace:** property to be used
- **Predicate:** property attached to the data
- **Value:** numerical/text details to map the property

#### Tagging

Event LVL vs Attribute LVL: Set tags to entire events, set tags to attributes only when they are an exception

Minimal subset of tags
- **[Traffic Light Protocol:](https://www.first.org/tlp/)** color schema guides intelligence sharing
- **Confidence**
- **Origin:** source of information -- automated/manual investigation
- **Permissible Actions Protocol:** how the data can be used to search for compromises within org