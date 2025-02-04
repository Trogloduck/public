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

#### Show databases
```python
mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
```

