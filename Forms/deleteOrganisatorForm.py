from flask_wtf import FlaskForm
from wtforms.fields.simple import HiddenField


class DeleteOrganisatorForm(FlaskForm):
    OrganisationID = HiddenField("OrganisationID")
