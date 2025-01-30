*Structured Query Language: query, manipulate, transform data from relational database (collection of related (two-dimensional) tables)*

- SQL table: *entity* (object)
- SQL row: *instance* (type of object)
- SQL column: *property* (of the object)

___
# Basics

**`SELECT`**: query data from SQL database
```sql
SELECT my_column, another_column, …
FROM my_table;
```
*N.B: not case-sensitive, not indentation sensitive (could be a line)*

`SELECT *`: retrieve all columns

___
### Conditions

**`WHERE`**
```sql
SELECT my_column, another_column, …
FROM my_table
WHERE _condition_
	AND/OR _another_condition_
	AND/OR …;
```

##### Logical/Mathematical Operators

- `=`, `!=`, `<`, `>`, `<=`, `>=`
- (`NOT`) `BETWEEN ... AND ...`
- (`NOT`) `IN (...)` (in a list)
- `"my_column"` (`NOT`) `LIKE "string_2"`: case-insensitive str comparison
	- `%`: matches zero or more characters
	- `_`: matches any one character
- `IS` (`NOT`) `NULL`

##### Expressions: more complex conditions

*Example:*
```sql
SELECT particle_speed / 2.0 AS half_particle_speed
FROM physics_data
WHERE ABS(particle_position) * 10.0 > 500;
```

```sql
SELECT _col_expression_ AS _expr_description_, …
FROM mytable;
```
*used to  save time*

Keyword **`AS`** can be used to use aliases for expressions, columns, tables

##### Aggregate expressions -- Functions

```sql
SELECT AGG_FUNC(_column_or_expression_) AS aggregate_description, …
FROM mytable
WHERE _constraint_expression_;
```

Commun aggregate functions:
- `COUNT()`
- `MIN/MAX()`
- `AVG()`
- `SUM()`

**`GROUP BY my_column`**: groups rows that have same value in my_column

**`HAVING _condition_`**: add condition after grouping

___
### Filters

**`DISTINCT`**: keyword used to discard duplicates, usually used in conjunction with `GROUP BY`
```sql
SELECT DISTINCT my_column, another_column, …
FROM my_table
WHERE _condition(s)_;
```

**`ORDER BY`**
```sql
SELECT my_column, another_column, …
FROM my_table
WHERE _condition(s)_
ORDER BY my_column ASC/DESC;
```

**`LIMIT` & `OFFSET`**: used to determine subset of rows to return
```SQL
SELECT my_column, another_column, …
FROM my_table
WHERE _condition(s)_
ORDER BY column ASC/DESC
LIMIT num_limit OFFSET num_offset;
```

`LIMIT`: number of rows to return

`OFFSET` = x   \#start at x+1

*Often used in conjunction with `ORDER BY`*

___
# Multi-table query - `JOIN`

Tables sharing info about single entity have _primary key_ (identifies entity _uniquely_ across database).

Common primary key type: auto-incrementing integer (space efficient)

Str, hashed value also common

```sql
SELECT my_column, another_table_column, …
FROM my_table
INNER JOIN another_table
	ON my_table.id = another_table.id
…;
```
**`INNER JOIN`**: matches same key (.id) rows from my_table and another_table, key defined by **`ON`**

Also possible to match with different names keys:
```sql
ON my_table.id = another_table.number
```

- `INNER JOIN`: intersection of both tables
- `FROM table_a` **`FULL JOIN`** `table_b`: union of both tables
- `FROM table_a` **`LEFT JOIN`** `table_b`: includes all rows from table_a whether table_b has corresponding row or not
- `FROM table_a` **`RIGHT JOIN`** `table_b`: same but for table_b

___
# Query execution order

1. FROM & JOIN
2. WHERE
3. GROUP BY
4. HAVING
5. SELECT
6. DISTINCT
7. ORDER BY
8. LIMIT & OFFSET

---
# Modifying data

**Schema**: *describes **structure** of each table, and **datatypes** that each column of the table can contain $\Rightarrow$ **efficiency** & **consistency***

### Inserting rows

**`INSERT INTO`**
```sql
INSERT INTO my_table
VALUES (value_or_expr, another_value_or_expr, …),
	   (value_or_expr_2, another_value_or_expr_2, …),
	   …;
```
*number of values doesn't need to match number of columns, some columns can have default values*

```sql
INSERT INTO my_table
(my_column, another_column, …)
VALUES (value_or_expr, another_value_or_expr, …),
	   (value_or_expr_2, another_value_or_expr_2, …),
	   …;
```
*specifies for which columns we add data $\Rightarrow$ number of values needs to match number of columns*

### Updating rows

**`UPDATE`**
```sql
UPDATE my_table
SET my_column = value_or_expr,
	other_column = another_value_or_expr,
	…
WHERE _condition_;
```
*applies changes to rows of my_column, other_column which satisfy _condition_*

### Deleting rows

**`DELETE`**
```sql
DELETE FROM my_table
WHERE _condition_;
```

___
# Creating a table
*and 2 chairs*

### Schema

**`CREATE TABLE`**
```sql
CREATE TABLE IF NOT EXISTS my_table (
	my_column _DataType_ _TableConstraint_ DEFAULT _default_value_,
	another_column _DataType_ _TableConstraint_ DEFAULT _default_value_,
	…
);
```

### Data types

- INTEGER, BOOLEAN: integer number, boolean can be represented by 0/1
- FLOAT, DOUBLE, REAL: different types of numbers
- CHARACTER(num_chars), VARCHAR(num_chars), TEXT
- DATE, DATETIME
- BLOB: binary

### Constraints

- PRIMARY KEY: values in this column are unique, can be used to identify row
- AUTOINCREMENT: value is incremented with each row insertion
- UNIQUE: values in column are unique
- NOT NULL: value inserted can't be null
- CHECK (expression): use complex expression to test validity of values inserted (positive, certain size, start with certain prefix, etc.)
- FOREIGN KEY: consistency check, ensures each value in this column corresponds to another value in a column in another table

*Example:*
```sql
CREATE TABLE movies (
	id INTEGER PRIMARY KEY,
	title TEXT,
	director TEXT,
	year INTEGER,
	length_minutes INTEGER
);
```

___
## Altering a table -- `ALTER TABLE`
### Adding columns

**`ADD`**
```sql
ALTER TABLE my_table
ADD my_column DataType OptionalTableConstraint
	DEFAULT default_value;
```

### Removing columns

**`DROP`**
```sql
ALTER TABLE my_table
DROP my_column;
```

### Renaming a table

**`RENAME TO`**
```sql
ALTER TABLE my_table
RENAME TO new_name;
```

## Dropping tables

```sql
DROP TABLE IF EXISTS my_table;
```
*deletes my_table*

___
