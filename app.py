from flask import Flask
from models import db
from controllers.index import index_blueprint
from controllers.laufer import laufer_blueprint
from controllers.marathonlauf import marathonlauf_blueprint
from controllers.organisator import organisator_blueprint

app = Flask(__name__)
app.secret_key = "VerySecretSecretKey"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:rootroot@localhost/Marathon"

db.init_app(app)

# hier blueprint registrieren
app.register_blueprint(index_blueprint)
app.register_blueprint(laufer_blueprint)
app.register_blueprint(marathonlauf_blueprint)
app.register_blueprint(organisator_blueprint)

app.run(debug=True)
