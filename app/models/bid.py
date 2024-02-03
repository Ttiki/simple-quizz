from datetime import datetime

from app.models.db import db


class Bid(db.Model):
    __tablename__ = 'bids'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)

    def __repr__(self):
        return f"<Bid(id={self.id}, amount={self.amount}, user={self.user}, item_id={self.item_id}, timestamp={self.timestamp})>"
