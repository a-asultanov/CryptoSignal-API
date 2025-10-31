from extensions import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    alerts = db.relationship('Alert', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'


class Coin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(10), unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    alerts = db.relationship('Alert', backref='coin', lazy=True)

    def __repr__(self):
        return f'<Coin {self.symbol} - {self.name}>'

class Alert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    coin_symbol = db.Column(db.String(10), db.ForeignKey('coin.symbol'), nullable=False)
    target_price = db.Column(db.Float, nullable=False)
    is_triggered = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Alert {self.coin_symbol} @ {self.target_price}>'