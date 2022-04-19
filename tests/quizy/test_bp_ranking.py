from unittest.mock import patch, MagicMock

import pytest
from flask import Flask
from flask.testing import FlaskClient

from quizy.data import QuizyData
from quizy.data_models import QuizResult


@pytest.fixture(name='test_client_with_ranking')
def fixture_test_client_with_ranking(app: Flask) -> FlaskClient:
    quizzes_taken = [
        QuizResult(uuid='12345678-abcd-effe-dcba-876543219009', user_id=666, score=10),
        QuizResult(uuid='12345678-abcd-effe-dcba-876543210099', user_id=666, score=60),
        QuizResult(uuid='12345678-abcd-effe-dcba-876543210909', user_id=666, score=30),
    ]
    app.config['QuizyData'] = QuizyData(quizzes={}, quizzes_taken=quizzes_taken)
    return app.test_client()


def test_ranking_show_page_is_presented(test_client_with_ranking: FlaskClient) -> None:
    response = test_client_with_ranking.get('/ranking/show')
    assert response.status_code == 200
    assert 'This is the quizzes ranking!' in response.text
    assert '12345678-abcd-effe-dcba-876543219009' in response.text
    assert '12345678-abcd-effe-dcba-876543210099' in response.text
    assert '12345678-abcd-effe-dcba-876543210909' in response.text


def test_non_empty_ranking(test_client_with_ranking: FlaskClient) -> None:
    response = test_client_with_ranking.get('/ranking/json')
    assert response.status_code == 200
    assert response.is_json
    assert 'ranking' in response.json
    assert len(response.json['ranking']) == 3
    assert response.json['ranking'][0]['uuid'] == '12345678-abcd-effe-dcba-876543210099'
    assert response.json['ranking'][1]['uuid'] == '12345678-abcd-effe-dcba-876543210909'
    assert response.json['ranking'][2]['uuid'] == '12345678-abcd-effe-dcba-876543219009'
