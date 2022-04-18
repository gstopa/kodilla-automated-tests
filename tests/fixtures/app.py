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
def test_client(app) -> FlaskClient:
    return app.test_client()
