### Table of contents
- [[#URL]]
- [[#HTTP Messages]]
	- [[#HTTP Request]]
		- [[#Request Line]]
		- [[#Request Headers]]
		- [[#Request Body]]
	- [[#HTTP Response]]
		- [[#Status Line]]
		- [[#Headers]]

___
### URL
[[#Table of contents|Back to the top]]

**URL** - Uniform Resource Locator: guides browser to right place on internet

![[Pasted image 20251112091332.png]]
- **Scheme**: protocol used to access website
- **User**: rare because unsafe
- **Host/Domain**: most important part of URL, the website itself
- **Port**: right service on web server (HTTP: 80, HTTPS: 443)
- **Path** to specific file on server
- **Query String** starts with "`?`", often used for search terms and form inputs, often exploited for **injections**
- **Fragment** starts with "`#`", points to specific section of page, can also be exploited for **injections**

___
### HTTP Messages
[[#Table of contents|Back to the top]]

*Very important for understanding how a webapp works: shows how user's requests and server's responses are communicated*

![[Pasted image 20251112092446.png]]

- **Start Line**: kind of message, request from user / response from server, how message should be handled
- **Headers**: key-value pairs
- **Empty Line**: separates header from body
- **Body**: actual data user wants to send (e.g. form data) / server responds with (e.g. webpage)

![[Pasted image 20251112093149.png]]

#### HTTP Request
##### Request Line
[[#Table of contents|Back to the top]]

AKA Start Line: kind of request
`HTTP method, URL path, HTTP version`

- **HTTP Methods**: action user wants to perform on resource identified by URL path
	- **`GET`**: **fetch data** from server without making any changes --> only send data user is allowed to see
	- **`POST`**: **send data** to server --> sanitize against injections
	- **`PUT`**: **replace/update** something on server --> verify user authorization
	- **`DELETE`**: **removes** something from server --> verify user authorization
	- **`PATCH`**: **update** part of a resource
	- **`HEAD`**: like `GET` but only for headers
	- **`OPTIONS`**: inform on what methods are available for specific resource
	- **`TRACE`**: like `OPTIONS`, which methods are allowed
	- **`CONNECT`**: create secure connection like HTTPS, encrypted communication
	- ...

- **URL Path**: tells server where to find wanted resource --> can be manipulated by attackers in order to access resources
	- Validate URL path
	- Sanitize path against injections
	- Privacy and risk assessments to protect sensitive data

- **HTTP Version**: HTTP/2 and /3 are faster and more secure but **HTTP/1.1** is still very common

##### Request Headers
[[#Table of contents|Back to the top]]

Common Request Headers

| **Request Header** | **Example**                                                                      | **Description**                                                                          |
| ------------------ | -------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Host               | `Host: tryhackme.com`                                                            | Specifies the name of the web server the request is for.                                 |
| User-Agent         | `User-Agent: Mozilla/5.0`                                                        | Shares information about the web browser the request is coming from.                     |
| Referer            | `Referer: https://www.google.com/`                                               | Indicates the URL from which the request came from.                                      |
| Cookie             | `Cookie: user_type=student; room=introtowebapplication; room_status=in_progress` | Information the web server previously asked the web browser to store is held in cookies. |
| Content-Type       | `Content-Type: application/json`                                                 | Describes what type or format of data is in the request.                                 |

##### Request Body
[[#Table of contents|Back to the top]]

`POST`/`PUT` --> data is sent to web server --> data is request body
Common formats (`Content-Type`): `URL Encoded` (default), `Form Data`, `JSON`, `XML`

- **`application/x-www-form-urlencoded`** - *URL Encoded*: `key1=value1&key2=value2`, special characters %encoded%

- **`multipart/form-data`** - *Form Data*: data blocks separated by boundary (defined header of request itself), used to send binary data (files, images) for instance
  Example
```HTTP REQUEST
POST /upload HTTP/1.1
Host: tryhackme.com
User-Agent: Mozilla/5.0
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW

----WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="username"

aleksandra
----WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="profile_pic"; filename="aleksandra.jpg"
Content-Type: image/jpeg

[Binary Data Here representing the image]
----WebKitFormBoundary7MA4YWxkTrZu0gW--
```

- **`application/json`** - *JSON - JavaScript Object Notation*: 
```JSON
{
    "name": "Aleksandra",
    "age": 27,
    "country": "US"
}
```

- **`application/xml`** - *XML*: 
```XML
<user>
    <name>Aleksandra</name>
    <age>27</age>
    <country>US</country>
</user>
```

#### HTTP Response
##### Status Line
[[#Table of contents|Back to the top]]

1. **HTTP Version**
2. **Status Code**: three-digit number showing outcome of request
3. **Reason Phrase**: short message explaining status code in human-readable terms

Status Codes and Reason Phrases

- **100-199** - ***Informational***
Server has received part of the request and is waiting for the rest, "keep going" signal

- **200-299** - ***Successful***
Everything worked as expected: server processed request and sent back requested data

- **300-399** - ***Redirection***
Requested resource has moved to different location, usually provides new URL

- **400-499** - ***Client Error***
Problem with request (wrong URL, missing authentication, ...)

- **500-599** - ***Server Error***
Server encountered error while trying to fulfil request

Common Status Codes
- **100** - Continue: server got first part of request, ready for rest
- **200** - OK: request successful, server sending back requested resource
- **301** - Moved Permanently: resource permanently moved to new URL
- **404** - Not Found: server couldn't find requested resource
- **500** - Internal Server Error: something went wrong server-side

##### Headers

Key-value pairs, info about response and how to handle it

Required response headers
- **`Date`**: when response was generated by server
- **`Content-Type`**: kind of content (HTML, JSON, ...) and character set (UTF-8, ...)
- **`Server`** (nginx, ...)

Common headers
- **`Set-Cookie`**: sends cookies from server to client, client stores and sends back with future requests. Cookies should have `HttpOnly` (can't be accessed by JavaScript) and `Secure`(only HTTPS) flags
- **`Cache-Control`**: how long client can cache response before checking with server again, can prevent sensitive info from being cached (`no-cache`)
- **`Location`**: used in redirection responses, can be exploited by attackers to redirect to malicious websites (*open redirect vulnerabilities*)

___
### Security Headers

https://securityheaders.com/: analyze security headers

##### CSP - Content-Security-Policy
[[#Table of contents|Back to the top]]


##### HSTS - Strict-Transport-Security
[[#Table of contents|Back to the top]]


##### X-Content-Type-Options
[[#Table of contents|Back to the top]]


##### Referrer-Policy
[[#Table of contents|Back to the top]]



___
### 
[[#Table of contents|Back to the top]]


