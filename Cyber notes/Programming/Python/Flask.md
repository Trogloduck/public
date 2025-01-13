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

#### Navigation bar
```html
<nav class="navbar navbar-expand-md navbar-dark bg-dark">
	<a class="navbar-brand" href="#">Flask Market</a>
	<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav">
		<span class="navbar-toggler-icon"></span>
	</button>
	<div class="collapse navbar-collapse" id="navbarNav">
		<ul class="navbar-nav mr-auto">
			<li class="nav-item active">
				<a class="nav-link" href="{{ url_for('home_page') }}">Home <span class="sr-only">(current)</span></a>
			</li>
			<li class="nav-item">
				<a class="nav-link" href="{{ url_for('market_page') }}">Market</a>
			</li>
		</ul>
		<ul class="navbar-nav">
			<li class="nav-item">
				<a class="nav-link" href="#">Login</a>
			</li>
			<li class="nav-item">
				<a class="nav-link" href="#">Register</a>
			</li>
		</ul>
	</div>
</nav>
```

Navigate between different pages of the website

Home and market pages are functional while login and register are not 

**`{{ url_for('home_page') }}`** jinja syntax: fetch link to home page from main flask script (`def home_page()`)
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

___
# SQLAlchemy

```python
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    barcode = db.Column(db.String(12), nullable=False, unique=True)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(1024), unique=True)

    def __repr__(self):
        return f'Item {self.id}: {self.name}'
```

`id` is mandatory

`100` is the max length of `name
`
`nullable=False`: item cannot have empty name

`unique=True`: 2 items cannot have same name

`__repr__` method: custom representation of data when using `Item.query.all()` 
## Create database.db file

Execute `python` in the directory of the main *project*.py
```python
from project import db
db.create_all()
```
or
```python
from flask_website import app, db
with app.app_context():
    db.create_all()
```

Alternative: same lines in flask shell
```powershell
$env:FLASK_APP="project.py"
flask shell
```
#### Add item to database

In the python or flask shell
```python
item1 = Item(name="Premium package", price=25, barcode='012345678912', description="You know it's just a better experience")
db.session.add(item1)
db.session.commit()
```

`Item.query.all()`: check content of database

#### Looping
```python
for item in Item.query.all():
	item.id
	item.name
	item.price
	item.description
```
*shows info for all items*
#### Filtering
```python
for item in Item.query.filter_by(price=25):
	item.name
```
*shows name of all items with price=25*

