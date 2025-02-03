**`;`**: always end command with semicolon

Command lines: not case-sensitive

Column, table names: case-sensitive

Possible to write SQL command on several lines by not ending the line with **`;`** and then hitting `ENTER`

**`SHOW DATABASES`**: show existing databases

**`CREATE DATABASE my_database`**: create my_database

**`USE my_database`**: subsequent changes will be done on my_database

Create my_table
```mysql
CREATE TABLE my_table
	(id INT UNSIGNED NOT NULL AUTO_INCREMENT,
	name VARCHAR(30) NOT NULL,
	PRIMARY KEY (id)
	);
```

