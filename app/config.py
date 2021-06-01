import os
from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

#   Configure for local test
#   This works with SQLite3
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "newsdatabase.sqlite"))

# Config app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
#application.config['JSON_AS_ASCII'] = False

db = SQLAlchemy(app)

api = Api(app,
          title='News Reader',
          description='API of information about latest news')
