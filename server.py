from flask import Flask, request
from flask_restful import Api, Resource

from models import Models


class AiModel(Resource):
    __models = Models()

    def get(self):
        typ = request.args.get('type')
        name = request.args.get('name')
        req = request.args.get('request')
        model = self.__models.get_model(typ, name)
        result = model.get_json_result(req)
        return result, 200


class Server:
    def __init__(self):
        self.__app = Flask(__name__)
        self.__api = Api(self.__app)
        self.__api.add_resource(AiModel, "/model", "/model/")

    def run(self):
        self.__app.run(debug=True)
