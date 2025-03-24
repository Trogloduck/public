### Table of contents
- [[#1. In -- Initial Foothold]]
	- [[#1.1 Reconnaissance -- [MITRE Tactic TA0043](https //attack.mitre.org/tactics/TA0043/)|1.1 Reconnaissance]]
	- [[#1.2 Weaponization -- [MITRE Tactic TA0001](https //attack.mitre.org/tactics/TA0001/))|1.2 Weaponization]]
	- [[#1.3 Social Engineering -- [MITRE Tactic TA0001](https //attack.mitre.org/tactics/TA0001/)|1.3 Social Engineering]]
	- [[#1.4 Exploitation -- [MITRE Tactic TA0002](https //attack.mitre.org/tactics/TA0002/)|1.4 Exploitation]]
	- [[#1.5 Persistence -- [MITRE Tactic TA0003](https //attack.mitre.org/tactics/TA0003/)|1.5 Persistence]]
	- [[#1.6 Defence Evasion -- [MITRE Tactic TA0005](https //attack.mitre.org/tactics/TA0005/)|1.6 Defence Evasion]]
	- [[#1.7 Command & Control -- [MITRE Tactic TA0011](https //attack.mitre.org/tactics/TA0011/)|1.7 Command & Control]]
	- [[#1.8 Pivoting -- [MITRE Tactic TA0008](https //attack.mitre.org/tactics/TA0008/)|1.8 Pivoting]]
- [[#2. Through -- Network Propagation]]
- [[#3. Out -- Action on Objectives]]

___
UKC (2017) has the advantage of being very comprehensive compared to other frameworks

![[Pasted image 20250324114445.png]]

___
### 1. In -- Initial Foothold

#### 1.1 Reconnaissance -- [MITRE Tactic TA0043](https://attack.mitre.org/tactics/TA0043/)
[[#Table of contents|Back to the top]]

- Gather target information
- Passive/active reconnaissance

- Systems, services running on target $\rightarrow$ weaponization, exploitation 
- Contact/employees lists $\rightarrow$ impersonate/leverage in social engineering / phishing
- Potential credentials $\rightarrow$ pivoting, initial access
- Understanding network topology, other networked systems $\rightarrow$ pivoting 

#### 1.2 Weaponization -- [MITRE Tactic TA0001](https://attack.mitre.org/tactics/TA0001/))
[[#Table of contents|Back to the top]]

Setting up necessary infrastructure to perform attack
	$\rightarrow$ C2, system capable of catching reverse shells and delivering payloads to system

#### 1.3 Social Engineering -- [MITRE Tactic TA0001](https://attack.mitre.org/tactics/TA0001/)
[[#Table of contents|Back to the top]]

Manipulate employees to perform actions that will aid in the adversaries attack
- Getting user to open malicious attachment
- Impersonating web page to gather credentials
- Calling/visiting target and impersonating user in order to request password reset or be able to gain access to areas of a site the attacker would not have had access to (impersonating utility engineer)

#### 1.4 Exploitation -- [MITRE Tactic TA0002](https://attack.mitre.org/tactics/TA0002/)
[[#Table of contents|Back to the top]]

Abuse of vulnerabilities to perform code execution
- Uploading and executing a reverse shell to a web application
- Interfering with an automated script on the system to execute code
- Abusing a web application vulnerability to execute code on the system it is running on

#### 1.5 Persistence -- [MITRE Tactic TA0003](https://attack.mitre.org/tactics/TA0003/)
[[#Table of contents|Back to the top]]

Maintain access to system
- Creating service on target system that will allow attacker to regain access
- Adding target system to C2 where commands can be executed remotely at any time
- Leaving other forms of backdoors that execute when a certain action occurs on the system

#### 1.6 Defence Evasion -- [MITRE Tactic TA0005](https://attack.mitre.org/tactics/TA0005/)
[[#Table of contents|Back to the top]]

Evade defensive measures put in place in the system or network
- Web application firewalls
- Network firewalls
- Anti-virus systems
- Intrusion detection systems

>*This phase is valuable when analyzing an attack as it helps form a response and better yet - gives the defensive team information on how they can improve their defence systems in the future.*

#### 1.7 Command & Control -- [MITRE Tactic TA0011](https://attack.mitre.org/tactics/TA0011/)
[[#Table of contents|Back to the top]]

Establish communications between adversary and target system

#### 1.8 Pivoting -- [MITRE Tactic TA0008](https://attack.mitre.org/tactics/TA0008/)
[[#Table of contents|Back to the top]]

Reach other systems within a network that are not otherwise accessible

*For example, an adversary can gain access to a web server that is publicly accessible to attack other systems that are within the same network (but are not accessible via the internet)*

___
### 2. Through -- Network Propagation

___
### 3. Out -- Action on Objectives

