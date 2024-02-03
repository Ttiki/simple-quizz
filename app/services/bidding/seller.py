from app.models.db import db
from app.models.item import Item


def list_items():
    # Logic to list all items from the database
    items = Item.query.all()
    return {"items": [item.serialize() for item in items]}, 200


def get_item(item_id):
    # Logic to retrieve details of a specific item by ID
    item = Item.query.get(item_id)
    if item:
        return {"item_id": item.id, "details": item.serialize()}, 200
    else:
        return {"error": f"Item with ID {item_id} not found"}, 404


def update_item(item_id, data):
    # Logic to update details of a specific item by ID
    item = Item.query.get(item_id)
    if item:
        item.update(data)  # You need to implement the update method in your Item model
        db.session.commit()
        return {"message": f"Item {item_id} updated successfully"}, 200
    else:
        return {"error": f"Item with ID {item_id} not found"}, 404


def delete_item(item_id):
    # Logic to delete a specific item by ID
    item = Item.query.get(item_id)
    if item:
        db.session.delete(item)
        db.session.commit()
        return {"message": f"Item {item_id} deleted successfully"}, 200
    else:
        return {"error": f"Item with ID {item_id} not found"}, 404
