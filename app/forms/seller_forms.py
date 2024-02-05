from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, StringField, HiddenField


class AddItemForm(FlaskForm):
    """
    Form for adding an item to the seller's inventory.

    Attributes:
        name (StringField): Field for entering the item name.
        description (StringField): Field for entering the item description.
        initial_price (IntegerField): Field for entering the initial price of the item.
        item_id (HiddenField): Hidden field for storing the item ID.
        submit (SubmitField): Button for submitting the form.
    """
    name = StringField('Item Name')
    description = StringField('Item Description')
    initial_price = IntegerField('Initial Price')
    item_id = HiddenField('Item ID')
    submit = SubmitField('Update Item')
