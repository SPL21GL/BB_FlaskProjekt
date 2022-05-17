from flask_wtf import FlaskForm
from wtforms.fields.simple import HiddenField


class DeleteMarathonlaufForm(FlaskForm):
    MarathonID = HiddenField("MarathonlaufID")
