from flask import request, jsonify
from flask_restx import Resource, fields
import json
from app.config import api, isOnDev, project_dir
from app.externalapi import *

from app.models.sourcesmodel  import SourceModel as TheModel
from app.schemas.sourceschema import SourceSchema as TheSchema
from app.const import HttpStatus, EmptyValues

#   Name of the current item/element
CURRENT_NAME = 'Sources'


#   Namespace to route
local_ns = api.namespace('Sources', description=CURRENT_NAME + ' related operations')

#   Database schemas
source_schema = TheSchema()
#headline_list_schema = TheSchema(many=True)
#   Model required by flask_restx for expect on POST and PUT methods
model_validator = local_ns.model(CURRENT_NAME, {
            'headlines_id': fields.Integer,
            'allnews_id': fields.Integer,
            'name': fields.String,
            'description': fields.String,
            'url': fields.String,
            'category': fields.String,
            'language': fields.String,
            'country': fields.String
})

@local_ns.route('/')
class SourcesList(Resource):
    @local_ns.doc('Get all the' +CURRENT_NAME+ 's')
    def get(self):
        try:
            if isOnDev:
                response = jsonify(TheModel.find_all())
                response.status_code = HttpStatus.OK


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
            element_data = source_schema.load(element_json)
            element_data.save_to_db()
            response = jsonify(element_data.json())
            response.status_code = HttpStatus.CREATED
        except Exception as e:
            response = jsonify({'message': e.__str__()})
            response.status_code = HttpStatus.BAD_REQUEST
        return response


@local_ns.route('/<int:id>')
class Sources(Resource):
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
                #element_data.headlines_id = EmptyValues.EMPTY_STRING if request.json['headlines_id'] == EmptyValues.EMPTY_STRING else request.json['headlines_id']
                #element_data.allnews_id = EmptyValues.EMPTY_STRING if request.json['allnews_id'] == EmptyValues.EMPTY_STRING else request.json['allnews_id']
                element_data.name = EmptyValues.EMPTY_STRING if request.json['name'] == EmptyValues.EMPTY_STRING else request.json['name']
                element_data.description = EmptyValues.EMPTY_STRING if request.json['description'] == EmptyValues.EMPTY_STRING else request.json['description']
                element_data.url = EmptyValues.EMPTY_INT if request.json['url'] == EmptyValues.EMPTY_STRING else request.json['url']
                element_data.category = EmptyValues.EMPTY_INT if request.json['category'] == EmptyValues.EMPTY_STRING else request.json['category ']
                element_data.language = EmptyValues.EMPTY_INT if request.json['language'] == EmptyValues.EMPTY_STRING else request.json['language']
                element_data.country = EmptyValues.EMPTY_INT if request.json['country'] == EmptyValues.EMPTY_STRING else request.json['country']
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

@local_ns.route('/<country>')
class SourcesCountry(Resource):
    @local_ns.doc('Get the ' + CURRENT_NAME + ' with the specified id',
                  params={'country': 'country of the ' + CURRENT_NAME + ' to get'})
    def get(self, country):
        try:
            element_data = TheModel.find_by_country(country)
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


''''@local_ns.doc('Create an external api ' + CURRENT_NAME)
class ExrernalNews:
    #@local_ns.expect(model_validator)
    # response error getting message:Not allowed
    def post(self):
        if not isOnDev:
            response = jsonify({'message': 'Not allowed'})
            response.status_code = HttpStatus.NOT_ALLOWED
            return response
        try:
            # make the api call
            element_json  = request.get_json()
            element_data = source_schema.load(element_json)
            element_data.save_to_db()
            response = jsonify(element_data.json())
            response.status_code = HttpStatus.CREATED
        except Exception as e:
            response = jsonify({'message': e.__str__()})
            response.status_code = HttpStatus.BAD_REQUEST
        return response'''
