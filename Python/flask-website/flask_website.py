"""
Flask app for the web interface
"""

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)

# define route for root URL
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('index.html')

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    barcode = db.Column(db.String(12), nullable=False, unique=True)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(1024), nullable=False, unique=True)

    def __repr__(self):
        return f'Item {self.name}'


# define route for market URL
@app.route('/market')
def market_page():
    items = [
    {'id': 1, 'name': 'A night stargazing with Mark Zuckerberg', 'barcode': '893212299897', 'price': 10},
    {'id': 2, 'name': 'A bowling game with Jeffrey Bezos', 'barcode': '123985473165', 'price': 7},
    {'id': 3, 'name': 'A dinner and a heated debate with Elon Musk', 'barcode': '123985473165', 'price': 10}
    ]
    return render_template('market.html', items=items)

# activate server with debug mode on
if __name__ == '__main__':
    app.run(debug=True)