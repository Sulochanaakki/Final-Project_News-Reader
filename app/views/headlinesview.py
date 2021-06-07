from flask import request, jsonify
from flask_restx import Resource, fields
import json
from app.views import externalapi
from app.config import api, isOnDev,project_dir

from app.models.headlinesmodel import HeadlineModel as TheModel
from app.schemas.headlineschema import HeadlineSchema as TheSchema
from app.const import HttpStatus,EmptyValues

#   Name of the current item/element
CURRENT_NAME = 'Headlines'


#   Namespace to route
local_ns = api.namespace('Headlines', description=CURRENT_NAME + ' related operations')

#   Database schemas
headline_schema = TheSchema()
#headline_list_schema = TheSchema(many=True)
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
                response = jsonify(externalapi.headlines())

        except Exception as e:
            response = jsonify({'message': e.__str__()})
            response.status_code = HttpStatus.INTERNAL_ERROR
        return response

    @local_ns.doc('Create an ' + CURRENT_NAME)
    @local_ns.expect(model_validator)
    #response error getting message:Not allowed
    def post(self):
        if not isOnDev:
            response = jsonify({'message': 'Not allowed'})
            response.status_code = HttpStatus.NOT_ALLOWED
            return response
        try:
            element_json = request.get_json()
            element_data = headline_schema.load(element_json)
            element_data.save_to_db()
            response = jsonify(element_data.json())
            response.status_code = HttpStatus.CREATED
        except Exception as e:
            response = jsonify({'message': e.__str__()})
            response.status_code = HttpStatus.BAD_REQUEST
        return response


@local_ns.route('/<int:id>')
class Headlines(Resource):
    @local_ns.doc('Get the ' + CURRENT_NAME + ' with the specified id',
                  params={'id': 'id of the ' + CURRENT_NAME + ' to get'})
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

    @local_ns.doc('Update an ' + CURRENT_NAME + ' with the specified id',
                  params={
                      'id': 'id of the ' + CURRENT_NAME + ' to update'})
    @local_ns.expect(model_validator)
    def put(self, id):
        #error message:Not allowed
        if not isOnDev:
            response = jsonify({'message': 'Not allowed'})
            response.status_code = HttpStatus.NOT_ALLOWED
            return response
        try:
            element_data = TheModel.find_by_id(id)

            if element_data:
                element_data.id = EmptyValues.EMPTY_STRING if request.json['id'] == EmptyValues.EMPTY_STRING else request.json['id']
                element_data.source = EmptyValues.EMPTY_STRING if request.json['source'] == EmptyValues.EMPTY_STRING else request.json['source']
                element_data.author = EmptyValues.EMPTY_STRING if request.json['author'] == EmptyValues.EMPTY_STRING else request.json['title']
                element_data.title = EmptyValues.EMPTY_STRING if request.json['title'] == EmptyValues.EMPTY_STRING else  request.json['state']
                element_data.description = EmptyValues.EMPTY_STRING if request.json['description'] == EmptyValues.EMPTY_STRING else request.json['description']
                element_data.url = EmptyValues.EMPTY_INT if request.json['url'] == EmptyValues.EMPTY_STRING else request.json['url']
                element_data.urlToImage = EmptyValues.EMPTY_INT if request.json['urlToImage'] == EmptyValues.EMPTY_STRING else request.json['UrlToImage']
                element_data.publishedAt = EmptyValues.EMPTY_INT if request.json['publishedAt'] == EmptyValues.EMPTY_STRING else request.json['publishedAt']
                element_data.content = EmptyValues.EMPTY_INT if request.json['content'] == EmptyValues.EMPTY_STRING else request.json['content']
                element_data.save_to_db()
                response = jsonify(element_data.json())
                response.status_code = HttpStatus.CREATED
            else:
                response = jsonify({'message': CURRENT_NAME + ' not found.'})
                response.status_code = HttpStatus.NOT_FOUND
        except Exception as e:
            response = jsonify({'message': e.__str__()})
            response.status_code = HttpStatus.BAD_REQUEST
        return response

    @local_ns.doc('Delete an ' + CURRENT_NAME + ' with the specified id',
                  params={
                      'id': 'id of the ' + CURRENT_NAME + ' to delete'})
    def delete(self, id):
        #error message:Not allowed
        if not isOnDev:
            response = jsonify({'message': 'Not allowed'})
            response.status_code = HttpStatus.NOT_ALLOWED
            return response
        try:
            element_data = TheModel.find_by_id(id)
            if element_data:
                element_data.delete_from_db()
                response = jsonify({'message': CURRENT_NAME + ' deleted.'})
                response.status_code = HttpStatus.OK
            else:
                response = jsonify({'message': CURRENT_NAME + ' not found.'})
                response.status_code = HttpStatus.NOT_FOUND
        except Exception as e:
            response = jsonify({'message': e.__str__()})
            response.status_code = HttpStatus.INTERNAL_ERROR
        return response






