from flask import Flask, request, redirect
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
from models import db, Laufer
from Forms.addLauferForm import AddLauferForm
laufer_blueprint = Blueprint('laufer_blueprint', __name__)

@laufer_blueprint.route("/laufer", methods=["get","post"])
def index():

    addLauferFormObject = AddLauferForm()

    if addLauferFormObject.validate_on_submit():
        print(addLauferFormObject.Herkunft.data)
        print(addLauferFormObject.Email.data)
        print(addLauferFormObject.Nachname.data)
        print(addLauferFormObject.Vorname.data)
        print(addLauferFormObject.Geburtsdatum.data)

        newLaufer = Laufer()
        newLaufer.Herkunft = addLauferFormObject.Herkunft.data
        newLaufer.Email = addLauferFormObject.Email.data
        newLaufer.Nachname = addLauferFormObject.Nachname.data
        newLaufer.Vorname = addLauferFormObject.Vorname.data
        newLaufer.Geburtsdatum = addLauferFormObject.Geburtsdatum.data

        db.session.add(newLaufer)
        db.session.commit()

        return redirect("/laufer")

    laufer = db.session.query(Laufer).all()
    return render_template("laufer.html", form = addLauferFormObject, items = laufer)