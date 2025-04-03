Ain't Markup Language: human-readable data serialization language for managing data // JSON
- Case-sensitive.
- `.yml`
- Spaces for indentation, not tabs

```YAML
# mapping scalar to sequence
common_attr:
- element1
- element2
- …

# sequence mapping different collections
-
coll1_attr1: value11
coll1_attr2: value12
…
-
coll2_attr1: value21
coll2_attr2: value22
…
-
…

# separating collections
# collection_1
---
- coll1_obj1
- coll1_obj2
- …
# collection_2
---
- coll2_obj1
- coll2_obj2
- …

# mapping array to array
? [elem1,elem2,…]
: [attr1,attr2,…]
```