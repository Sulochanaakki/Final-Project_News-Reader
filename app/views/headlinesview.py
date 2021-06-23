from flask import request, jsonify
from flask_restx import Resource, fields
import json
from app.config import api, isOnDev,project_dir

from app.models.headlinesmodel import HeadlineModel as TheModel
from app.schemas.headlineschema import HeadlineSchema as TheSchema
from app.const import HttpStatus,EmptyValues

#   Name of the current item/element
CURRENT_NAME = 'Headlines'
CACHE_FILE = "/db/newsheadlines.json"

#   Namespace to route
local_ns = api.namespace('headline', description=CURRENT_NAME + ' related operations')

#   Database schemas
local_schema = TheSchema()
#   Model required by flask_restx for expect on POST and PUT methods
model_validator = local_ns.model(CURRENT_NAME, {
    'id': fields.Integer,
    'source': fields.String,
    'author': fields.String,
    'title': fields.String,
    'description': fields.String,
    'url' : fields.String,
    'urlToImage':  fields.String,
    'publishedAt': fields.String,
    'content': fields.String
})

@local_ns.route('/')
class HeadlinesList(Resource):
    @local_ns.doc('Get all the' +CURRENT_NAME+ 's')
    def get(self):
        try:
            if isOnDev:
                response = jsonify(TheModel.find_all())
                response.status_code = HttpStatus.OK
            else:
               f = open(project_dir + CACHE_FILE, "r")
               data_json = json.loads(f.read())
               f.close()
               response = jsonify(data_json)
               #print(data_json)
            response.status_code = HttpStatus.OK

        except Exception as e:
            response = jsonify({'message': e.__str__()})
            response.status_code = HttpStatus.INTERNAL_ERROR
        return response

    @local_ns.doc('Create an ' + CURRENT_NAME)
    @local_ns.expect(model_validator)
    def post(self):
        if not isOnDev:
            response = jsonify({'message': 'Not allowed'})
            response.status_code = HttpStatus.NOT_ALLOWED
            return response
        try:
            element_json = request.get_json()
            element_data = local_schema.load(element_json)
            element_data.save()
            response = jsonify(element_data.json())
            response.status_code = HttpStatus.CREATED
        except Exception as e:
            response = jsonify({'message': e.__str__()})
            response.status_code = HttpStatus.BAD_REQUEST
        return response

    @local_ns.route('/<int:id>')
    class Headlines(Resource):
        @local_ns.doc('Get the ' + CURRENT_NAME + ' with the specified id',
                      params={
                          'id': 'id of the ' + CURRENT_NAME + ' to get'
                      })
        def get(self, id):
            try:
                element_data = TheModel.find_by_id(id)
                if element_data:
                    response = jsonify(element_data.json())
                    response.status_code = HttpStatus.OK
                else:
                    response = jsonify({'message': CURRENT_NAME + ' not found.'})
                    response.status_code = HttpStatus.NOT_FOUND
            except Exception as e:
                response = jsonify({'message': e.__str__()})
                response.status_code = HttpStatus.INTERNAL_ERROR
            return response
