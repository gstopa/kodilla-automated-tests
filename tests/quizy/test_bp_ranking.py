from typing import List

import pytest
from flask import Flask
from flask.testing import FlaskClient

from quizy.data import QuizyData
from quizy.data_models import QuizResult


@pytest.fixture(name='ranking')
def fixture_ranking(app: Flask) -> List[QuizResult]:
    quizzes_taken = [
        QuizResult(uuid='12345678-abcd-effe-dcba-876543210099', user_id=666, score=60),
        QuizResult(uuid='12345678-abcd-effe-dcba-876543210909', user_id=666, score=30),
        QuizResult(uuid='12345678-abcd-effe-dcba-876543219009', user_id=666, score=10),
    ]
    app.config['QuizyData'] = QuizyData(quizzes={}, quizzes_taken=quizzes_taken)
    return quizzes_taken


def test_ranking_show_page_is_presented(test_client: FlaskClient, ranking: List[QuizResult]) -> None:
    response = test_client.get('/ranking/show')
    assert response.status_code == 200
    assert 'This is the quizzes ranking!' in response.text
    assert ranking[0].uuid in response.text
    assert ranking[1].uuid in response.text
    assert ranking[2].uuid in response.text


def test_non_empty_ranking(test_client: FlaskClient, ranking: List[QuizResult]) -> None:
    response = test_client.get('/ranking/json')
    assert response.status_code == 200
    assert response.is_json
    assert 'ranking' in response.json
    assert len(response.json['ranking']) == 3
    assert response.json['ranking'][0]['uuid'] == ranking[0].uuid
    assert response.json['ranking'][1]['uuid'] == ranking[1].uuid
    assert response.json['ranking'][2]['uuid'] == ranking[2].uuid
