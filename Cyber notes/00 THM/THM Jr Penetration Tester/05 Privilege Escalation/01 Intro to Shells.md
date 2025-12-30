https://tryhackme.com/room/introtoshells

### Table of contents
- [[#Tools]]
- [[#Shell Types]]
- [[#Netcat]]
- [[#Netcat Shell Stabilization]]

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
