### Table of contents
- [[#ATT&CK]]
- [[#CAR]]
- [[#ENGAGE]]
- [[#D3FEND]]
- [[#AEP]]

___
**Basic terminology**

**APT** -- Advanced Persistent Threat: threat group or nation-state group, "Advanced" can be misleading as they are mostly using very common tools, they don't have a "superweapon" like a zero-day for every attack

**TTPs**
- **Tactics**: objectives
- **Techniques**: how objectives are reached
- **Procedures**: how techniques are implemented

___
### ATT&CK
Adversarial Tactics, Techniques, and Common Knowledge -- https://attack.mitre.org/
[[#Table of contents|Back to the top]]

APT's TTPs **wiki**: descriptions, groups, softwares, remediations, ...

ATT&CK **Navigator**: annotation of ATT&CK matrix $\rightarrow$ select techniques and frequencies $\rightarrow$ map to APT

*Example*: Navigator of the [Carbanak APT group](https://mitre-attack.github.io/attack-navigator//#layerURL=https%3A%2F%2Fattack.mitre.org%2Fgroups%2FG0008%2FG0008-enterprise-layer.json)

___
### CAR
Cyber Analytics Repository -- https://car.mitre.org/
[[#Table of contents|Back to the top]]

Collection of analytics -- **detection rules**/methods tied to ATT&CK techniques, tailored for specific softwares like Splunk

___
### ENGAGE
*Sorry, not a fancy acronym* -- https://engage.mitre.org/
[[#Table of contents|Back to the top]]

Adversary Engagement Approach
- Cyber **Denial**: prevent ability
- Cyber **Deception**: plant artifacts to mislead

Engage matrix 6 steps: 1. Prepare, 2. Expose, 3. Affect, 4. Elicit (gather information about adversary), 5. Understand

Default focus on "Operate" (Expose, Affect, Elicit)

**Tools** provides tools for each steps and substeps

___
### D3FEND
Detection, Denial, Disruption Framework Empowering Network Defense -- https://d3fend.mitre.org/
[[#Table of contents|Back to the top]]

Knowledge graph of cybersecurity countermeasures
Definition, How it works, Considerations, Example

___
### AEP
ATT&CK Emulation Plans
[[#Table of contents|Back to the top]]

[CTID](https://mitre-engenuity.org/cybersecurity/center-for-threat-informed-defense/) -- Center of Threat-Informed Defense: companies/vendors, conduct research on cyber threats and TTPs, share it to improve cyber defense (AttackIQ (founder), Verizon, Microsoft (founder), Red Canary (founder), Splunk)

[Adversary Emulation Library](https://github.com/center-for-threat-informed-defense/adversary_emulation_library) public library making AEP free, each plan mimics a specific APT

___
### CTI - Cyber Threat Intelligence

https://www.crowdstrike.com/en-us/
https://attack.mitre.org/groups/