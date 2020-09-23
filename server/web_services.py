#!/usr/bin/env python3

"""
web_services.py

Flask methods to implement online game

Author: Dr. Andreas Janzen, janzen@gmx.net
Date: 2020-09-23
"""


import db_services
import flask


app = flask.Flask(__name__)


def build_views(app)
    @app.route("/")
    def index():
        return "Hello world!"

    @app.errorhandler(404)
    def not_found():
        return flask.Response("The page was not found.", status=404)


def run_web_app():
    app.run(debug=True)
