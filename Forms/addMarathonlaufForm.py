from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields import DecimalField
from wtforms import validators


class AddMarathonlaufForm(FlaskForm):
    Preisgeld = DecimalField("Preisgeld", validators=[
                             validators.InputRequired()])
    Kilometer = DecimalField("Kilometer", validators=[
                             validators.InputRequired()])
    Datum = DateField("dueDate", validators=[validators.InputRequired()])
    Preis_für_Teilnahme = DecimalField(
        "Preisgeld", validators=[validators.InputRequired()])
    Besucher = DecimalField("Besucher", validators=[
                            validators.InputRequired()])
