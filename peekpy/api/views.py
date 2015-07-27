# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify
from flask.views import MethodView

from .exception import APIException

api = Blueprint('api', __name__, url_prefix='/api')


#Register the api exception handler
@api.errorhandler(APIException)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


class FolderAPI(MethodView):

    def get(self):
        return "<h1> GET method</h1>"

    def post(self):
        return "<h1> POST method</h1>"

#Register the method view
api.add_url_rule('/f/', view_func=FolderAPI.as_view('folder'))
