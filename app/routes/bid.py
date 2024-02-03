from flask import Blueprint, jsonify, request, render_template

from app.services.bidding import bid

bidding_service = Blueprint('bidding_service', __name__)


@bidding_service.route('/ongoing_bids', methods=['GET'])
def ongoing_bids():
    # Assuming you have a method to retrieve ongoing bids from the database
    ongoing_bids = bid.get_ongoing_bids()

    return render_template('bids.html', bids=ongoing_bids)


@bidding_service.route('/create_bidding', methods=['POST'])
def create_bidding_route():
    data = request.get_json()

    if 'item_id' not in data or 'initial_price' not in data:
        return jsonify({"error": "Incomplete data provided"}), 400

    item_id = data['item_id']
    initial_price = data['initial_price']

    result, status_code = bid.create_bidding(item_id, initial_price)

    return jsonify(result), status_code


@bidding_service.route('/get_bidding/<int:item_id>', methods=['GET'])
def get_bidding_route(item_id):
    result, status_code = bid.get_bidding(item_id)

    return jsonify(result), status_code


@bidding_service.route('/place_bid/<int:item_id>', methods=['POST'])
def place_bid_route(item_id):
    data = request.get_json()

    if 'amount' not in data:
        return jsonify({"error": "Amount not provided"}), 400

    amount = data['amount']

    result, status_code = bid.place_bid(item_id, amount)

    return jsonify(result), status_code


@bidding_service.route('/get_bids/<int:item_id>', methods=['GET'])
def get_all_bids_for_item_route(item_id):
    result, status_code = bid.get_all_bids_for_item(item_id)
    return jsonify(result), status_code
