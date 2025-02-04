**`;`**: always end command with semicolon

**`#`**: comment

Command lines: not case-sensitive

Column, table names: case-sensitive

Possible to write SQL command on several lines by not ending the line with **`;`** and then hitting `ENTER`

**`SHOW DATABASES`**: show existing databases

**`CREATE DATABASE my_database`**: create my_database >< `DROP DATABASE`

**Create a table**

**`USE my_database`**: use my_database as default for subsequent statements

```mysql
CREATE TABLE IF NOT EXISTS my_table (
	my_column _DataType_ _TableConstraint_ DEFAULT _default_value_,
	another_column _DataType_ _TableConstraint_ DEFAULT _default_value_,
	…
);
```

In the creation of the table, I can make the "id" the primary key:
```mysql
CREATE TABLE IF NOT EXISTS my_table (
	id INT unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY,
	…
);
```

[Data types](https://dev.mysql.com/doc/refman/8.0/en/data-types.html)

**`DESCRIBE my_table`**: displays column names, datatypes, null, key, default value, extra

*Alternative with more info:* `SHOW CREATE TABLE my_table`

**Adding columns**
```mysql
ALTER TABLE my_table
ADD my_column _DataType_ _TableConstraint_ DEFAULT _default_value_,
	another_column …;
```
**Dropping columns
```mysql
ALTER TABLE my_table
DROP my_column, another_column, …;
```

**Adding records (rows)**
```mysql
INSERT INTO my_table (my_column, another_column)
VALUES (my_value_1, another_value_1), (my_value_2, another_value_2), …;
```
**Deleting records**
```mysql
DELETE FROM my_table
WHERE _condition_;
```


___
More info: https://dev.mysql.com/doc/mysql-getting-started/en/