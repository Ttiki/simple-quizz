from flask import Blueprint, jsonify

from app.models.db import db
from app.models.item import Item  # Import the Item model

seller_service = Blueprint('seller_service', __name__)


@seller_service.route('/list_items', methods=['GET'])
def list_items():
    # Logic to list all items from the database
    items = Item.query.all()
    return jsonify({"items": [item.serialize() for item in items]}), 200


@seller_service.route('/get_item/<int:item_id>', methods=['GET'])
def get_item(item_id):
    # Logic to retrieve details of a specific item by ID
    item = Item.query.get(item_id)
    if item:
        return jsonify({"item_id": item.id, "details": item.serialize()}), 200
    else:
        return jsonify({"error": f"Item with ID {item_id} not found"}), 404


@seller_service.route('/update_item/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    # Logic to update details of a specific item by ID
    item = Item.query.get(item_id)
    if item:
        # Update the item in the database based on the provided data
        item.update(data)  # You need to implement the update method in your Item model
        db.session.commit()
        return jsonify({"message": f"Item {item_id} updated successfully"}), 200
    else:
        return jsonify({"error": f"Item with ID {item_id} not found"}), 404


@seller_service.route('/delete_item/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    # Logic to delete a specific item by ID
    item = Item.query.get(item_id)
    if item:
        # Delete the item from the database based on item_id
        db.session.delete(item)
        db.session.commit()
        return jsonify({"message": f"Item {item_id} deleted successfully"}), 200
    else:
        return jsonify({"error": f"Item with ID {item_id} not found"}), 404
