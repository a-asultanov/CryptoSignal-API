from flask import Flask, jsonify
from config import Config
from extensions import db
from models import User, Coin, Alert


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)


    db.init_app(app)

    import routes
    app.register_blueprint(routes.bp)

    @app.route('/health', methods=['GET'])
    def health_check():
        return jsonify({"status": "ok", "message": "CryptoSignal API is running"}), 200

    return app


if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)