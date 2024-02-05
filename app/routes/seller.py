from flask import Blueprint, jsonify, render_template, redirect, url_for, request

from app.forms.seller_forms import AddItemForm  # Updated import path
from app.models.bid import Bid
from app.models.db import db
from app.models.item import Item  # Import the Item model

seller_service = Blueprint('seller_service', __name__)


@seller_service.route('/list_items', methods=['GET'])
def list_items():
    """
    Renvoie une liste de tous les articles disponibles.

    :return: Le template 'list-items.html' avec la liste des articles.
    """
    items = Item.query.all()
    return render_template('list-items.html', items=items)


@seller_service.route('/view_item/<int:item_id>', methods=['GET', 'POST'])
def view_item(item_id):
    """
    View function to display an item and handle bid submission.

    Args:
        item_id (int): The ID of the item to be viewed.

    Returns:
        render_template: The rendered HTML template with the item details and bids.
    """
    item = Item.query.get(item_id)

    if request.method == 'POST':
        # Logic to handle bid submission
        bid_amount = request.form.get('bid_amount')
        # Validate and process the bid
        # You need to implement the logic for handling bids in your Bid model
        bid = Bid(item_id=item_id, amount=bid_amount)
        db.session.add(bid)
        db.session.commit()

    bids = Bid.query.filter_by(item_id=item_id).all()
    return render_template('view-item.html', item=item, bids=bids)


@seller_service.route('/update_item/<int:item_id>', methods=['GET', 'POST'])
def update_item(item_id):
    """
    Update an item in the database based on the provided data.

    Args:
        item_id (int): The ID of the item to be updated.

    Returns:
        If the item is successfully updated, it redirects to the list_items route.
        If the item is not found, it returns a JSON response with an error message and a 404 status code.
        Otherwise, it renders the update-item.html template with the form and item_id.
    """
    item = Item.query.get(item_id)
    if not item:
        return jsonify({"error": f"Item with ID {item_id} not found"}), 404

    form = AddItemForm(obj=item)

    if form.validate_on_submit():
        item.name = form.name.data
        item.description = form.description.data
        item.initial_price = form.initial_price.data
        db.session.commit()
        return redirect(url_for('seller_service.list_items'))

    return render_template('update-item.html', form=form, item_id=item_id)


@seller_service.route('/delete_item/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    """
    Delete a specific item by ID.

    Args:
        item_id (int): The ID of the item to be deleted.

    Returns:
        A JSON response with a success message if the item is deleted successfully,
        or an error message if the item is not found.

    """
    # Logic to delete a specific item by ID
    item = Item.query.get(item_id)
    if item:
        # Delete the item from the database based on item_id
        db.session.delete(item)
        db.session.commit()
        return jsonify({"message": f"Item {item_id} deleted successfully"}), 200
    else:
        return jsonify({"error": f"Item with ID {item_id} not found"}), 404


@seller_service.route('/add_item', methods=['GET', 'POST'])
def add_item():
    """
    Add a new item to the inventory.

    This function handles the '/add_item' route and allows sellers to add a new item to the inventory.
    It validates the form data, creates a new item object, adds it to the database, and redirects to the list_items route.

    Returns:
        A redirect response to the list_items route.

    """
    form = AddItemForm()
    if form.validate_on_submit():
        # Create a new item based on the form data
        new_item = Item(
            name=form.name.data,
            description=form.description.data,
            initial_price=form.initial_price.data
        )
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('seller_service.list_items'))

    return render_template('add-item.html', form=form)
