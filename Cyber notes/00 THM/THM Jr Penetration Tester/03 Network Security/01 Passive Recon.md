https://tryhackme.com/room/passiverecon

### Table of contents
- [[#Passive vs Active]]
- [[#CLI Tools]]
- [[#Online Tools]]

___
### Passive vs Active
[[#Table of contents|Back to the top]]

- **Passive:** no direct engagement of target, publicly available info (DNS records, job ads, news articles, ...)
- **Active:** active engagement of target (connecting to company server, physical premises, social engineering)

___
### CLI Tools
[[#Table of contents|Back to the top]]

`whois domain.com`: info about registrar, DNS

**`nslookup -type=option domain.com`:** **N**ame **S**erver **Look Up**

**`dig domain.com option`:** **D**omain **I**nformation **G**roper, additional functionality, also DNS

| Option | Result             |
| ------ | ------------------ |
| A      | IPv4 Addresses     |
| AAAA   | IPv6 Addresses     |
| CNAME  | Canonical Name     |
| MX     | Mail Servers       |
| SOA    | Start of Authority |
| TXT    | TXT Records        |

___
### Online Tools
[[#Table of contents|Back to the top]]

**[DNSDumpster](https://dnsdumpster.com/):** find subdomains

**[Shodan](https://www.shodan.io/):** tries to connect to every reachable device