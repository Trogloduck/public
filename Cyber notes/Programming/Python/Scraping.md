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
- `CONNECT`: use a proxy as communication tunnel
- `TRACE`: asks what server has received (test and diagnose the connection.
- `PUT`: add resource to server
- `DELETE`: delete resource from server

```python
import requests
from bs4 import BeautifulSoup

# website url
url = "https://letterboxd.com/incelticide/"

# send GET request to website
my_request = requests.get(url)

# display the url and status code
print(url, my_request.status_code)

# parse through content of the website
soup = BeautifulSoup(my_request.content, "lxml")

# display h1 titles
for header_tag in soup.find_all('h1'):
    print(header_tag.text)
```

___

# Targeted information retrieval

1. Go to website
2. Right-click > Inspector
3. Hover over interesting part, it will be highlighted in the HTML code
2+3. Right-click on element of interest > Inspector
4. Identify tag of interest

```python
import requests
from bs4 import BeautifulSoup

# website url
url = "https://letterboxd.com/incelticide/"

# send GET request to website
my_request = requests.get(url)

# display the url and status code
print(url, my_request.status_code)

# parse through content of the website
soup = BeautifulSoup(my_request.content, "lxml")

# display reviews titles
# html tag of review: <div class="body-text -prose collapsible-text">
index = 1
for review in soup.find_all('div', class_='body-text -prose collapsible-text'):
    print(f"_______________________\nReview n°{index}:\n{review.text}")
    index += 1

# display reviews titles
# html tag of movie title: <h2 class="headline-2 prettify">
index = 1
for title in soup.find_all('h2', class_='headline-2 prettify'):
    print(f"_______________________\nMovie n°{index}:\n{title.text}")
    index += 1

# combines displaying reviews and movie titles
index = 1
for review, title in zip(soup.find_all('div', class_='body-text -prose collapsible-text'),
                         soup.find_all('h2', class_='headline-2 prettify')):
    print(f"_______________________\nMovie n°{index}:\n{title.text}\n{review.text}")
    index += 1
```

Navigate through the website and collect data of interest by using the hrefs (`title.a["href"]`) and building URLs by concatenating, then fetch the data from the next webpage with GET:
```python
# display reviews titles and links to the film page and synopsis
index = 0
for title in soup.find_all(class_='headline-2 prettify'):
    print(f"_______________________\n{title.text}\n")
    film_page = "https://letterboxd.com" + title.a['href'].replace('/incelticide', '')
    print(f"Film page: {film_page}\n")
    index += 1
    # send GET request to film page
    film_request = requests.get(film_page)
    # parse through content of film page
    film_soup = BeautifulSoup(film_request.content, "lxml")
    # display synopsis of film
    synopsis = film_soup.find(class_='truncate').text
    print(f"Synopsis: {synopsis}\n")
```

Create a dataframe and save it in a .csv file (final step of scraping, full project), added time delays to not trigger suspicion by sending requests too fast
```python
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# website url
url = "https://letterboxd.com/incelticide/"

# send GET request to website
my_request = requests.get(url)
time.delay(1)

# display url and status code
print(url, my_request.status_code)

# parse through website content
soup = BeautifulSoup(my_request.content, "lxml")

# display movie titles, links to the film page and synopsis, and reviews in that order
index = 0
for title, review in zip(soup.find_all(class_='headline-2 prettify'),
                         soup.find_all('div', class_='body-text -prose collapsible-text')):
    print(f"_______________________\n{title.text}\n")
    film_page = "https://letterboxd.com" + title.a['href'].replace('/incelticide', '')
    time.delay(1)
    print(f"Film page: {film_page}\n")
    index += 1
    # send GET request to film page
    film_request = requests.get(film_page)
    # parse through content of film page
    film_soup = BeautifulSoup(film_request.content, "lxml")
    # display synopsis of film
    synopsis = film_soup.find(class_='truncate').text
    print(f"Synopsis: {synopsis}\n")
    print(f"Review:\n{review.text}\n")

# create a pandas dataframe
# create a dictionary with the data
data = {
    'Title': [title.text for title in soup.find_all(class_='headline-2 prettify')],
    'URL': ["https://letterboxd.com" + title.a['href'].replace('/incelticide', '') for title in soup.find_all(class_='headline-2 prettify')],
    'Synopsis': [film_soup.find(class_='truncate').text if film_soup.find(class_='truncate') else 'No synopsis available' for film_soup in [BeautifulSoup(requests.get("https://letterboxd.com" + title.a['href'].replace('/incelticide', '')).content, "lxml") for title in soup.find_all(class_='headline-2 prettify')]],
    'Review': [review.text for review in soup.find_all('div', class_='body-text -prose collapsible-text')]
}

# create a pandas dataframe
df = pd.DataFrame(data)

# display the dataframe
print(df)

# save the dataframe in a CSV file
df.to_csv('letterboxd_data.csv', index=False)
```