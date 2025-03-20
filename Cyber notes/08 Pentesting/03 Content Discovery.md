### Table of contents
- [[#Manual]]
	- [[#`robots.txt`]]
	- [[#Favicon]]
	- [[#`sitemap.xml`]]
	- [[#HTTP Headers]]
	- [[#Framework Stack]]
- [[#OSINT]]
	- [[#Google hacking/dorking]]
	- [[#Wappalyzer]]
	- [[#Wayback Machine]]
	- [[#GitHub]]
	- [[#S3 Buckets]]
- [[#Automated]]

___

**Content**: file, video, picture, backup, feature, ...

**Content discovery**: beyond obvious visible content, try to find things **not intended for public**
*Example*: staff pages/portals, older versions of website, backup files, config files, admin panels, ...

3 ways of discovery: Manually, Automated, OSINT (Open-Source Intelligence)

___
### Manual

#### `robots.txt`
[[#Table of contents|Back to the top]]

*File that tells search engines which pages they are allowed/forbidden to show*

Sometimes, can be accessed just by adding **`/robots.txt`** to domain's URL

#### Favicon
[[#Table of contents|Back to the top]]

*Icon to brand website*

![[Pasted image 20250320094041.png|500]]

If framework is used and default favicon isn't modified, it can give a clue about the framework used
$\rightarrow$ check against this database: [OWASP favicon database](https://wiki.owasp.org/index.php/OWASP_favicon_database)

1. `CTRL + F "favicon"` in source page: look for favicon URL (href)
2. `curl favicon_URL | md5sum`: get favicon MD5 hash
3. `CTRL + F md5_hash` on OWASP favicon database

#### `sitemap.xml`
[[#Table of contents|Back to the top]]

List of every file publicly listed
`main-domain/sitemap.xml`

#### HTTP Headers
[[#Table of contents|Back to the top]]

`curl target_URL -v`: headers show software running on server (version), scripting languages, ... (-v shows the headers)

#### Framework Stack
[[#Table of contents|Back to the top]]

1. Discover framework through favicon, HTML comment, copyright notices /credits
2. Locate, go to framework's website
3. Read documentation, change logs

___
### OSINT
#### Google hacking/dorking
[[#Table of contents|Back to the top]]

Use filters to target specific website

Example filters

| **Filter**  | **Description**                             |
| ----------- | ------------------------------------------- |
| `site:`     | results only from specified website address |
| `inurl:`    | results with specified word in URL          |
| `filetype:` | results with particular file extension      |
| `intitle:`  | results contain specified word in title     |

More filters: https://github.com/chr3st5an/Google-Dorking

#### Wappalyzer
[[#Table of contents|Back to the top]]

Online tool, browser extension, identify technologies used on website 
$\rightarrow$ framework, CMS (Content Management Systems), payment processors, ...

#### Wayback Machine
[[#Table of contents|Back to the top]]

https://archive.org/web/
May help uncover old pages still active on current website

#### GitHub
[[#Table of contents|Back to the top]]

Search for target name on GitHub $\rightarrow$ source code or even passwords

#### S3 Buckets
[[#Table of contents|Back to the top]]

Storage service by Amazon, save files / static website content in cloud, HTTP/S
Owner sets access permissions: public, private, writable; sometimes incorrectly set

`http(s)://{name}.s3.amazonaws.com`

Finding S3 bucket
- Page source
- GitHub repo
- Automated search: use company name followed by common terms -- {name}-assets, {name}-www, {name}-public, {name}-private, etc.

---
### Automated
[[#Table of contents|Back to the top]]

Automated requests checking if file/directory exists

Wordlists: .txt list containing commonly used words

[Worldlists database](https://github.com/danielmiessler/SecLists)

1. Download worldlist
2. Feed wordlist path into automated tool

**`fuff`**
```Shell
ffuf -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt -u http://10.10.124.235/FUZZ
```

**`dirb`**
```Shell
dirb http://10.10.124.235/ /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt
```

**`gobuster`**
```Shell
gobuster dir --url http://10.10.124.235/ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt
```