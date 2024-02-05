from app.models.db import db
from app.models.item import Item


def list_items():
    """
    Retrieve a list of all items from the database.

    Returns:
        A tuple containing a dictionary with the serialized items and a status code.
    """
    items = Item.query.all()
    return {"items": [item.serialize() for item in items]}, 200


def get_item(item_id):
    """
    Retrieve details of a specific item by ID.

    Args:
        item_id (int): The ID of the item to retrieve.

    Returns:
        tuple: A tuple containing the item details and the HTTP status code.
            The item details are returned as a dictionary with the following keys:
                - "item_id": The ID of the item.
                - "details": The serialized details of the item.
            The HTTP status code indicates the success or failure of the operation.
            If the item is found, the status code is 200.
            If the item is not found, the status code is 404 and an error message is returned.
    """
    item = Item.query.get(item_id)
    if item:
        return {"item_id": item.id, "details": item.serialize()}, 200
    else:
        return {"error": f"Item with ID {item_id} not found"}, 404


def update_item(item_id, data):
    """
    Update the details of a specific item by ID.

    Args:
        item_id (int): The ID of the item to be updated.
        data (dict): The updated data for the item.

    Returns:
        dict: A dictionary containing the result of the update operation.
            If the item is found and updated successfully, the dictionary will contain
            a "message" key with a success message and a status code of 200.
            If the item is not found, the dictionary will contain an "error" key with
            an error message and a status code of 404.
    """
    item = Item.query.get(item_id)
    if item:
        item.update(data)  # You need to implement the update method in your Item model
        db.session.commit()
        return {"message": f"Item {item_id} updated successfully"}, 200
    else:
        return {"error": f"Item with ID {item_id} not found"}, 404


def delete_item(item_id):
    """
    Delete a specific item by ID.

    Args:
        item_id (int): The ID of the item to be deleted.

    Returns:
        dict: A dictionary containing the result of the deletion operation.
            If the item is deleted successfully, the dictionary will have a "message" key with a success message and a status code of 200.
            If the item is not found, the dictionary will have an "error" key with an error message and a status code of 404.
    """
    item = Item.query.get(item_id)
    if item:
        db.session.delete(item)
        db.session.commit()
        return {"message": f"Item {item_id} deleted successfully"}, 200
    else:
        return {"error": f"Item with ID {item_id} not found"}, 404
