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
```
x = 1
print(id(x))
x += 1
print(id(x))
```
*prints different IDs*

**Mutable** object: ID doesn't change

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
___

At the end of `my_script.py`:
```
if __name__ == "__main__":
    my_function()
```

`__name__` is a built-in variable that is automatically set to `"__main__"` if `my_script.py` is directly executed

In terminal, `python my_script.py` --> `__name__ = "__main__"` --> it will execute `my_function`

If I import `my_script.py` in `another_script.py`, then `__name__ = my_script` so it won't execute `my_function`, the function will only execute if the line `my_script.my_function()` is included in `another_script.py`
___

[[OOP]]: Object-oriented programming
___

**VirtualEnv**: Install needed dependencies in separate Python environment to avoid conflicts

My virtualenv is intalled here: (it's not on PATH so I might have to move it)
`C:\Users\Windows 11\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\Scripts`
*seems to work*

***Create*** new env in current dir, default name "env": `python -m virtualenv env` or `virtualenv env`

***Activate***: `source env/bin/activate`
*When activating an env, it should automatically deactivate any other previously activated env*

Prompt change when env activated:
![[Pasted image 20240905095800.png]]

***Install "dependency"*** on env: pip dependency

***Save list*** all dependencies in "requirements.txt": `pip freeze > requirements.txt`

***Re-install*** dependencies: `pip install -r requirements.txt`

***De-activate*** env: `deactivate`
___
[[Good practices]]
___
[[Python packages]]
