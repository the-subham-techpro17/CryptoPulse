from flask import Blueprint, render_template, request
from app.utils import get_crypto_price

main = Blueprint('main', __name__)

@main.route('/')
def home():
    # You can fetch multiple prices for different cryptocurrencies here
    crypto_prices = get_crypto_price()
    return render_template('index.html', crypto_prices=crypto_prices)

@main.route('/search', methods=['GET', 'POST'])
def search():
    coin_name = request.form.get('coin_name')
    price = get_coin_price_by_name(coin_name)
    
    # If coin not found, price will be "Not found"
    return render_template('result.html', coin_name=coin_name, price=price)

def get_coin_price_by_name(coin_name):
    crypto_prices = get_crypto_price()
    
    # Search for the coin in the dictionary and return its price
    if coin_name.lower() in crypto_prices:
        return crypto_prices[coin_name.lower()]['usd']
    else:
        return "Not found"
