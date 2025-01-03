- [[#Protocols]]
- [[#Delivery]]
- [[#Headers]]
- [[#Types of phishing]]
- [[#Practical tips]]
- [[#Tools for/against phishing]]
___
# Protocols

3 specific protocols involved to facilitate outgoing and incoming email messages

- **SMTP** (**Simple Mail Transfer Protocol)**: utilized to handle sending of emails
- **POP3 (Post Office Protocol)**: transferring email between client and mail server
- **IMAP (Internet Message Access Protocol)**: transferring email between client and mail server

| Feature               | POP3                                            | IMAP                                                    |
| --------------------- | ----------------------------------------------- | ------------------------------------------------------- |
| **Storage**           | Downloads emails to client, removes from server | Emails stay on server, accessible from multiple devices |
| **Synchronization**   | No sync across devices                          | Full sync across all devices                            |
| **Server Management** | Limited, managed on client                      | Extensive, managed on server                            |
| **Offline Access**    | Available after download                        | Depends on sync status                                  |
| **Folders**           | No server-side folders                          | Supports server-side folders                            |
| **Resource Usage**    | Uses less server storage                        | Uses more server storage                                |
| **Connection**        | Intermittent connection possible                | Requires consistent connection                          |
| **Use Case**          | Single device use                               | Multiple device access                                  |
| **Security**          | Can be less secure                              | Generally more secure                                   |
___
# Delivery

![[Pasted image 20240909145015.png]]
1. Alexa sends email to Billy (`billy@johndoe.com`)
2. **SMTP** server needs to determine where to send Alexa's email. It queries **DNS** for information associated with `johndoe.com`
3. **DNS** server obtains information `johndoe.com` and sends it to **SMTP** server
4. **SMTP** server sends Alexa's email across Internet to Billy's mailbox at `johndoe.com`
5. Alexa's email passes through various **SMTP** servers and is finally relayed to destination **SMTP** server
6. Alexa's email finally reached destination **SMTP** server
7. Alexa's email is forwarded and is sitting in local **POP3/IMAP** server waiting for Billy
8. Billy logs into his email client, which queries the local **POP3/IMAP** server for new emails in his mailbox
9. Alexa's email is copied (**IMAP**) or downloaded (**POP3**) to Billy's email client
___
# Headers

Syntax of e-mail messages: IMF (Internet Message Format)

1. **X-Originating-IP** - The IP address of the email was sent from (this is known as an **[X-header](https://help.returnpath.com/hc/en-us/articles/220567127-What-are-X-headers-)**)
2. **Smtp.mailfrom** - The domain the email was sent from (these headers are within **Authentication-Results**)
3. **Reply-To** / Reply-Path - This is the email address a reply email will be sent to instead of the **From** email address
___
# Types of phishing

- **Spam**: unsolicited junk emails sent to large number of recipients. More malicious variant of Spam: **MalSpam**.
- **Phishing**: emails sent to target(s) purporting to be from trusted entity to lure individuals into providing sensitive information
- **Spear phishing**: takes phishing a step further by targeting specific individual(s) or organization seeking sensitive information
- **Whaling**: similar to spear phishing, but targeted specifically to C-Level high-position individuals (CEO, CFO, etc.)
- **Smishing**: takes phishing to mobile devices by targeting mobile users with specially crafted text messages
- **Vishing**: similar to smishing, but based on voice calls
___

**BEC** (Business Email Compromise): adversary gains control of internal employee's account and uses compromised email account to convince other internal employees to perform unauthorized or fraudulent actions
___
# Practical tips

- Use inspector to examine the code of legitimate page, DOM (Document Object Model), to replicate
- Falsify federated identity providing service (login with google, facebook, etc.)
	- Redirect to legitimate wrong password page

# Tools for/against phishing

Possible to investigate shortened links with online tools

Defanging a url: `domain[.]com`

[Typosquatting](https://www.csoonline.com/article/570173/what-is-typosquatting-a-simple-but-effective-attack-technique.html): `facedook.com`, `facebook.net`, `face-book.com`, `face.book.com`, `facebook-network.com`, ...

[VirusTotal](https://www.virustotal.com/gui/home/upload): analyzes files and URLs for viruses, worms, trojans and other kinds of malicious content

[PhishTools](https://www.phishtool.com/): threat intelligence, OSINT, email metadata and battle tested auto-analysis pathways into one powerful phishing response platform

[MX Lookup](https://mxtoolbox.com/)
This test will list MX records for a domain in priority order. The MX lookup is done directly against the domain's authoritative name server, so changes to MX Records should show up instantly. You can click Diagnostics , which will connect to the mail server, verify reverse DNS records, perform a simple Open Relay check and measure response time performance. You may also check each MX record (IP Address) against 105 DNS based blacklists

[PhishTank](https://phishtank.com/?)
PhishTank is a collaborative clearing house for data and information about phishing on the Internet. Also, PhishTank provides an open API for developers and researchers to integrate anti-phishing data into their applications at no charge.

[Spamhaus](https://www.spamhaus.org/): Spamhaus is the world leader in supplying realtime highly accurate threat intelligence to the Internet's major networks

[Phishing incident response](https://www.incidentresponse.org/playbooks/phishing): 7 steps defined by NIST incident response process: Prepare, Detect, Analyze, Contain, Eradicate, Recover, Post-Incident Handling