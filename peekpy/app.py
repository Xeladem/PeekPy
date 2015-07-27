# -*- coding: utf-8 -*-

from flask import Flask, render_template

from .api import api
from .admin import admin
from .website import website

from .utils import INSTANCE_FOLDER_PATH

# For import *
__all__ = ['init_app']

DEFAULT_BLUEPRINTS = (
    api,
    admin,
    website
)


def init_app(config=None, app_name=None, blueprints=None):
    """ Initiate the peekpy app """
    if app_name is None:
        app_name = DefaultConfig.PROJECT
    if blueprints is None:
        blueprints = DEFAULT_BLUEPRINTS

    app = Flask(app_name,
                instance_path=INSTANCE_FOLDER_PATH,
                instance_relative_config=True)

    #Register the blueprints
    register_blueprints(app, blueprints)

    #Initiate the error handlers
    init_error_handlers(app)

    return app


def init_error_handlers(app):
    """ Init the various error handlers"""

    @app.errorhandler(403)
    def forbidden_page(error):
        return render_template("errors/forbidden_page.html"), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("errors/page_not_found.html"), 404

    @app.errorhandler(500)
    def server_error_page(error):
        return render_template("errors/server_error.html"), 500


def register_blueprints(app, blueprints):
    """ Register the blueprints in the Flask app object"""

    for bp in blueprints:
        app.register_blueprints(bp)