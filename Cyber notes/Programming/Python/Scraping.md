*Automatic data collection on the Web*

#### XML

Language used to describe data and facilitate data exchange between machines and software

`pip install numpy`

`pip install lxml`

![[XML example file]]

```python
import os
from lxml import etree

# Get directory in which the script is located
dir_path = os.path.dirname(os.path.realpath(__file__))

# Create a file path for the data.xml file
file_path = os.path.join(dir_path, 'data.xml')

# Open the file and read its contents
with open(file_path, 'r') as my_file:
    tree = etree.parse(my_file)
    for name, job in tree.xpath('/users/user'):
        print(f"{name.text} is a {job.text}")
```
*displays the name and job of each user*

```python
for user in tree.xpath("/users/user"):
	print(user.get("data-id"))
```
*displays the data-id of each user*

```python
for user in tree.xpath("/users/user[job='Veterinary']/name"):
	print(user.text)
```
*displays the names of users whose job is Veterinary*

