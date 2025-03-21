1. Hash Values
MD5 is not secure, vulnerable to hash collision
Hash lookup: [VirusTotal](https://www.virustotal.com/gui/), [Metadefender Cloud - OPSWAT](https://metadefender.opswat.com/?lang=en)
```powershell
Get-FileHash PATH/TO/FILE -Algorithm MD5
```
```Shell
md5sum PATH/TO/FILE
```

2. IP Address

3. Domain Names
/!\ typosquatting and punycode
Tools to shorten malicious URL
	- bit.ly
	- goo.gl
	- ow.ly
	- s.id
	- smarturl.it
	- tiny.pl
	- tinyurl.com
	- x.co
$\rightarrow$ use unshortener webapp to uncover original domain

5. Host Artifacts

6. Network Artifacts

7. Tools
**app.any.run**: sandbox environment, detonate object and observe its activity, investigate links

7. TTPs
