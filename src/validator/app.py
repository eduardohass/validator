import logging as log
from flask import Flask

from validator.ext import config
from validator.ext import site
from validator.ext import toolbar
from validator.ext import db
from validator.ext import cli
from validator.ext import admin
# from validator.rule import views


log.basicConfig(level=log.DEBUG, format="%(asctime)s %(levelname)s:\n%(message)s\n")


def create_app():
    """Factory Padrão"""
    log.info('[create_app]')
    app = Flask(__name__)
    config.init_app(app)
    db.init_app(app)
    #admin.init_app(app)
    cli.init_app(app) 
    toolbar.init_app(app)
    site.init_app(app)
    return app


# if __name__ == "__main__":
#     app = create_app()
#     app.run(host='0.0.0.0', debug=True)

