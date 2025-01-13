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
        return f'Item {self.id}: {self.name}'


# define route for market URL
@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)

# activate server with debug mode on
if __name__ == '__main__':
    app.run(debug=True)