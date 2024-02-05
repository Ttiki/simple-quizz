from app.models.db import db


class Item(db.Model):
    """
    Represents an item in the e-commerce platform.

    Attributes:
    - id (int): The unique identifier of the item.
    - name (str): The name of the item.
    - description (str): The description of the item.
    - initial_price (int): The initial price of the item.
    - closing_time (datetime): The closing time of the item's auction.
    - bids (list): The list of bids placed on the item.
    - user_id (int): The ID of the user who listed the item.

    Methods:
    - __init__(self, name, description, initial_price, closing_time=None, user_id=None): Initializes a new Item object.
    - __repr__(self): Returns a string representation of the Item object.
    - update(self, data): Updates the item details based on the provided data.
    - serialize(self): Converts the item details to a dictionary for JSON serialization.
    """
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    initial_price = db.Column(db.Integer, nullable=False)
    closing_time = db.Column(db.DateTime, default=None, nullable=True)

    bids = db.relationship('Bid', backref='item', lazy=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, name, description, initial_price, closing_time=None, user_id=None):
        self.name = name
        self.description = description
        self.initial_price = initial_price
        self.closing_time = closing_time
        self.user_id = user_id

    def __repr__(self):
        return f"<Item(id={self.id}, name={self.name}, initial_price={self.initial_price}, closing_time={self.closing_time}, user_id={self.user_id})>"

    def update(self, data):
        """
        Update item details based on the provided data.

        Parameters:
        - data (dict): Dictionary containing the fields to be updated.

        Note: You should customize this method based on your specific fields.
        """
        if 'name' in data:
            self.name = data['name']
        if 'description' in data:
            self.description = data['description']
        if 'initial_price' in data:
            self.initial_price = data['initial_price']

        # Add more fields as needed

        # You might also want to validate the input data before updating

    def serialize(self):
        """
        Convert item details to a dictionary for JSON serialization.
        Customize this method based on your specific fields.
        """
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "initial_price": self.initial_price,
            # Add more fields as needed
        }
