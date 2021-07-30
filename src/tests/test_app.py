
def test_app_name_is_ok(app):
    assert app.name == 'validator.app'

# parametro config vem do módulo pytest-flask
def test_request_returns_404(client):
    response = client.get("/url_que_nao_existe")
    assert response.status_code == 404

# def test_request_returns_200(client):
#     response = client.get("/")
#     assert response.status_code == 200