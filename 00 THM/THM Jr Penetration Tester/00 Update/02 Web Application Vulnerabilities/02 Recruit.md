Attackbox
`10.130.127.112`

Target
`10.130.141.208`
`http://10.130.141.208`

`/file.php?cv=...`

nmap -sV
**Apache httpd 2.4.41**

`gobuster dir -u http://10.130.141.208:80 -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt -x bak,txt,html,php -t 20`
- 200
	- index.php
	- sitemap.xml
	- api.php
	- config.php
	- file.php
- 301
	- mail --> mail.log
	- phpmyadmin --> credentials required
	- javascript
	- assets
	- dashboard.php
	- logout.php
- 403 (forbidden)
	- .htpasswd
	- .htpasswd.txt
	- .htpasswd.bak
	- ...


`gobuster dir -u http://10.130.141.208:80 -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt -t 20`

Finding in /mail
mail.log
HR credential (username: hr) in `config.php`
Admin credentials in backend database