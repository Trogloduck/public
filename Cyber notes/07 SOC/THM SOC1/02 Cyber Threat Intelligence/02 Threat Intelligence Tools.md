### Table of contents
- [[#urlscan.io]]
- [[#abuse.ch]]
- [[#PhishTool]]
- [[#Cisco Talos Intelligence]]

___
### urlscan.io
[[#Table of contents|Back to the top]]

https://urlscan.io/

Scan results

- **Summary:** general info -- identified IP, domain registration details, page history, site screenshot
- **HTTP:** HTTP connections made by scanner to site, data fetched, file types received
- **Redirects:** HTTP/client-side redirects
- **Links:** outgoing links
- **Behavior:** variables, cookies $\rightarrow$ identify frameworks used in developing site
- **Indicators:** IPs, domains, hashes associated with site

___
### abuse.ch
[[#Table of contents|Back to the top]]

https://abuse.ch/

Identify and track malware and botnets

**MalwareBazaar**

- Samples upload: analysis, build database
- Hunting: set up alerts matching tags, signatures, YARA rules, ClamAV signatures, vendor detection

**FeodoTracker**

Intel about C2 associated with Dridex, Emotes (aka Heodo), TrickBot, QakBot and BazarLoader/BazarBackdoor, IPs and IOCs blocklists

**SSL Blacklist**

SSL certificates and JA3 fingerprints lists $\rightarrow$ deny list / threat hunting rulesets

**URLhaus**

URLs used for malware distribution, domains, hashes and filetypes

**Threatfox**

IOCs exported in MISP (Malware Information Sharing Platform) events, Suricata IDS Ruleset, Domain Host files, DNS Response Policy Zone, .json, .csv

___
### PhishTool
[[#Table of contents|Back to the top]]

https://www.phishtool.com/

- Email analysis
- Heuristic intelligence
- Classification, reporting

**Analysis Tab**

- **Headers:** source, destination email addresses, Originating IP, DNS addresses, Timestamp
- **Received Lines:** email traversal process across various SMTP servers for tracing purposes
- **X-headers:** extension headers added by recipient mailbox to provide additional information about email
- **Security:** security frameworks and policies such as Sender Policy Framework (SPF), DomainKeys Identified Mail (DKIM) and Domain-based Message Authentication, Reporting and Conformance (DMARC)
- **Attachments**
- **Message URLs:** external URLs

`md5sum email_file` > search for hash on VirusTotal or other databases

___
### Cisco Talos Intelligence
[[#Table of contents|Back to the top]]

https://talosintelligence.com/

- **Threat Intelligence & Interdiction:** threats correlation, tracking, IOCs $\rightarrow$ intel
- **Detection Research:** vulnerability and malware analysis $\rightarrow$ threat detection rules
- **Engineering & Development:** maintenance support for inspection engines and keeps them up-to-date to identify, triage emerging threats
- **Vulnerability Research & Discovery:** repeatable means of identifying and reporting security vulnerabilities
- **Communities:** image of team and open-source solutions
- **Global Outreach:** publications

`sha256sum email_file` > search for hash in Talos database