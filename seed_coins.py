from app import create_app
from extensions import db
from models import Coin

app = create_app()

with app.app_context():
    coins = [
        Coin(symbol="BTC", name="bitcoin", price=0),
        Coin(symbol="ETH", name="ethereum", price=0),
        Coin(symbol="CYBRO", name="cybro", price=0)
    ]
    db.session.add_all(coins)
    db.session.commit()
    print("Coins added successfully.")