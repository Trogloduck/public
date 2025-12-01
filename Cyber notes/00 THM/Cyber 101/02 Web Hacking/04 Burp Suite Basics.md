### Table of contents
- [[#Intro]]
- [[#Burp Community]]
- [[#Dashboard]]
- [[#Intro to Proxy]]
- [[#Connecting through Proxy]]
- [[#Site Map and Issue Definitions]]
- [[#Burp Browser]]
- [[#Scoping]]
- [[#Proxying HTTPS]]

___
### Intro
[[#Table of contents|Back to the top]]

Java-based framework, solution for comprehensive pentesting, web and mobile apps, APIs

Captures, enables manipulation of HTTP(S) traffic between browser and server

___
### Burp Community
[[#Table of contents|Back to the top]]

- **Proxy**: interception, modification of requests and responses while interacting with web applications
- **[Repeater](https://tryhackme.com/room/burpsuiterepeater)**: capturing, modifying, resending same request multiple times --> crafting payloads through trial and error (e.g. SQL Injection) / testing functionality of endpoint for vulnerabilities
- **[Intruder](https://tryhackme.com/room/burpsuiteintruder)**: spraying endpoints with requests (e.g. brute-force or fuzzing)
- **[Decoder](https://tryhackme.com/room/burpsuiteom)**: decode captured information or encode payloads before sending them
- **[Comparer](https://tryhackme.com/room/burpsuiteom)**: comparison of two pieces of data at either word or byte level
- **[Sequencer](https://tryhackme.com/room/burpsuiteom)**: assessing randomness of tokens, such as session cookie values or other supposedly randomly generated data. If the algorithm used for generating these values lacks secure randomness, it can expose avenues for devastating attacks.


___
### Dashboard
[[#Table of contents|Back to the top]]

Divided into 4 quadrants:

![[Pasted image 20251121162446.png]]

1. **Tasks**: define background tasks Burp Suite will perform while you use the application
2. **Event log**: actions performed by Burp Suite
3. **Issue Activity**: specific to Burp Suite Professional, displays vulnerabilities identified by automated scanner, ranked by severity and filterable based on certainty of vulnerability
4. **Advisory**: more detailed information about identified vulnerabilities

___
### Intro to Proxy
[[#Table of contents|Back to the top]]

Intercepted traffic can be manipulated, sent to other tools, or explicitly allowed to continue to its destination

- **Intercepting Requests:** requests made through Burp Proxy are intercepted and held back from reaching target server. They appear in Proxy tab --> forwarding, dropping, editing, sending to other Burp modules.
- **Capture and Logging:** helpful for later analysis and review of prior requests
- **WebSocket Support:** Burp Suite captures and logs WebSocket communication
- **Logs and History:** captured requests can be viewed in **HTTP history** and **WebSockets history** sub-tabs

- (Server) **Response Interception:** deactivated by default, explicitly request
- **Match and Replace:** in **Proxy settings**, use of regex to modify incoming and outgoing requests --> dynamic changes (e.g. modifying user agent or manipulating cookies)

___
### Connecting through Proxy
[[#Table of contents|Back to the top]]

**FoxyProxy**: Burp extension for Firefox
--> Configure browser to redirect traffic through Burp

Create Burp Proxy Configuration:
- Title: `Burp` (or any preferred name)
- Proxy IP: `127.0.0.1`
- Port: `8080`

___
### Site Map and Issue Definitions
[[#Table of contents|Back to the top]]

Target tab

1. **Site map**: map out web applications in a tree structure, automatically generate site map by simply browsing web application, accumulate data during initial enumeration steps
2. **Issue definitions**: list of all vulnerabilities scanner looks for
3. **Scope settings**: include or exclude specific domains/IPs to define scope of our testing, focus on web applications we are specifically targeting and avoid capturing unnecessary traffic

___
### Burp Browser
[[#Table of contents|Back to the top]]

Built-in Chromium browser

On Linux, use Burp with a lower privileged account (not root), for security

___
### Scoping
[[#Table of contents|Back to the top]]

Target tab > right-click target from list on left and "Add To Scope" > Yes

Check scope: Target tab > Scope settings sub-tab

Proxy still intercepts everything (even out of scope) --> Proxy settings sub-tabs > Request and Response interception rules > tick `And URL Is in target scope`

___
### Proxying HTTPS
[[#Table of contents|Back to the top]]

TLS enabled --> might run into error PortSwigger Certificate Authority (CA) is not authorized to secure the connection

--> Manually add PortSwigger CA certificate to browser's list of trusted certificate authorities
1. **Download CA Certificate:** Burp Proxy activated, go to `http://burp/cert` > will download `cacert.der` file
2. **Access and update Firefox Certificate Settings:**
	1. Type `about:preferences` into your Firefox URL bar
	2. Search for "certificates" and click **View Certificates** button
	3. **Import CA Certificate:** Certificate Manager window, click on **Import**, import `cacert.der`
	4. **Set Trust for CA Certificate:** check "Trust this CA to identify websites"

![[portswigger ca certificate.gif]]


Tip: use CTRL + U to make script URL safe in HTTP request