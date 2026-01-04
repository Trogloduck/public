https://tryhackme.com/room/linprivesc

### Table of contents
- [[#y tho]]
- [[#Enumeration]] --> [[#`ps` -- Processes|`ps`]], [[#`find`|`find`]]
- [[#Automated Enumeration]]
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
### 
[[#Table of contents|Back to the top]]



___
### 
[[#Table of contents|Back to the top]]



___
