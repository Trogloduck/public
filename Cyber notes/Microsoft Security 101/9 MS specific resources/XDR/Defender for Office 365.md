Protects against phishing, malware arriving by email links, attachments, collaboration tools (SharePoint, Teams, Outlook)

Accessed through Defender portal (Email & collaboration node)

Real-time views of threats, investigation, hunting, remediation

#### Prevent and detect

- **Policies** for anti-malware, anti-spam, and anti-phishing
- Outbound **spam** filtering
- **Connection filtering**: identify good/bad source email servers by IP addresses
- **Quarantine policies**
- Submit messages, URLs, attachments to **MS** for **analysis**
- **Safe attachments**: additional protection layer against malware. Files are scanned by MS 365 virus detection engine, Safe Attachments opens files in virtual environment ("**detonation**")
- Email and collaboration **alerts**
- **Attack simulation training**: admins run realistic attack scenarios, identify and train vulnerable users before real attack occurs
- **[[Definitions#SIEM|SIEM]]** integration
#### Investigate

- **Audit log search** by admins, insider risk teams, compliance and legal investigators
- **Message trace**: follows email messages (message received/rejected/deferred/delivered)
- **Reports**: how email security features are protecting org
- **Explorer** (AKA Threat Explorer) or Real-time detections: near real-time tools, SecOps investigate, respond to threats
- **SIEM** integration for **alerts**
- **URL trace**: investigate domain to see if malicious or not
- **Threat trackers**: created and saved queries to automate threat discovery
- **Campaigns**: identifies and categorizes coordinated phishing and malware email attacks
#### Respond

- **ZAP** (Zero-hour Auto Purge): retroactively detects and neutralizes malicious phishing, spam, malware messages already delivered to Exchange Online mailboxes
- **AIR**: Automated Investigation and Response
- **SIEM** integration for automated **responses**

