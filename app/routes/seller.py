from flask import Blueprint, jsonify, render_template, redirect, url_for, request

from app.forms.seller_forms import AddItemForm  # Updated import path
from app.models.bid import Bid
from app.models.db import db
from app.models.item import Item  # Import the Item model

seller_service = Blueprint('seller_service', __name__)


@seller_service.route('/list_items', methods=['GET'])
def list_items():
    items = Item.query.all()
    return render_template('list-items.html', items=items)


@seller_service.route('/view_item/<int:item_id>', methods=['GET', 'POST'])
def view_item(item_id):
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
    return render_template('view-item.html',  item=item, bids=bids)


@seller_service.route('/update_item/<int:item_id>', methods=['GET', 'POST'])
def update_item(item_id):
    item = Item.query.get(item_id)
    if not item:
        return jsonify({"error": f"Item with ID {item_id} not found"}), 404

    form = AddItemForm(obj=item)

    if form.validate_on_submit():
        # Update the item in the database based on the provided data
        item.name = form.name.data
        item.description = form.description.data
        item.initial_price = form.initial_price.data
        db.session.commit()
        return redirect(url_for('seller_service.list_items'))

    return render_template('update-item.html', form=form, item_id=item_id)


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


@seller_service.route('/add_item', methods=['GET', 'POST'])
def add_item():
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
