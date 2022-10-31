

from flask import jsonify
from flask_restful import Resource


class HomeResource(Resource):

    def get(self):
        return jsonify({ "message" : "home get rest api response"})
    
    def post(self):
        return jsonify({ "message" : "home post rest api response"})