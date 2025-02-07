- [[#Setup]]
- [[#Common script - Setup]]
- [[#Create database and table]]
	- [[#`.insert()`]], [[#`.insert_one()`]], [[#`.insert_many()`]], [[#`_id`]]
- [[#Find data]], [[#Filter data]]
- [[#Miscellaneous]]


___
### Setup

Install community server: https://www.mongodb.com/try/download/community

Ensure .cfg file points to a path without spaces for log collection (`C:\Program Files\MongoDB\Server\8.0`)

Install MongoDB as a Microsoft service: 
```shell
mongod --config "C:\Program Files\MongoDB\Server\8.0\bin\mongod.cfg" --install
```

Start MongoDB server: `net start MongoDB` >< `net stop MongoDB`

For Python scripting, install pymongo: `pip install pymongo`

___
### Common script - Setup

```python
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/") # connect to MongoDB local server
mydb = myclient["mydatabase"] # select database
mycol = mydb["customers"] # select collection
```
*"Collections" are tables*

**NB**: MongoDB doesn't create empty databases/collections. It creates the database/collection when you insert rows into it.

### Create database and table

#### `.insert()`

##### `.insert_one()`

Create **dictionary** with **properties** as keys and **instances** as values, then **insert** into collection
```python
mydict = { "property_1": "instance_1", "property_2": "instance_2", … }
`x = mycol.insert_one(my_dict)`
```

##### `.insert_many()`

Create **list** of dictionaries, then insert into collection
```python
mylist = [  
  { "name": "Amy", "address": "Apple st 652"},  
  { "name": "Hannah", "address": "Mountain 21"},
  …
]  
x = mycol.insert_many(mylist)
```

##### `_id`

MongoDB automatically creates unique IDs for items added to collections. Specify IDs using `_id`
```python
mylist = [  
  { "_id": 1, "name": "John", "address": "Highway 37"},  
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  …
]
x = mycol.insert_many(mylist)
```

___
### Find data

#### `.find_one()`
```python
x = mycol.find_one()  
print(x)
```
*Returns 1st result*

##### `.find()`
Include all fields
```python
for x in mycol.find():  
  print(x)
```
Equivalent to `SELECT *`

Include several fields
```python
for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):  
  print(x)
```
*Will not return the IDs*

**Exclude** one field: `{ "_id": 0 }`

**Include** one field: `{ "_id": 0, "name":1 }` selects `name` (0 on `_id` field zeroes other fields)

**NB**: `{ "_id": 0, "name":1, "address":0 }` will return an error. Can't have a combination of 0s and 1s other than with the `_id`field

### Filter data



___
### Miscellaneous

```python
myclient.list_database_names() # return database list
mydb.list_collection_names() # return collection list
x.inserted_id # return IDs created by operation x
```
