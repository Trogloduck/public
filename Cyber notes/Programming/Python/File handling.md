#### Opening modes

**`open(/path, 'r'/'w')`**: opens file located at */path*, in *reading/writing* mode

*/path* can either be relative or absolute

**`'a'`**: opens and appends

**`'x'`**: creates new file and opens for writing

`'+'` can be used to modify `r`, `w`, ...

**`file_name.close()`**: always close file at the end in order to avoid errors


Best practice: opening with a ***context manager*** (closes file by itself at end of block of code, preventing errors)
```python
with open(file_name, 'r') as my_file:
	print(my_file.read())
```
or
```python
with file_name.open() as my_file:
	print(my_file.read())
```

*`my_file` exists outside of the block but is closed*

*`.open()` is a method of the Path object in the pathlib module*

#### OS
*Operating system dependent module allowing to do file/path manipulation*

**Script directory**

`import os`

```python
os.path.dirname(os.path.realpath(__file__))
```
*returns directory in which the current code/script is stored*

From there, it's possible to concatenate path to move relatively to the initial location (adding "`\..`" for instance)

Or

`from pathlib import Path`

```python
relative_path = Path(__file__).parent / "./test/bogus.txt"
```


```python
test_path = os.path.join(current_path, "test")
```
*adds `\path` or `/path` depending on OS to the current_path*

