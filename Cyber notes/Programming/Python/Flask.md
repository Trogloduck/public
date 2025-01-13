Create web application using only Python

#### Start flask app
```powershell
$env:FLASK_APP = "flask_website.py"
flask run
```

```python
from flask import Flask

# initialize Flask app
app = Flask(__name__)

# define route for root URL
@app.route('/')
def hello():
    return 'Hello, World!'
```

![[Pasted image 20250110115313.png]]
___
#### Debug mode
> ***Test modifications in real time** on the web app's script without reloading the flask app (just refreshing web page, not turning flask off an on again)*

```powershell
$env:FLASK_DEBUG=1
```
*(turn off when deployed for clients)*

Debug mode can be activated at the end of the flask app script:
```python
if __name__ == '__main__':
    app.run(debug=True)
```

___

**Flask routes** can be made ***dynamically***
```python
@app.route("/about/<username>")
def about_page(username):
    return f"<h1>About Page of {username}</h1>"
```

**Clean practice** (use **`render_template`**)
```python
from flask import Flask, render_template

# initialize Flask app
app = Flask(__name__)

# define route for root URL
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('index.html')
```
*Notice **several routes** can lead to the same html page (`'/'` and `'/home'` lead to `index.html`)*

In a subfolder of the main project, called "templates", `index.html`:
```html
<h1>Hello world!</h1>
<!-- Some more html content -->
```

To style the website, use styling framework $\rightarrow$ Bootstrap

___
# Jinja

### Loop

*Jinja can be used to create Python loops within HTML code*

1. In the main python flask script, create a list of dictionaries, each containing information about an item
```python
items = [
    {'id': 1, 'name': 'A night stargazing with Mark Zuckerberg', 'barcode': '893212299897', 'price': 10},
    {'id': 2, 'name': 'A bowling game with Jeffrey Bezos', 'barcode': '123985473165', 'price': 7},
    {'id': 3, 'name': 'A dinner and a heated debate with Elon Musk', 'barcode': '123985473165', 'price': 10}
]
```

2. In an HTML page that needs to access data in the list, create a loop
```html
{% for item in items %}
	<tr>
		<td>{{ item.id }}</td>
		<td>{{ item.name }}</td>
		<td>{{ item.barcode }}</td>
		<td>{{ item.price }}$</td>
	</tr>
{% endfor %}
```

### Template inheritance

*Jinja can be used to create an HTML base template that will be reused in our pages*

base.html
```html
<!doctype html>
<html lang="en">
   <head>
      <!-- Required meta tags -->
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
      <title>
          {% block title %}
  
          {% endblock %}
      </title>
   </head>
   <body>
      {% block content %}
  
      {% endblock %}
      <!-- Future Content here -->
   </body>
   <style>
      body {
      background-color: #212121;
      color: white
      }
   </style>
</html>
```

index.html
```html
{% extends 'base.html' %}
{% block title %}
    Home Page
{% endblock %}

{% block content %}
    This is content for the Home Page
{% endblock %}
<!-- Some more html content -->
```

*The index.html page inherits from the base.html and can add more content to it.*

