# app/__init__.py

from flask import Flask
from .models.db import db
from .models.item import Item
from .models.bid import Bid
from .routes.seller import seller_service
from .routes.bid import bidding_service


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///esbay.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the SQLAlchemy extension
    db.init_app(app)

    # Register the seller_service Blueprint
    app.register_blueprint(seller_service)
    app.register_blueprint(bidding_service)

    # Initialize the database and create tables
    with app.app_context():
        db.create_all()

        # Insert some initial data for testing
        item1 = Item(name="Laptop", description="Powerful laptop", initial_price=800)
        item2 = Item(name="Smartphone", description="Latest smartphone", initial_price=500)

        bid1 = Bid(amount=900, item=item1)
        bid2 = Bid(amount=550, item=item2)

        db.session.add_all([item1, item2, bid1, bid2])
        db.session.commit()

    return app
