from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import StringField
from wtforms import validators


class AddLauferForm(FlaskForm):
    Herkunft = StringField("Herkunft", validators=[validators.InputRequired()])
    Email = StringField("Email", validators=[validators.InputRequired()])
    Nachname = StringField("Nachname", validators=[validators.InputRequired()])
    Vorname = StringField("Vorname", validators=[validators.InputRequired()])
    Geburtsdatum = DateField("dueDate", validators=[
                             validators.InputRequired()])
