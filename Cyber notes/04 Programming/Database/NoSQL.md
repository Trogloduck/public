- [[#Types of NoSQL]]
- [[#Primary key (PK) - Foreign key (FK)]]
- [[#Normalization]]

___

## Types of NoSQL

#### Column
Timestamp differentiate valid - old/stale values, typically used in distributed environments with syncing system

#### Graph
Data into nodes, relationships into edges

#### Key-value
Dictionary/Hashtable. Key: word. Value: definition. 

#### Document
All details of an object in one instance


![[Pasted image 20250205102117.png]]

##### Primary key (PK) - Foreign key (FK)

![[Pasted image 20250205102812.png]]

*For **Customer**, the **primary key** is **CustomerID**, we can join Orders with Customer using CustomerID. In **Orders**, **OrderID** is the primary key, while **CustomerID** is considered a **foreign key***


**Entity integrity**: *primary key can't be null*

**Referential integrity**: *a **foreign key** must always **match** up with a **primary key** (otherwise, we have an orphan record)*

### Normalization

- Eliminate redundancy (prevent duplicates)
- Ensure logical entities

Rational to group attributes together

#### 1NF -- 1st normal form

Arrange data in spreadsheet

Columns: attributes

Unique PK

**No repeating groups**: if repeating, break it down into several records

##### *Example*

**Repeating groups**

Items table:

| Name  | Group                  |
| ----- | ---------------------- |
| item1 | group1, group2         |
| item2 | group2                 |
| item3 | group1, group2, group3 |

**No repeating groups**

Name table:

| id (PK) | Name  | GroupID (FK) |
| ------- | ----- | ------------ |
| 1       | item1 | 1            |
| 2       | item1 | 2            |
| 3       | item2 | 2            |
| 4       | item3 | 1            |
| 5       | item3 | 2            |
| 6       | item3 | 3            |

Group table:

| GroupID (PK) | Group  |
| ------------ | ------ |
| 1            | group1 |
| 2            | group2 |
| 3            | group3 |

#### 2NF -- 2nd normal form

Also 1NF

**No partial dependencies**

**Partial dependency**: attribute depends on PK only partially

##### *Example*

**With partial dependencies**

Orders table:

| OrderID | OrderDate | CustomerID | LastName | Address | BookID | Title | Price | Quantity |
| ------- | --------- | ---------- | -------- | ------- | ------ | ----- | ----- | -------- |

**Without partial dependencies**

Orders tables:

| OrderID | OrderDate | CustomerID | LastName | Address |
| ------- | --------- | ---------- | -------- | ------- |

Books cost table:

| BookID | Title | Price |
| ------ | ----- | ----- |

Books quantity table:

| OrderID | BookID | Quantity |
| ------- | ------ | -------- |
***NB**: OrderID and BookID form a **composite key**: a PK formed of several fields*

#### 3NF -- 3rd normal form

Also 2NF

**No transitive dependencies**

Transitive dependency: value which is not at all dependent on PK, but rather on another field or fields

##### *Example*

**With transitive dependencies**

Orders table:

| OrderID | OrderDate | CustomerID | LastName | Address |
| ------- | --------- | ---------- | -------- | ------- |
*LastName and Address depend on CustomerID*


**Without transitive dependencies**

Orders table:

| OrderID | OrderDate | CustomerID |
| ------- | --------- | ---------- |

Customers table:

| CustomerID | LastName | Address |
| ---------- | -------- | ------- |
