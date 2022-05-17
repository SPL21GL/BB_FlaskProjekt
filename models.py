# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Laufer(db.Model):
    __tablename__ = 'laufer'

    LauferID = db.Column(db.Integer, primary_key=True, unique=True)
    Herkunft = db.Column(db.String(64))
    Email = db.Column(db.String(64))
    Nachname = db.Column(db.String(64))
    Vorname = db.Column(db.String(64))
    Geburtsdatum = db.Column(db.Date)


class MarathonLaufer(db.Model):
    __tablename__ = 'marathon_laufer'

    Marathon_LauferID = db.Column(db.Integer, primary_key=True, unique=True)
    LauferID = db.Column(db.ForeignKey('laufer.LauferID'), index=True)
    MarathonID = db.Column(db.ForeignKey(
        'marathonlauf.MarathonID'), index=True)

    laufer = db.relationship(
        'Laufer', primaryjoin='MarathonLaufer.LauferID == Laufer.LauferID', backref='marathon_laufers')
    marathonlauf = db.relationship(
        'Marathonlauf', primaryjoin='MarathonLaufer.MarathonID == Marathonlauf.MarathonID', backref='marathon_laufers')


class MarathonOrganisator(db.Model):
    __tablename__ = 'marathon_organisator'

    Marathon_OrganisatorID = db.Column(
        db.Integer, primary_key=True, unique=True)
    OrganisationID = db.Column(db.ForeignKey(
        'organisator.OrganisationID'), index=True)
    Marathon2ID = db.Column(db.ForeignKey(
        'marathonlauf.MarathonID'), index=True)

    marathonlauf = db.relationship(
        'Marathonlauf', primaryjoin='MarathonOrganisator.Marathon2ID == Marathonlauf.MarathonID', backref='marathon_organisators')
    organisator = db.relationship(
        'Organisator', primaryjoin='MarathonOrganisator.OrganisationID == Organisator.OrganisationID', backref='marathon_organisators')


class Marathonlauf(db.Model):
    __tablename__ = 'marathonlauf'

    MarathonID = db.Column(db.Integer, primary_key=True, unique=True)
    Preisgeld = db.Column(db.Integer)
    Kilometer = db.Column(db.Integer)
    Datum = db.Column(db.Date)
    Preis_für_Teilnahme = db.Column(db.Integer)
    Besucher = db.Column(db.String(64))


class Organisator(db.Model):
    __tablename__ = 'organisator'

    OrganisationID = db.Column(db.Integer, primary_key=True, unique=True)
    Anschrift = db.Column(db.String(64))
    Name = db.Column(db.String(64))
    Sponsoren = db.Column(db.String(64))
    Telefonnummer = db.Column(db.Integer)
