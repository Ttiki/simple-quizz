# Import necessary modules
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, ValidationError

from app.services.bidding.bid import get_current_highest_bid


# Create a form for placing bids
class PlaceBidForm(FlaskForm):
    item_id = IntegerField('Item ID', validators=[DataRequired()])
    amount = IntegerField('Bid Amount', validators=[DataRequired()])
    submit = SubmitField('Place Bid')