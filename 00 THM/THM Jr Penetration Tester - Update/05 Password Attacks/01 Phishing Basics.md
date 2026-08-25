https://tryhackme.com/room/phishingbasics

### Table of contents
- [[#Intro]]
- [[#Psychology]]
- [[#Techniques]]
- [[#Phishing Campaign]]
- [[#Practical]]

___
### Intro
[[#Table of contents|Back to the top]]

- **Phishing:** wide net
- **Spear Phishing:** targeted tailored attack
- **Whaling:** spear phishing aimed at heavy target (CEA, CFO, ...)

___
### Psychology
[[#Table of contents|Back to the top]]

![[Pasted image 20260825104536.png]]

- **Scarcity:** leverage FOMO and loss aversion
- **Urgency:** speed over scrutiny, prevent victim form checking (threaten with inconvenient consequences (lockouts, delays, ...))
- **Authority:** fake status/expertise to gain compliance
	- Titles, signature, formal tone, role label (HR, IT, Finance, ...)
- **Fear:** threat and alarm, trigger protective reaction, "fix" problem, make risk personal (account compromise, legal trouble, ...)
	- Wording: "security alert", "breach", or "unauthorised access"
- **Curiosity:** promise interesting information, subject line short, intriguing, vague (use words like "confidential", "exclusive", ...)
- **Trust:** familiar brands, colleagues, communication styles, feel safe --> recognisable names, logos, routines (monthly report, ticket number, ...)

Cognitive biases
- **Overconfidence bias*:** think to be too smart to fall for phishing
- **Confirmation \*:** info fit expectation
- **Authority \*:** trust info from authority figure

___
### Techniques
[[#Table of contents|Back to the top]]

##### URL & Domain Manipulation
- **URL Masking:** `[https://legitimate.com](http://attacker.com)`
- **Homograph Attack:** `go0gle.com`
- **Typosquatting:** `faecbook.com`
- **URL Shortening:** `https://tinyurl.com/fwtvrnk8`

##### Email Spoofing

SMTP doesn't have built-in authentication for email addresses --> if domain lacks security measures, Python script can modify email address of sender

**Mitigation:**  **SPF** (Sender Policy Framework), **DMARC** (Domain-based Message Authentication, Reporting, and Conformance), and **DKIM** (DomainKeys Identified Mail)

##### Credential Harvesting
Legitimate website clone
1. **Logs** credentials into attacker file/database
2. **Redirects** victim to legitimate website to prevent suspicion (victim perceives failed login attempt)

##### VBA Macros
(Visual Basic for Applications)
1. Victim receives and opens `.docm`
2. Victim clicks "Enable Content" upon being prompted by MS Word to enable macros
3. VBA macro executes hidden command
4. Attacker receives confirmation of execution

##### Tools
- **[GoPhish](https://github.com/gophish/gophish):** store SMTP server setting for sending emails, web-based tool for creating email templates with WYSIWYG (What You See Is What You Get) editor, schedule emails, analytics dashboard (clicks, opening)
- **[EvilNginx](https://github.com/kgretzky/evilginx2):** bypass MFA, reverse proxy between victim and legitimate site, captures credentials and session tokens
- **[SET -- The Social Engineering Toolkit](https://github.com/trustedsec/social-engineer-toolkit):** multitool, spear-phishing, common websites fake versions, ... 

___
### Phishing Campaign
[[#Table of contents|Back to the top]]

![[Pasted image 20260825113924.png]]

1. **Planning & Scoping:** agreement with client
	- User groups to be targeted, techniques, bounds, message volume
	- Measured outcomes ("clicked a link", "attempted to submit credentials", ...)
	- Timing, legal sign-off, ***ROE*** (Rules Of Engagement) ...
	  
2. **Reconnaissance:** public info --> company websites, press releases, LinkedIn profiles, public social posts
   ***Document sources*** to prove research stayed ethical and limited to OSINT
   
3. **Scenario & Payload Development:** turn intel into realistic but harmless payload (no malware, no credential capture)
   
4. **Exploitation & Post-Exploitation:** run campaign, monitor metrics, stay vigilant to follow ROE
   
5. **Reporting & Debriefing:** analyse what happened and why, no naming, focus on practical improvements

Recommendations Table

| Metric                     | What it measures                           | Benchmark                                                   | Suggested Recommendation(s)                                 |
| -------------------------- | ------------------------------------------ | ----------------------------------------------------------- | ----------------------------------------------------------- |
| Open Rate                  | % of users who opened email                | ~50–65%                                                     | Targeted refresher training                                 |
| Click Rate                 | % of all users who clicked link            | - 8–14%: acceptable<br>- >14%: high risk                    | Focused security awareness training                         |
| Credential Entry Rate      | % of all users who entered credentials     | - <2%: low risk<br>- 2–5%: moderate risk<br>- >5% high risk | Phishing site identification training, MFA implementation   |
| Attachment Detonation Rate | % of users who opened/executed attachment. | \>5–7% suggests risk                                        | Educate on safe handling of attachments, Sandbox detonation |
| Reporting Rate (24h)       | % of users who reported email within 24h   | - >40% strong<br>- 30–40% average<br>- <30% low             | Reporting awareness campaign                                |

___
### Practical
[[#Table of contents|Back to the top]]

##### Scenario
- Spear-phishing targeted at Bob, head of finance at TryAccounting
- Email: `bob@tryaccounting.thm`
- Strict password policy
- Email security
- Goal: gain Bob's credentials

Set up Credential Harvesting Website
1. SSH into VM: `ssh attacker@10.130.135.109`; password: `attacker1234`
2. Launch SET: `SET`
3. Select Social-Engineering Attacks: `1`
4. Website Attack Vectors: `2`
5. Credential Harvester: `3`
6. Custom Import: `3`, IP - `10.130.135.109`, path - `/home/attacker/setoolkit/`, choose 1 "Copy just the index.html", URL - `http://tryacounting.thm` (typosquatting)
7. View result: `http://10.130.135.109`

Phish
1. Log into Rainloop client `http://10.130.135.109:8080` - `attacker@phisher.thm:attacker1234`
2. Attempt to email Bob --> email security response: "DELIVERY FAILURE NOTIFICATION"
   --> need to spoof email
3. "New Message", click on attacker email and select `support@tryaccounting.thm`
4. Email subject: "Action Required: Password Expiration Notice"
```
Dear Bob, 

As part of our security policy, we require all TryAccounting employees to change their passwords every 3 months. Please log in to our internal portal and update your password before Friday: http://tryacounting.thm

Thank you, 

TryAccounting Support Team
```

If target enters credentials, they will be displayed in shell executing SET