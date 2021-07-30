# from dynaconf import FlaskDynaconf
from os import environ

def init_app(app):
    # FlaskDynaconf(app)
    # app.config.load_extensions("EXTENSIONS")
    app.config['SECRET_KEY'] = environ.get("SECRET_KEY")
    app.config['FLASK_ADMIN_SWATCH'] = "flatly" #bootswatch para os templates
    app.config["DB_DATABASE_URI"] = environ.get("DB_DATABASE_URI") # "mongodb://root:hass123@mongodb:27017"
    app.config["DB_DATABASE_NAME"] = environ.get("DB_DATABASE_NAME") # "db_validator"

    if app.debug:
        app.config["DEBUG_TB_TEMPLATE_EDITOR_ENABLED"] = True
        app.config["DEBUG_TB_PROFILER_ENABLED"] = True
        # app.config['DEBUG_TB_PROFILER_ENABLED'] = True
        # app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True
        # app.config['DEBUG_TB_HOSTS'] = True
        # app.config['DEBUG_TB_ENABLED'] = True
        
