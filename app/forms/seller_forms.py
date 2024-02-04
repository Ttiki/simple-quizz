from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, StringField, HiddenField


class AddItemForm(FlaskForm):
    name = StringField('Item Name')
    description = StringField('Item Description')
    initial_price = IntegerField('Initial Price')
    item_id = HiddenField('Item ID')
    submit = SubmitField('Update Item')
