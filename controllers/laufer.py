from flask import request, redirect, flash
from flask.templating import render_template
from flask import Blueprint
from models import db, Laufer
from Forms.addLauferForm import AddLauferForm
from Forms.deleteLauferForm import DeleteLauferForm
from Forms.editLauferForm import EditLauferForm
import sqlalchemy.orm

laufer_blueprint = Blueprint('laufer_blueprint', __name__)


@laufer_blueprint.route("/laufer")
def marathonlauf():

    addLauferFormObject = AddLauferForm()

    session: sqlalchemy.orm.scoping.scoped_session = db.session

    laufer = session.query(Laufer).order_by(Laufer.LauferID).all()

    return render_template("laufer.html", items=laufer, form=addLauferFormObject)


@laufer_blueprint.route("/laufer/addLauferForm", methods=["get", "post"])
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
    return render_template("addlauferForm.html", form=addLauferFormObject, items=laufer)


@laufer_blueprint.route("/laufer/delete", methods=["post"])
def deleteLaufer():
    deleteLauferFormObj = DeleteLauferForm()
    if deleteLauferFormObj.validate_on_submit():
        print("gültig")

        LauferIdToDelete = deleteLauferFormObj.LauferID.data
        LauferToDelete = db.session.query(Laufer).filter(
            Laufer.LauferID == LauferIdToDelete)
        LauferToDelete.delete()

        db.session.commit()
    else:
        print("Fatal Error")

    flash(f"Laufer with id {LauferIdToDelete} has been deleted")

    return redirect("/laufer")


@laufer_blueprint.route("/laufer/editLauferForm", methods=["post"])
def submitEditForm():
    editLauferFormObject = EditLauferForm()

    if editLauferFormObject.validate_on_submit():
        print("Submit wurde durchgeführt")

        LauferID = editLauferFormObject.LauferID.data

        Laufer_to_edit = db.session.query(Laufer).filter(
            Laufer.LauferID == LauferID).first()
        Laufer_to_edit.Herkunft = editLauferFormObject.Herkunft.data
        Laufer_to_edit.Email = editLauferFormObject.Email.data
        Laufer_to_edit.Nachname = editLauferFormObject.Nachname.data
        Laufer_to_edit.Vorname = editLauferFormObject.Vorname.data
        Laufer_to_edit.Geburtsdatum = editLauferFormObject.Geburtsdatum.data

        db.session.commit()

        return redirect("/laufer")
    else:
        raise ("Fatal Error")


@laufer_blueprint.route("/laufer/editLauferForm")
def showEditForm():
    LauferID = request.args["LauferID"]

    Laufer_to_edit = db.session.query(Laufer).filter(
        Laufer.LauferID == LauferID).first()

    editLauferFormObject = EditLauferForm()

    editLauferFormObject.LauferID.data = Laufer_to_edit.LauferID
    editLauferFormObject.Herkunft.data = Laufer_to_edit.Herkunft
    editLauferFormObject.Email.data = Laufer_to_edit.Email
    editLauferFormObject.Nachname.data = Laufer_to_edit.Nachname
    editLauferFormObject.Vorname.data = Laufer_to_edit.Vorname
    editLauferFormObject.Geburtsdatum.data = Laufer_to_edit.Geburtsdatum

    return render_template("editLauferForm.html", form=editLauferFormObject)
