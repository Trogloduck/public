< [[05 Programming]]

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

**Immutable** objects: ID attributed to object may change if object is modified

Ex:
```python
x = 1
print(id(x))
x += 1
print(id(x))
```
*prints different IDs*

**Mutable** object: ID doesn't change

Ex:
```python
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
___

At the end of `my_script.py`:
```python
if __name__ == "__main__":
    my_function()
```

`__name__` is a built-in variable that is automatically set to `"__main__"` if `my_script.py` is directly executed

In terminal, `python my_script.py` --> `__name__ = "__main__"` --> it will execute `my_function`

If I import `my_script.py` in `another_script.py`, then `__name__ = my_script` so it won't execute `my_function`, the function will only execute if the line `my_script.my_function()` is included in `another_script.py`
___

**[[OOP]]**: Object-oriented programming
___

**[[VirtualEnv]]**: Install needed dependencies in separate Python environment to avoid conflicts
___

**[[Good practices]]**
___

**[[Python packages]]**
