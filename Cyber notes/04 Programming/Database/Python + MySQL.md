#### Common script - Connection
```python
import mysql.connector
from my_packages.creds import user, pw

mydb = mysql.connector.connect(
  host="localhost",
  user=user(),
  password=pw()
)
```
*Common part to all subsequent scripts, connects to MySQL database using credentials*, `print(mydb)` to check if connection succeeded

*In order to avoid displaying credentials in script, save credentials in other script that can be encrypted*

##### Show databases
```python
mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
```

##### Create/drop database
```python
mycursor.execute("CREATE DATABASE my_database)
mycursor.execute("DROP DATABASE my_database)
```

##### Connect to database
```python
import mysql.connector
from my_packages.creds import user, pw

mydb = mysql.connector.connect(
  host="localhost",
  user=user(),
  password=pw(),
  database="my_database"
)
```

##### Create table
```python
mycursor.execute("CREATE TABLE my_table (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")
```

##### Insert rows
```python
sql = "INSERT INTO my_table (id, name) VALUES (%s, %s)"
val = (1, "Jeremy Bower")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
```
Multiple rows
```python
val = [
  (2, 'George'),
  (3, 'Michael'),
  …
]
```
Return last record id
```python
mycursor.lastrowid
```
