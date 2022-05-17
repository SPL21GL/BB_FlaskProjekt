from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, HiddenField
from wtforms.fields import DecimalField


class EditOrganisatorForm(FlaskForm):
    OrganisationID = HiddenField("OrganisationID")
    Anschrift = StringField("Preisgeld")
    Name = StringField("Name")
    Sponsoren = StringField("Sponsoren")
    Telefonnummer = DecimalField("Telefonnummer")
