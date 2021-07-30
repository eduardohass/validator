import pytest
from validator.app import create_app

# cria um app validator e disponibiliza para todos os testes do módulo (scope=module)
# caso seja necessário criar um recurso (ex: app) para cada função, deve-se colocar como (scope=function)
@pytest.fixture(scope="module")
def app():
    """Instance of Main flask app"""
    return create_app()
    # app = create_app()
    # app.testing = True
    # return app