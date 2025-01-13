"""
Flask app for the web interface
"""

from flask import Flask, render_template

# initialize Flask app
app = Flask(__name__)

# define route for root URL
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('index.html')

@app.route('/market')
def market_page():
    items = [
    {'id': 1, 'name': 'A night stargazing with Mark Zuckerberg', 'barcode': '893212299897', 'price': 10},
    {'id': 2, 'name': 'A bowling game with Jeffrey Bezos', 'barcode': '123985473165', 'price': 7},
    {'id': 3, 'name': 'A dinner and a heated debate with Elon Musk', 'barcode': '123985473165', 'price': 10}
]
    return render_template('market.html', items=items)


if __name__ == '__main__':
    app.run(debug=True)