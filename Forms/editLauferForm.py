from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import StringField, HiddenField


class EditLauferForm(FlaskForm):
    LauferID = HiddenField("LauferID")
    Herkunft = StringField("Herkunft")
    Email = StringField("Email")
    Nachname = StringField("Nachname")
    Vorname = StringField("Vorname")
    Geburtsdatum = DateField("Geburtsdatum")
