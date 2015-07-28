# -*- coding: utf-8 -*-
import shortuuid

from flask import Blueprint, jsonify, redirect, request
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

    def get(self, folder_id, link_id):
        #Generate random id and redirect
        #if no folder name is provided
        if folder_id is None:
            #Generate a shortUUID and redirect to the new folder
            rand_fid = shortuuid.ShortUUID().random(length=6)
            new_url = request.url + rand_fid
            return redirect(new_url, code=303)
        else:
            return "<h1> Create or load folder</h1>"

    def post(self, folder_id, link_id):
        return "<h1> POST method</h1>"


class LinksAPI(MethodView):

    def get(self, folder_id, link_id):
        if link_id is None:
            return "<h1> print links <h1>"
        else:
            return "<h1> create a link <h1>"

    def post(self, folder_id, link_id):
        return "<h1> POST links method</h1>"

#Register the method view
folder_view = FolderAPI.as_view('folder')
links_view = LinksAPI.as_view('links')

api.add_url_rule('/f/',
                 view_func=folder_view,
                 methods=['GET', 'POST'],
                 defaults={'folder_id': None,
                           'link_id': None})

api.add_url_rule('/f/<string:folder_id>',
                 view_func=folder_view,
                 methods=['GET', 'PATCH', 'PUT', 'DELETE'],
                 defaults={'link_id': None})

api.add_url_rule('/f/<string:folder_id>/l/',
                 view_func=links_view,
                 methods=['POST', 'GET'],
                 defaults={'link_id': None})

api.add_url_rule('/f/<string:folder_id>/l/<string:link_id>',
                 view_func=links_view,
                 methods=['GET', 'PATCH', 'PUT', 'DELETE'])