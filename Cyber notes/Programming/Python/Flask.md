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

