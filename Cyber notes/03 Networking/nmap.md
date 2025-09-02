*Discover live hosts, find open ports, detect service versions*

### Table of contents

- [[#Host Discovery]]
- [[#Port Scanning]]: [[#TCP]], [[#UDP]], [[#Version detection]], [[#Forcing scan]]
- [[#Speed]]

### Host Discovery
[[#Table of contents|Back to the top]]
*Who is online?*

Specify targets:
- **Range**: `192.168.0.1-10`
- **Subnet**: `192.168.0.1/24` equivalent to `192.168.0.0-255`
- **Hostname**: `example.thm`

`-sn`: discover online hosts on network

If my IP is `192.168.66.89`, I can use `nmap -sn 192.168.66.0/24` to scan my **local network**

`-sL`: **confirms** list of targets, doesn't actually scan, good to use when you don't know subnets by heart

### Port Scanning
[[#Table of contents|Back to the top]]
*Who is listening: any network service that is listening for incoming connections*

All ports are either **[[TCP]]** or **[[UDP]]**. Typically webserver will run on TCP ports 80 or 443, DNS server on TCP (and UDP) 53

#### TCP
##### telnet
`-sT`: "connect scan" -- attempt a **3-way handshake** (SYN, SYN-ACK, ACK) with every target port, very similar to classic nmap scan
	$\rightarrow$ if successful connection, nmap tears down connection with RST-ACK packet

If port closed, target will respond with RST-ACK directly
##### SYN scan
*more stealthy way*

`-sS`: only sends the SYN packet, not the ACK, then RST

#### UDP
`-sU`: nmap directly sends UDP packets as no connection is required in UDP and informs you whether destination is reachable or not

#### Limiting target ports

nmap scans 1000 most common ports by default

`-F` (fast): 100 most common
`-p[range]`: 
	`-p10-1024`
	`-p-25`: up to 25
	`-p-`: all ports

#### Version detection

`-O`: OS detection
`-sV`: version detection of services running on open ports
`-A` = `-O` & `-sV`

#### Forcing scan

`-Pn`: some hosts may appear to be down when running `-sS` so nmap won't launch port scan on them, this option forces the port scan

### Speed
[[#Table of contents|Back to the top]]

Running scan at normal speed might trigger **IDS** $\Rightarrow$ nmap provides 6 different speeds

| Time template | Name       | Initial scan delay (`--scan-delay`) |
| ------------- | ---------- | ----------------------------------- |
| `-T0`         | paranoid   | 5 minutes                           |
| `-T1`         | sneaky     | 15 seconds                          |
| `-T2`         | polite     | 0.4 seconds                         |
| `-T3`         | normal     | 0                                   |
| `-T4`         | aggressive | 0                                   |
| `-T5`         | insane     | 0                                   |
$\rightarrow$ `-T0` / `-T 0` / `-T paraonoid`: slowest speed
$\Rightarrow$ difference between T3 and subsequent speeds is on other parameters than initial scan delay, such as RTT (running timeout) or retries

NB:
`--min-parallelism <numprobes>` and `--max-parallelism <numprobes>` can be used to modify number of port probes active at the same time
`--min-rate <number>` and `--max-rate <number>`: rate -- packets sent /second

### Output
[[#Table of contents|Back to the top]]
*What you see*

- Show more details
- Choose file format to save data

`-v`: **verbose mode**
$\rightarrow$ increase verbosity by adding more "v"s, by pushing "v" while scan is ongoing, by specifying verbosity level (`-v3`), max level is 6

If verbose mode insufficient, **debugging mode** works the same with letter "d", max level 9

#### Saving scan report

- `-oN <filename>`: normal output
- `-oX <filename>`: XML output
- `-oG <filename>`: `grep`-able output (useful for `grep` and `awk`)
- `-oA <basename>`: output in all major formats (.gnmap, .nmap, .xml)

