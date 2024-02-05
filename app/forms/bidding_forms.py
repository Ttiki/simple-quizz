# Import necessary modules
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired


# Create a form for placing bids
class PlaceBidForm(FlaskForm):
    """
    A form class for placing bids.

    Attributes:
        item_id (IntegerField): The ID of the item being bid on.
        amount (IntegerField): The amount of the bid.
        submit (SubmitField): Button to submit the bid.
    """
    item_id = IntegerField('Item ID', validators=[DataRequired()])
    amount = IntegerField('Bid Amount', validators=[DataRequired()])
    submit = SubmitField('Place Bid')
