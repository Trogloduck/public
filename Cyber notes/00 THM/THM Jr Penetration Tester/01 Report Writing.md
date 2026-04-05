https://tryhackme.com/room/writingpentestreports

### Table of contents
- [[#Structure]]
- [[#1. Summary]]
- [[#2. Vulnerability Write-Ups]]
- [[#3. Appendices]]
- [[#Style]]

___
### Structure
[[#Table of contents|Back to the top]]

Audiences (stakeholders)
- **Technical:** understand root cause of vulnerabilities, remediation (devs, IT support team, ...), **70-90%** of 1 report aimed at them
- **Security:** higher-level executive, coordinates, prioritizes, **10-20%** of report
- **Business:** help those dumdums understand **business impact**, **5-10%** of report, abstracted from technical

##### Sections

| Section                     | Target Audience     | Description                                                                                                                                                                                                                                                                   |
| --------------------------- | ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Summary**                 | Business & Security | High-level view, explains what was tested, found, why it matters, remediation, in business terms                                                                                                                                                                              |
| **Vulnerability Write-Ups** | Technical           | Write-ups (details on vulnerability, replication methods, remediation) for each issue                                                                                                                                                                                         |
| **Appendices**              | Security            | Supporting details that don’t fit in main report (detailed testing scope, methodology, artefacts), usually used by security stakeholders to understand coverage that was achieved during engagement and next steps that would be required once remediation has been performed |

___
### 1. Summary
[[#Table of contents|Back to the top]]

*What was tested, found, why it matters, remediation*

Should be written **last**

Sometimes required to break down summary in 2 parts
- **Executive Summary:** for business stakeholders, avoid technical jargon, focus on business risk, security posture, impact
- **Findings & Recommendations:** for security team, common vulnerability themes, attack chains, risk ratings, draw links between issues

##### Structure
- **Overview:** what was tested, type of system/app, goals of assessment, scope, coverage achieved
- **Results:** issues found
- **Impact:** if issues is unaddressed, how system can be exploited
- **Remediation Direction:** high level, actions that should be taken, budget, low hanging fruits

___
### 2. Vulnerability Write-Ups
[[#Table of contents|Back to the top]]

*Vulnerability name and description, where and how it was found, remediation*

##### Structure
- **Title:** short, descriptive (e.g. "*Unauthenticated SQL Injection in Login Form*")
- **Risk Rating:** rating in isolation, client risk rating matrix / public one (CVSS)
- **Summary:** vulnerability explanation, potential impact
- **Background:** more detailed explanation of vulnerability, why it matters, helps non security understand root cause and stakes
- **Technical Details & Evidence:** where and how it was found; evidence -- requests, responses, payloads, screenshots, code snippets, ...
- **Impact:** what attacker could achieve
- **Remediation Advice:** actionable steps, address root cause (e.g. SQLi --> 1° parameterisation, then sanitization and validation), if include further defence-in-depth controls say they can't be implemented in isolation (without 1°)
- **References** (optional)**:** links to relevant vendors / guidance to support fix

##### Context - Details to include
- **Where** vulnerability was found: endpoint, parameter, feature, ...
- What **assumptions** is required for vulnerability to be exploited: credentials, admin access, timeframe, ...
- **Impact:** same vulnerability doesn't affect different clients the same way
- **Remediation:** different clients address same vulnerability in different ways depending on their means and priorities

___
### 3. Appendices
[[#Table of contents|Back to the top]]

*Audit trail: shows work, backs up findings, allows for informed follow-up*

Audience: security stakeholders, future testers

**Assessment Scope**
How close assessment was to what was originally scoped in ROE (Rule of Engagement)
Helps security stakeholders understand next steps: what is left to be tested

**Assessment Artefacts**
List any changes that might have been made during testing
Try to cleanup as much as possible but some artefacts will be left, prevent false positives
Provide recommendations on if artefacts need to be removed and how they should be

___
### Style
[[#Table of contents|Back to the top]]

**Write clearly**
Avoid ambiguity, use simple, direct language, make point obvious
Should avoid over complicated vocabulary

**Write professionally**
- Objectivity: stick to facts, no exaggeration, no emotional language, no assumptions about intent
- Consistency: terminology, formatting, structure

**Best Practices**
- Write in past **passive** form (e.g. "A vulnerability was discovered" instead of "We discovered a vulnerability")
- Mask sensitive info
- Avoid contractions and casual language
- QA -- Quality Assurance: reread and have a peer read report