from flask_admin import Admin

admin = Admin()

def init_app(app):
    admin.name = app.config.get("ADMIN_APP_NAME","Validator App")
    admin.template_mode = app.config.get("ADMIN_TEMPLATE_MODE", "bootstrap2")
    admin.init_app(app)