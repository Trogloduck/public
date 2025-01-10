Allows to create web application using only Python

To start flask app:
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

> **`Debug mode`** *allows to **test modifications in real time** on the web app's script without reloading the flask app (just refreshing web page, not turning flask off an on again)*

```powershell
$env:FLASK_DEBUG=1
```
*(turn off when deployed for clients)*

Debug mode can be activated at the end of the flask app script:
```python
if __name__ == '__main__':
    app.run(debug=True)
```

Flask routes can be made dynamically:
```python
@app.route("/about/<username>")
def about_page(username):
    return f"<h1>About Page of {username}</h1>"
```

Clean practice:
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
*Notice several routes can lead to the same html page (`'/'` and `'/home'` lead to `index.html`)*

In a subfolder of the main project, called "templates", `index.html`:
```html
<h1>Hello world!</h1>
```

To style the website, use styling framework $\rightarrow$ Bootstrap

