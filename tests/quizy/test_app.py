from unittest.mock import patch
import pytest
from flask import Flask
from flask.testing import FlaskClient
from quizy.app import create_app


@pytest.fixture(name='app')
def fixture_app() -> Flask:
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    yield app


@pytest.fixture(name='test_client')
def fixture_test_client(app) -> FlaskClient:
    return app.test_client()


def test_home_page_is_presented(test_client) -> None:
    response = test_client.get('/')
    assert response.status_code == 200
    assert "Those are the quizzes!" in response.text


def test_ranking_show_page_is_presented(test_client) -> None:
    response = test_client.get('/ranking/show')
    assert response.status_code == 200
    assert "This is the quizzes ranking!" in response.text


def test_ranking_json_page_is_presented(test_client) -> None:
    response = test_client.get('/ranking/json')
    assert response.status_code == 200
    assert response.is_json
    assert 'ranking' in response.json


def test_quizy_choose_page_is_presented(test_client) -> None:
    response = test_client.get('/quizy/choose')
    assert response.status_code == 200
    assert "Choose wisely!" in response.text


@patch('quizy.bp_quizy.generate_questions')
def test_quizy_create_page_redirects_to_quizy_take(generate_questions_mock, test_client, easy_quiz_questions) -> None:
    generate_questions_mock.return_value = easy_quiz_questions
    response = test_client.post('/quizy/create', data={'difficulty': 'easy'})
    assert response.status_code == 302
    assert response.location.startswith('/quizy/take/')
    response = test_client.get(response.location)
    assert response.status_code == 200
    assert "You chose wisely" in response.text


def test_quizy_create_page_redirects_to_quizy_choose_when_difficulty_is_wrong(test_client) -> None:
    response = test_client.post('/quizy/create', data={'difficulty': 'costam'})
    assert response.status_code == 302
    assert response.location.startswith('/quizy/choose')


def test_quizy_take_page_redirects_to_quizy_choose_when_uuid_does_not_exist(test_client) -> None:
    response = test_client.get('/quizy/take/6af48814-8ef6-45fd-b73f-doesnotexist')
    assert response.status_code == 302
    assert response.location.startswith('/quizy/choose')


def test_quizy_count_me_in_is_presented(test_client) -> None:
    response = test_client.post('/quizy/create', data={'difficulty': 'easy'})
    test_client.get(response.location)
    answers = {
        str(index): 'True'
        for index in range(10)
    }
    response = test_client.post('/quizy/count_me_in', data=answers)
    assert response.status_code == 200
    assert "So you have scored" in response.text


def test_non_empty_ranking(test_client) -> None:
    response = test_client.post('/quizy/create', data={'difficulty': 'easy'})
    uuid = response.location.split('/')[-1]
    test_client.get(response.location)
    answers = {
        str(index): 'True'
        for index in range(10)
    }
    test_client.post('/quizy/count_me_in', data=answers)
    response = test_client.get('/ranking/json')
    assert response.status_code == 200
    assert response.is_json
    assert 'ranking' in response.json
    assert response.json['ranking'][0]['uuid'] == uuid
