import pytest
from flask import Flask
from flask.testing import FlaskClient
from quizy.app import create_app


@pytest.fixture
def app() -> Flask:
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    yield app


@pytest.fixture
def test_client(app: Flask) -> FlaskClient:
    return app.test_client()


@pytest.fixture
def test_client_logged_in(test_client: FlaskClient) -> FlaskClient:
    response = test_client.get('/user/register')
    for line in response.text.splitlines():
        if '<input id="csrf_token" name="csrf_token" type="hidden" value="' in line:
            csrf_token = line.split('"')[-2]
    response = test_client.post('/user/register', data={
        'next': '/',
        'reg_next': '/',
        'invite_token': '',
        'csrf_token': csrf_token,
        'username': 'aaa',
        'password': 'Qw1234',
    })
    test_client.get(response.location)
    return test_client
