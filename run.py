from app.config import app
from app.models import basemodel
from app.models import allnewsmodel
from app.models import headlinesmodel
from app.models import sourcesmodel
from app.views import externalapi
import db_create

appHost = '0.0.0.0'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8080', debug=True)