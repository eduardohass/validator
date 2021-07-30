from validator.ext.auth import models # noqa
# from validator.ext.auth.commands import list_users, add_user

from validator.ext.admin import admin
from validator.ext.auth.admin import UserAdmin

def init_app(app):
    """TODO: Inicializar Flask Simple Login + JWT"""
    # app.cli.command()(list_users)

    # admin.add_view(UserAdmin(UserAdmin, ))
