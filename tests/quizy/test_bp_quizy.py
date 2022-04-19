from typing import List, Dict
from unittest.mock import patch, MagicMock

import pytest
from flask import Flask
from flask.testing import FlaskClient

from quizy.data import QuizyData
from quizy.data_models import QuizQuestion, QuizTest, QuizResult


@pytest.fixture(name='quizzes')
def fixture_quizzes(
        app: Flask,
        easy_quiz_questions: List[QuizQuestion],
        medium_quiz_questions: List[QuizQuestion],
        hard_quiz_questions: List[QuizQuestion],
) -> Dict[str, QuizTest]:
    def indexed_questions(questions):
        return {
            str(index): question
            for index, question in enumerate(questions)
        }
    quizzes = {
        '12345678-abcd-effe-dcba-876543210099': QuizTest(
            uuid='12345678-abcd-effe-dcba-876543210099',
            difficulty='easy',
            questions=indexed_questions(easy_quiz_questions),
        ),
        '12345678-abcd-effe-dcba-876543210909': QuizTest(
            uuid='12345678-abcd-effe-dcba-876543210909',
            difficulty='medium',
            questions=indexed_questions(medium_quiz_questions),
        ),
        '12345678-abcd-effe-dcba-876543219009': QuizTest(
            uuid='12345678-abcd-effe-dcba-876543219009',
            difficulty='hard',
            questions=indexed_questions(hard_quiz_questions),
        ),
    }
    app.config['QuizyData'] = QuizyData(quizzes=quizzes, quizzes_taken=[])
    return quizzes


def test_quizy_choose_page_redirects_to_sign_in_when_not_logged_in(test_client: FlaskClient) -> None:
    response = test_client.get('/quizy/choose')
    assert response.status_code == 302
    assert response.location.startswith('/user/sign-in')


def test_quizy_choose_page_is_presented(test_client_logged_in: FlaskClient) -> None:
    response = test_client_logged_in.get('/quizy/choose')
    assert response.status_code == 200
    assert 'Choose wisely!' in response.text


def test_quizy_create_page_redirects_to_sign_in_when_not_logged_in(test_client: FlaskClient) -> None:
    response = test_client.post('/quizy/create', data={'difficulty': 'easy'})
    assert response.status_code == 302
    assert response.location.startswith('/user/sign-in')


@patch('quizy.bp_quizy.generate_questions')
def test_quizy_create_page_redirects_to_quizy_take(
        generate_questions_mock: MagicMock,
        test_client_logged_in: FlaskClient,
        easy_quiz_questions: List[QuizQuestion],
        quizzes: Dict[str, QuizTest],
) -> None:
    generate_questions_mock.return_value = easy_quiz_questions
    response = test_client_logged_in.post('/quizy/create', data={'difficulty': 'easy'})
    assert response.status_code == 302
    assert response.location.startswith('/quizy/take/')


@patch('quizy.bp_quizy.generate_questions')
def test_quizy_create_page_redirects_to_quizy_choose_when_difficulty_is_wrong(
        generate_questions_mock: MagicMock,
        test_client_logged_in: FlaskClient,
) -> None:
    generate_questions_mock.side_effect = [ValueError]
    response = test_client_logged_in.post('/quizy/create', data={'difficulty': 'costam'})
    assert response.status_code == 302
    assert response.location.startswith('/quizy/choose')


@patch('quizy.bp_quizy.generate_questions')
def test_quizy_create_page_redirects_to_quizy_choose_when_opentdb_not_accessible(
        generate_questions_mock: MagicMock,
        test_client_logged_in: FlaskClient,
) -> None:
    generate_questions_mock.side_effect = [ConnectionError]
    response = test_client_logged_in.post('/quizy/create', data={'difficulty': 'easy'})
    assert response.status_code == 302
    assert response.location.startswith('/error/opentdb')


def test_quizy_take_page_redirects_to_sign_in_when_not_logged_in(
        test_client: FlaskClient,
        quizzes: Dict[str, QuizTest],
) -> None:
    uuid = list(quizzes.keys())[-1]
    response = test_client.get(f'/quizy/take/{uuid}')
    assert response.status_code == 302
    assert response.location.startswith('/user/sign-in')


def test_quizy_take_page_redirects_to_quizy_choose_when_uuid_does_not_exist(
        test_client_logged_in: FlaskClient,
        quizzes: Dict[str, QuizTest],
) -> None:
    response = test_client_logged_in.get('/quizy/take/6af48814-8ef6-45fd-b73f-doesnotexist')
    assert response.status_code == 302
    assert response.location.startswith('/quizy/choose')


def test_quizy_take_page_is_presented(test_client_logged_in: FlaskClient, quizzes: Dict[str, QuizTest]) -> None:
    response = test_client_logged_in.get(f'/quizy/take/12345678-abcd-effe-dcba-876543210099')
    assert response.status_code == 200
    assert 'You chose wisely' in response.text


def test_quizy_count_me_in_page_redirects_to_sign_in_when_not_logged_in(
        test_client: FlaskClient,
        easy_quiz_answers_all_correct: Dict[str, str],
) -> None:
    response = test_client.post('/quizy/count_me_in', data=easy_quiz_answers_all_correct)
    assert response.status_code == 302
    assert response.location.startswith('/user/sign-in')


def test_quizy_count_me_in_page_post_redirects_to_get(
        test_client_logged_in: FlaskClient,
        quizzes: Dict[str, QuizTest],
        easy_quiz_answers_all_correct: Dict[str, str],
) -> None:
    uuid = '12345678-abcd-effe-dcba-876543210099'
    with test_client_logged_in.session_transaction() as session:
        session['quiz_uuid'] = uuid
    response = test_client_logged_in.post('/quizy/count_me_in', data=easy_quiz_answers_all_correct)
    assert response.status_code == 302
    assert response.location.startswith(f'/quizy/count_me_in/{uuid}/10')


def test_quizy_count_me_in_page_is_presented(test_client_logged_in: FlaskClient) -> None:
    uuid = '12345678-abcd-effe-dcba-876543210099'
    response = test_client_logged_in.get(f'/quizy/count_me_in/{uuid}/10')
    assert response.status_code == 200
    assert f'So you have scored 10 points in quiz {uuid}' in response.text
