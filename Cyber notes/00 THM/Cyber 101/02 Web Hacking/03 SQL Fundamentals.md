https://tryhackme.com/room/sqlfundamentals

### Table of contents
- [[#Intro]]
- [[#Database and Table Statements]]
- [[#CRUD]]
	- [[#Create - INSERT]]
	- [[#Read - SELECT]]
	- [[#UPDATE]]
	- [[#DELETE]]
- [[#Clauses]]
- [[#Operators]]
- [[#Functions]]

___
### Intro
[[#Table of contents|Back to the top]]

- **Relational Databases** (SQL): table-based
- **Non-relational Databases** (NoSQL): inconsistent data format but still organized in same place (e.g. social media platforms collecting user-generated content)

![[Pasted image 20251120143607.png]]

- **Primary key**: unique identifier for data
- **Foreign key**: identifier from other table, providing a link between tables

___
### Database and Table Statements
[[#Table of contents|Back to the top]]

`CREATE DATABASE database_name;`

`SHOW DATABASES;`

`USE database_name;`

`DROP database_name;`

```SQL
CREATE TABLE my_table (
	my_column1 data_type,
	my_column2 data_type,
);
```

`DESCRIBE my_table`

```SQL
ALTER TABLE my_table
ADD new_column data_type;
```

`DROP TABLE my_table`

___
### CRUD
[[#Table of contents|Back to the top]]
*Create, Read, Update, Delete*
#### Create - INSERT

```SQL
INTERT INTO my_table (my_column1, my_column2)
VALUES (my_value1, my_value2);
```

#### Read - SELECT

```SQL
SELECT my_column FROM my_table;
```

#### UPDATE

```SQL
UPDATE my_table
SET my_column2 = "new_value2"
WHERE my_column1 = my_value1;
```

#### DELETE

```SQL
DELETE FROM my_table where my_column1 = my_value1;
```

___
### Clauses
[[#Table of contents|Back to the top]]

`FROM`, `WHERE`, `DISTINCT`, `GROUP BY`, `ORDER BY` (`ASC`/`DESC`), `HAVING`, ...

`SELECT DISTINCT my_column FROM my_table;`


___
### Operators
[[#Table of contents|Back to the top]]

Logical: `TRUE`, `FALSE`

`LIKE`
```SQL
SELECT my_column1 FROM my_table
WHERE my_column2 like "%my_pattern%";
```

`AND`, `OR`, `NOT`

`BETWEEN` (`WHERE my_column1 BETWEEN my_value1 AND my_value2`)

Mathematical: `=`, `!=`, `<`, `<=`, `>`, `>=`

___
### Functions
[[#Table of contents|Back to the top]]

`CONCAT()`: combine text from different **columns**
```SQL
SELECT CONCAT(my_column1, " is the value of column1 for ", my_column2, " which is the value for column2") AS column1_column2 FORM my_table;
```

`GROUP_CONCAT()`: combine text from different **rows**
```SQL
SELECT my_column1, GROUP_CONCAT(my_column2 SEPARATOR ", ") AS my_table FROM my_table
GROUP BY my_column1;
```

`SUBSTRING()`: retrieve substring starting at determined position
```SQL
SELECT SUBSTRING(my_column1, start_index, number_of_characters_in_substring) AS my_new_column FROM my_table;
```

`LENGTH(my_column)`: counts number of characters

`COUNT(*)`: counts number of rows

`SUM(my_column)`: sums all values

`MAX()`, `MIN()`: finds max or min value from column