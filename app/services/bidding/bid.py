from datetime import datetime

from app.models.bid import Bid
from app.models.db import db
from app.models.item import Item


def create_bidding(item_id, initial_price):
    item = Item.query.get(item_id)

    if item is None:
        return {"success": False, "error": f"Item with ID {item_id} not found"}, 404

    if item.initial_price >= initial_price:
        return {"success": False, "error": "Initial price must be greater than the current initial price"}, 400

    new_bid = Bid(amount=initial_price, item=item)
    db.session.add(new_bid)
    db.session.commit()

    return {"success": True, "message": "Bidding created successfully"}, 201


def get_bidding(item_id):
    item = Item.query.get(item_id)

    if item is None:
        return {"success": False, "error": f"Item with ID {item_id} not found"}, 404

    bidding_info = {
        "item_id": item.id,
        "item_name": item.name,
        "current_price": item.initial_price,
        "bids": [{"bid_id": bid.id, "amount": bid.amount} for bid in item.bids]
    }

    return bidding_info, 200


def place_bid(item_id, amount):
    item = Item.query.get(item_id)

    if item is None:
        return {"success": False, "error": f"Item with ID {item_id} not found"}, 404

    if amount <= item.initial_price:
        return {"success": False, "error": "Bid amount must be greater than the current initial price"}, 400

    new_bid = Bid(amount=amount, item=item)
    db.session.add(new_bid)
    db.session.commit()

    return {"success": True, "message": "Bid placed successfully"}, 201


def get_all_bids_for_item(item_id):
    """
    Get all bids for a specific item.

    Parameters:
    - item_id (int): ID of the item.

    Returns:
    - List of dictionaries representing bids for the item.
    """
    item = Item.query.get(item_id)

    if item is None:
        return {"error": f"Item with ID {item_id} not found"}, 404

    bids = Bid.query.filter_by(item_id=item_id).all()

    bid_list = [{"bid_id": bid.id, "amount": bid.amount} for bid in bids]

    return bid_list, 200


def get_ongoing_bids():
    current_time = datetime.now()
    return Item.query.filter(Item.end_time > current_time).all()
