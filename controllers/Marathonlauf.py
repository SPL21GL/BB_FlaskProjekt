from flask import request, redirect, flash
from flask.templating import render_template
from flask import Blueprint
from models import db, Marathonlauf
from Forms.addMarathonlaufForm import AddMarathonlaufForm
from Forms.deleteMarathonlaufForm import DeleteMarathonlaufForm
from Forms.editMarathonlaufForm import EditMarathonlaufForm
import sqlalchemy.orm

marathonlauf_blueprint = Blueprint('marathonlauf_blueprint', __name__)


@marathonlauf_blueprint.route("/marathonlauf")
def marathonlauf():

    addMarathonlaufFormObject = AddMarathonlaufForm()

    session: sqlalchemy.orm.scoping.scoped_session = db.session

    marathonlauf = session.query(Marathonlauf).order_by(
        Marathonlauf.MarathonID).all()

    return render_template("marathonlauf.html", marathonlauf=marathonlauf, form=addMarathonlaufFormObject)


@marathonlauf_blueprint.route("/marathonlauf/addMarathonLaufForm", methods=["get", "post"])
def index():

    addMarathonlaufFormObject = AddMarathonlaufForm()

    if addMarathonlaufFormObject.validate_on_submit():
        print(addMarathonlaufFormObject.Preisgeld.data)
        print(addMarathonlaufFormObject.Kilometer.data)
        print(addMarathonlaufFormObject.Datum.data)
        print(addMarathonlaufFormObject.Preis_für_Teilnahme.data)
        print(addMarathonlaufFormObject.Besucher.data)

        newMarathonlauf = Marathonlauf()
        newMarathonlauf.Preisgeld = addMarathonlaufFormObject.Preisgeld.data
        newMarathonlauf.Kilometer = addMarathonlaufFormObject.Kilometer.data
        newMarathonlauf.Datum = addMarathonlaufFormObject.Datum.data
        newMarathonlauf.Preis_für_Teilnahme = addMarathonlaufFormObject.Preis_für_Teilnahme.data
        newMarathonlauf.Besucher = addMarathonlaufFormObject.Besucher.data

        db.session.add(newMarathonlauf)
        db.session.commit()

        return redirect("/marathonlauf")

    marathonlauf = db.session.query(Marathonlauf).all()
    return render_template("addMarathonlaufForm.html", form=addMarathonlaufFormObject, items=marathonlauf)


@marathonlauf_blueprint.route("/marathonlauf/delete", methods=["post"])
def deleteMarathonlauf():
    deleteMarathonlaufFormObj = DeleteMarathonlaufForm()
    if deleteMarathonlaufFormObj.validate_on_submit():
        print("gültig")

        MarathonIdToDelete = deleteMarathonlaufFormObj.MarathonID.data
        MarathonlaufToDelete = db.session.query(Marathonlauf).filter(
            Marathonlauf.MarathonID == MarathonIdToDelete)
        MarathonlaufToDelete.delete()

        db.session.commit()
    else:
        print("Fatal Error")

    flash(f"Marathonlauf with id {MarathonIdToDelete} has been deleted")

    return redirect("/marathonlauf")


@marathonlauf_blueprint.route("/marathonlauf/editMarathonlaufForm", methods=["post"])
def submitEditForm():
    editMarathonlaufFormObject = EditMarathonlaufForm()

    if editMarathonlaufFormObject.validate_on_submit():
        print("Submit wurde durchgeführt")

        MarathonID = editMarathonlaufFormObject.MarathonID.data

        Marathonlauf_to_edit = db.session.query(Marathonlauf).filter(
            Marathonlauf.MarathonID == MarathonID).first()
        Marathonlauf_to_edit.Preisgeld = editMarathonlaufFormObject.Preisgeld.data
        Marathonlauf_to_edit.Kilometer = editMarathonlaufFormObject.Kilometer.data
        Marathonlauf_to_edit.Datum = editMarathonlaufFormObject.Datum.data
        Marathonlauf_to_edit.Preis_für_Teilnahme = \
            editMarathonlaufFormObject.Preis_für_Teilnahme.data
        Marathonlauf_to_edit.Besucher = editMarathonlaufFormObject.Besucher.data

        db.session.commit()

        return redirect("/marathonlauf")
    else:
        raise ("Fatal Error")


@marathonlauf_blueprint.route("/marathonlauf/editMarathonlaufForm")
def showEditForm():
    MarathonID = request.args["MarathonID"]

    Marathonlauf_to_edit = db.session.query(Marathonlauf).filter(
        Marathonlauf.MarathonID == MarathonID).first()

    editMarathonlaufFormObject = EditMarathonlaufForm()

    editMarathonlaufFormObject.MarathonID.data = Marathonlauf_to_edit.MarathonID
    editMarathonlaufFormObject.Preisgeld.data = Marathonlauf_to_edit.Preisgeld
    editMarathonlaufFormObject.Kilometer.data = Marathonlauf_to_edit.Kilometer
    editMarathonlaufFormObject.Datum.data = Marathonlauf_to_edit.Datum
    editMarathonlaufFormObject.Preis_für_Teilnahme.data = Marathonlauf_to_edit.Preis_für_Teilnahme
    editMarathonlaufFormObject.Besucher.data = Marathonlauf_to_edit.Besucher

    return render_template("editMarathonlaufForm.html", form=editMarathonlaufFormObject)
