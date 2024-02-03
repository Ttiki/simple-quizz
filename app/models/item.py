from app.models.db import db


class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    initial_price = db.Column(db.Integer, nullable=False)
    closing_time = db.Column(db.DateTime, nullable=False)

    bids = db.relationship('Bid', backref='item', lazy=True)

    # Add a user_id field to link the seller to the user table
    # Update the foreign key reference to match the actual table name
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

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
