from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import StringField, HiddenField
from wtforms.fields import DecimalField


class EditMarathonlaufForm(FlaskForm):
    MarathonID = HiddenField("MarathonID")
    Preisgeld = DecimalField("Preisgeld")
    Kilometer = DecimalField("Kilometer")
    Datum = DateField("Datum")
    Preis_für_Teilnahme = DecimalField("Preis_für_Teilnahme")
    Besucher = StringField("Besucher")
