< [[Python]]

*Automatic data collection on the Web*

# XML

*Language used to describe data and facilitate data exchange between machines and software*

`pip install numpy`

`pip install lxml`

![[XML example file]]

```python
import os
from lxml import etree

# Get directory in which the current script is located
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

# Web scraping
*In the same way it is possible to parse XML, it is possible to parse HTML, using beautifulsoup for instance*

`pip install beautifulsoup4`

```python
import os
from bs4 import BeautifulSoup

# Get directory in which the script is located
dir_path = os.path.dirname(os.path.realpath(__file__))

# Create a file path for the data.xml file
letterbox_file_path = os.path.join(dir_path, 'letterbox.html')

# Open the file and read its contents
with open(letterbox_file_path, 'r', encoding = "utf-8") as file:
    html_doc = file.read()
    
# Parse the contents of the file
soup = BeautifulSoup(html_doc, "lxml")

# Print the titles of the file
for header_tag in soup.find_all('h1'):
    print(header_tag.text)
```

## Scraping via HTTP requests

HTTP is used to manage web requests: HTTP **request** (client) -- HTTP **response** (server)

- `GET`: request resource
- `HEAD`: request header
- `POST`: modifies resource
- `OPTIONS`: obtain communication options of resource/server
- `CONNECT`: This method allows you to use a proxy as a communication tunnel
- `TRACE` This method asks the server to return what it has received, in order to test and diagnose the connection.
- `PUT` This method allows you to add a resource to the server.
- `DELETE` This method allows you to delete a resource from the server.

```python
example code for http requests
```
