import os
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

#   Configure for local test
#   This works with SQLite3
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "db/newsdatabase.sqlite"))

# Config app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['JSON_AS_ASCII'] = False


db = SQLAlchemy(app)
ma = Marshmallow(app)

@app.before_first_request
def create_tables():
    db.create_all()

isOnDev = True
app.debug = isOnDev

api = Api(app,
          title='News Reader',
          description='API of information about latest news')


from app.models import allnewsmodel
from app.models import headlinesmodel
from app.models import sourcesmodel
from app.views import externalapi
#import db_create
from app.schemas import headlineschema

from app.views import externalapi
from app.views.headlinesview import HeadlinesList, Headlines
from app.views.allnewsview import AllNewsList, AllNews
from app.views.sourcesview import SourcesList, Sources
