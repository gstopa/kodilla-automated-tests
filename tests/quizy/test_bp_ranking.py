from unittest.mock import patch, MagicMock

from flask.testing import FlaskClient

from quizy.data_models import QuizResult


@patch('quizy.data.QuizyData.get_ranking')
def test_ranking_show_page_is_presented(get_ranking_mock: MagicMock, test_client: FlaskClient) -> None:
    get_ranking_mock.return_value = []
    response = test_client.get('/ranking/show')
    assert response.status_code == 200
    assert "This is the quizzes ranking!" in response.text


@patch('quizy.data.QuizyData.get_ranking')
def test_ranking_json_page_is_presented(get_ranking_mock: MagicMock, test_client: FlaskClient) -> None:
    get_ranking_mock.return_value = []
    response = test_client.get('/ranking/json')
    assert response.status_code == 200
    assert response.is_json
    assert 'ranking' in response.json


@patch('quizy.data.QuizyData.get_ranking')
def test_non_empty_ranking(get_ranking_mock: MagicMock, test_client: FlaskClient) -> None:
    ranking = [
        QuizResult(uuid='12345678-abcd-effe-dcba-876543210099', user_id=666, score=60),
        QuizResult(uuid='12345678-abcd-effe-dcba-876543210909', user_id=666, score=30),
        QuizResult(uuid='12345678-abcd-effe-dcba-876543219009', user_id=666, score=10),
    ]
    get_ranking_mock.return_value = ranking
    response = test_client.get('/ranking/json')
    assert response.status_code == 200
    assert response.is_json
    assert 'ranking' in response.json
    assert response.json['ranking'][0]['uuid'] == '12345678-abcd-effe-dcba-876543210099'
    assert response.json['ranking'][1]['uuid'] == '12345678-abcd-effe-dcba-876543210909'
    assert response.json['ranking'][2]['uuid'] == '12345678-abcd-effe-dcba-876543219009'
