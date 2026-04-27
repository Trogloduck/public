https://tryhackme.com/room/attacktivedirectory

### Table of contents
- [[#1. Setup]]
- 

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
### Enumeration
[[#Table of contents|Back to the top]]

`nmap 10.128.168.222`
`enum4linux-ng -A 10.128.168.222 -oA results.txt`





___
### 
[[#Table of contents|Back to the top]]



___
### 
[[#Table of contents|Back to the top]]



___
### 
[[#Table of contents|Back to the top]]



___
### 
[[#Table of contents|Back to the top]]



___
### 
[[#Table of contents|Back to the top]]



___
