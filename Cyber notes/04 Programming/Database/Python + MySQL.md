- [[#Databases]]
	- [[#Common script - Connection]]
	- [[#Show databases]]
	- [[#Create/drop database]]
	- [[#Connect to database]]
- [[#Tables]]
	- [[#Create table]]
	- [[#`INSERT INTO`]]
	- [[#`DELETE FROM`]]
	- [[#`SELECT`]]
___
## Databases
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
___
#### Show databases
```python
mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
```

#### Create/drop database
```python
mycursor.execute("CREATE DATABASE my_database)
mycursor.execute("DROP DATABASE my_database)
```

#### Connect to database
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

___
## Tables
#### `CREATE TABLE`

```python
mycursor.execute("CREATE TABLE my_table (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")
```
*>< `DROP TABLE`*

#### `INSERT INTO`

```python
sql = "INSERT INTO my_table (id, name) VALUES (%s, %s)"
val = (1, "Jeremy Bower")
mycursor.execute(sql, val)

mydb.commit() # required to save changes after adding/deleting rows

print(mycursor.rowcount, "record inserted.")
```
**`.rowcount`** *returns number of rows affected by statement*

##### `.executemany`: multiple rows
```python
val = [
  (2, 'George'),
  (3, 'Michael'),
  …
]

mycursor.executemany(sql, val)
```

Return last record id
```python
mycursor.lastrowid
```

#### `DELETE FROM`

```python
sql = "DELETE FROM my_table WHERE name = %s"
name = ('Michael',)
```

#### `UPDATE`

```python
val = ("Billy", "Jeremy Bower")
sql = "UPDATE my_table SET name = %s WHERE name = %s%"
```

#### `SELECT`

```python
mycursor.execute("SELECT * FROM my_table")

myresult = mycursor.fetchall() # fetch all rows from last executed statement

for x in myresult:
  print(x)
```

```python
myresult = mycursor.fetchone() # fetch 1st row from last executed statement
```

##### `WHERE` -- Filter
```python
sql = "SELECT * FROM my_table WHERE name = %s"
val = ('George',)

mycursor.execute(sql, val)
```
*Using the placeholder* **`%s`** *prevents **SQL injections***

##### `ORDER BY`
```python
sql = "SELECT * FROM my_table ORDER BY name ASC/DESC"  
```

##### `LIMIT` -- OFFSET
```python
sql = "SELECT * FROM my_table LIMIT 5 OFFSET 3"
```
*Start at 4th row, return $\leq$ 5 rows*

___
#### `JOIN`

(create another table called "ages" with id as primary key)
```python
sql = "SELECT \
  my_table.name as name, \
  ages.age as age \
  FROM my_table \
  INNER JOIN ages ON my_table.id = ages.id"
```
*Display names and ages*

- `INNER JOIN`: intersection of both tables
- `FROM table_a` **`FULL JOIN`** `table_b`: union of both tables
- `FROM table_a` **`LEFT JOIN`** `table_b`: includes all rows from table_a whether table_b has corresponding row or not
- `FROM table_a` **`RIGHT JOIN`** `table_b`: same but for table_b

