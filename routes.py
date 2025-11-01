from flask import Blueprint, jsonify, request
from extensions import db
from models import User, Coin, Alert
from crypto_service import fetch_prices
import asyncio
from datetime import datetime

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/status', methods=['GET'])
def status_check():
    return jsonify({"status": "ok", "message": "CryptoSignal API is running"}), 200

@bp.route('/coins', methods=['GET'])
def get_coins():
    coins = Coin.query.all()
    coins_data = [{"symbol": coin.symbol, "name": coin.name, "price": coin.price} for coin in coins]
    return jsonify(coins_data), 200

@bp.route('/coins/update', methods=['POST'])
def update_prices():
    coins = Coin.query.all()
    symbols = [coin.name.lower() for coin in coins]
    prices = asyncio.run(fetch_prices(symbols))

    for coin in coins:
        if coin.name.lower() in prices:
            coin.price = prices[coin.name.lower()]
            coin.last_updated = datetime.utcnow()

    db.session.commit()
    return jsonify({"message": "Coin prices updated successfully"}), 200