I can create a library with custom functions then import it to call the functions
The library just needs to be in the same folder

`ip = "%i.%i.%i.%i" % (a, b, c, d)`
*this will create a string "a.b.c.d"*

```
import os
command = "ssh root@{ip_address} -p 22"
os.system(command)
```
*this will create a* `command` *that we want the python script to execute in the shell*
*in this example the command uses* `ssh` *to connect to* `ip_address`*, using default user* `root` *and default port* `22`*
___

**Immutable** objects:
ID attributed to object may change if object is modified

Ex:
```
x = 1
print(id(x))
x += 1
print(id(x))
```
*prints different IDs*

**Mutable** object:
ID doesn't change

Ex:
```
x = [1, 2, 3]
print(id(x))
x.append(4)
print(id(x))
```
*prints same ID*

| Mutable         | Immutable |
| --------------- | --------- |
| \[Lists]        | Numbers   |
| {Dictionaries:} | "Strings" |
| {Sets}          | (Tuples)  |
