# app/__init__.py

from flask import Flask
from sqlalchemy import create_engine, text

from .models.bid import Bid
from .models.db import db
from .models.item import Item
from .models.user import User
from .routes.bid import bidding_service
from .routes.seller import seller_service


def create_app():
    """
    Creates and configures the Flask application.

    Returns:
        Flask: The configured Flask application.
    """
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///esbay.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'fb7cdcd143d4a71051e27c3b2d8288acdea7f78c7d4857816789f916578da35d'

    # Initialize the SQLAlchemy extension
    db.init_app(app)

    # Check if 'users' table exists
    engine = create_engine('sqlite:///esbay.db')

    # Register the seller_service Blueprint
    app.register_blueprint(seller_service)
    app.register_blueprint(bidding_service)

    # Initialize the database and create tables
    with app.app_context():
        print("Context created")
        try:
            db.create_all()
        except Exception as e:
            print(f"Error creating tables: {e}")

        # Check if 'users' table exists
        with engine.connect() as connection:
            result = connection.execute(text("SELECT name FROM sqlite_master WHERE type='table' AND name='users'"))
            if result.fetchone():
                print("The 'users' table exists.")
            else:
                print("The 'users' table does not exist.")

        # Insert some initial data for testing
        item1 = Item(name="Laptop", description="Powerful laptop", initial_price=800)
        item2 = Item(name="Smartphone", description="Latest smartphone", initial_price=500)

        bid1 = Bid(amount=900, item=item1)
        bid2 = Bid(amount=550, item=item2)

        db.session.add_all([item1, item2, bid1, bid2])
        db.session.commit()

    return app
