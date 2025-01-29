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
… ;
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

