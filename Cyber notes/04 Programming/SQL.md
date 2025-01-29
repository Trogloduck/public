*Structured Query Language: query, manipulate, transform data from relational database (collection of related (two-dimensional) tables)*

- SQL table: entity (object)
- SQL row: instance (type of object)
- SQL column: property (of the object)

# Query

Retrieve data from SQL database

```sql
SELECT my_column, another_column, …
FROM my_table;
```
*N.B: not case-sensitive, not indentation sensitive (could be a line)*

`SELECT *`: retrieve all columns

## With constraints

**`WHERE`**

```sql
SELECT my_column, another_column, …
FROM my_table
WHERE _condition_
	AND/OR _another_condition_
	AND/OR …;
```

**Logical/Mathematical Operators**
- `=`, `!=`, `<`, `>`, `<=`, `>=`
- (`NOT`) `BETWEEN ... AND ...`
- (`NOT`) `IN (...)` (in a list)
- `"string_1"` (`NOT`) `LIKE "string_2"`: case-insensitive str comparison
	- `%`: matches zero or more characters
	- `_`: matches any one character

