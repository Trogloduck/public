#### Open

**`open(/path, 'r'/'w')`**: opens file located at */path*, in *reading/writing* mode

*/path* can either be relative or absolute

**`'a'`**: opens and appends

**`'x'`**: creates new file and opens for writing

`'+'` can be used to modify `r`, `w`, ...

#### Close

**`file_name.close()`**

Best practice: opening with a *context manager* (closes file by itself at end of block of code, preventing errors)
```python
with open(file_name, 'r') as my_file:
	print(my_file.read())
```
*`my_file` exists outside of the block but is closed*

#### Opening with relative path

Allows to use `..` and `/` to navigate
```python
from pathlib import Path

relative_path = Path(__file__).parent / "./test/bogusfile.txt"

with relative_path.open() as my_file:
    print(my_file.read())
```
