from flask_wtf import FlaskForm
from wtforms.fields.simple import HiddenField


class DeleteLauferForm(FlaskForm):
    LauferID = HiddenField("LauferId")
