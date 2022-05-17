from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField
from wtforms.fields import DecimalField
from wtforms import validators


class AddOrganisatorForm(FlaskForm):
    Anschrift = StringField("Anschrift", validators=[
                            validators.InputRequired()])
    Name = StringField("Name", validators=[validators.InputRequired()])
    Sponsoren = StringField("Sponsoren", validators=[
                            validators.InputRequired()])
    Telefonnummer = DecimalField("Telefonnummer", validators=[
                                 validators.InputRequired()])
