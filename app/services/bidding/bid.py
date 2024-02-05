from datetime import datetime

from app.models.bid import Bid
from app.models.db import db
from app.models.item import Item


def create_bidding(item_id, initial_price):
    """
    Create a bidding for an item with the given item_id and initial_price.

    Args:
        item_id (int): The ID of the item.
        initial_price (float): The initial price for the bidding.

    Returns:
        dict: A dictionary containing the success status and a message.
            If the bidding is created successfully, the success status is True
            and the message is "Bidding created successfully".
            If the item with the given item_id is not found, the success status is False
            and the error message is "Item with ID {item_id} not found".
            If the initial price is not greater than the current initial price of the item,
            the success status is False and the error message is "Initial price must be greater
            than the current initial price".

    Raises:
        None
    """
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
    """
    Retrieve bidding information for a given item.

    Args:
        item_id (int): The ID of the item.

    Returns:
        tuple: A tuple containing the bidding information and the HTTP status code.
            The bidding information is a dictionary with the following keys:
                - item_id (int): The ID of the item.
                - item_name (str): The name of the item.
                - current_price (float): The current price of the item.
                - bids (list): A list of dictionaries representing each bid, with the following keys:
                    - bid_id (int): The ID of the bid.
                    - amount (float): The amount of the bid.
            The HTTP status code indicates the success or failure of the request.
    """
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
    """
    Place a bid on an item.

    Args:
        item_id (int): The ID of the item.
        amount (float): The amount of the bid.

    Returns:
        dict: A dictionary containing the success status and a message.
            - If the bid is placed successfully, the success status is True and the message is "Bid placed successfully".
            - If the item with the given ID is not found, the success status is False, the error status is 404,
              and the error message indicates that the item was not found.
            - If the bid amount is less than or equal to the current initial price of the item,
              the success status is False, the error status is 400,
              and the error message indicates that the bid amount must be greater than the current initial price.
    """
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
    """
    Retrieve all ongoing bids.

    Returns:
        list: A list of ongoing bids.
    """
    current_time = datetime.now()
    return Item.query.filter(Item.end_time > current_time).all()


def get_current_highest_bid(item_id):
    """
    Get the current highest bid amount for a given item.

    Parameters:
    item_id (int): The ID of the item.

    Returns:
    int or None: The amount of the highest bid, or None if there are no bids for the item.
    """
    highest_bid = Bid.query.filter_by(item_id=item_id).order_by(Bid.amount.desc()).first()
    if highest_bid:
        return highest_bid.amount
    return None
