#!/usr/bin/env python

from flask import Flask

from flask.ext.pymongo import PyMongo
from views import views

from models import MockArticle as Article

def create_app():
    app = Flask('collopyprobr')
    db = PyMongo(app)
    app.register_blueprint(views)
    return app

app = create_app()


if __name__ == '__main__':
    app.debug = True
    app.run()
