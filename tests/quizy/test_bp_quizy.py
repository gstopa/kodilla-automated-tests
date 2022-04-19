from typing import List
from unittest.mock import patch, MagicMock

from flask.testing import FlaskClient

from quizy.data_models import QuizQuestion


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


@patch('quizy.data.QuizyData.create_new_quiz')
@patch('quizy.bp_quizy.generate_questions')
def test_quizy_create_page_redirects_to_quizy_take(
        generate_questions_mock: MagicMock,
        create_new_quiz_mock: MagicMock,
        test_client_logged_in: FlaskClient,
        easy_quiz_questions: List[QuizQuestion],
) -> None:
    generate_questions_mock.return_value = easy_quiz_questions
    create_new_quiz_mock.return_value = '12345678-abcd-effe-dcba-876543210099'
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


def test_quizy_take_page_redirects_to_sign_in_when_not_logged_in(test_client: FlaskClient) -> None:
    response = test_client.get('/quizy/take/12345678-abcd-effe-dcba-876543210099')
    assert response.status_code == 302
    assert response.location.startswith('/user/sign-in')


@patch('quizy.data.QuizyData.get_quiz_questions')
def test_quizy_take_page_redirects_to_quizy_choose_when_uuid_does_not_exist(
        get_quiz_questions_mock: MagicMock,
        test_client_logged_in: FlaskClient,
) -> None:
    get_quiz_questions_mock.return_value = None
    response = test_client_logged_in.get('/quizy/take/6af48814-8ef6-45fd-b73f-doesnotexist')
    assert response.status_code == 302
    assert response.location.startswith('/quizy/choose')


@patch('quizy.data.QuizyData.get_quiz_questions')
def test_quizy_take_page_is_presented(
        get_quiz_questions_mock: MagicMock,
        test_client_logged_in: FlaskClient,
        easy_quiz_questions: List[QuizQuestion],
) -> None:
    get_quiz_questions_mock.return_value = {
        str(index): question
        for index, question in enumerate(easy_quiz_questions)
    }
    response = test_client_logged_in.get(f'/quizy/take/12345678-abcd-effe-dcba-876543210099')
    assert response.status_code == 200
    assert 'You chose wisely' in response.text


def test_quizy_count_me_in_page_redirects_to_sign_in_when_not_logged_in(test_client: FlaskClient) -> None:
    answers = {
        str(index): 'True'
        for index in range(10)
    }
    response = test_client.post('/quizy/count_me_in', data=answers)
    assert response.status_code == 302
    assert response.location.startswith('/user/sign-in')


@patch('quizy.data.QuizyData.calculate_quiz_score')
def test_quizy_count_me_in_page_post_redirects_to_get(
        calculate_quiz_score_mock: MagicMock,
        test_client_logged_in: FlaskClient,
) -> None:
    uuid = '12345678-abcd-effe-dcba-876543210099'
    calculate_quiz_score_mock.return_value = 6
    answers = {
        str(index): 'True'
        for index in range(10)
    }
    with test_client_logged_in.session_transaction() as session:
        session['quiz_uuid'] = uuid
    with patch('quizy.data.QuizyData.add_score_to_ranking'):
        response = test_client_logged_in.post('/quizy/count_me_in', data=answers)
    assert response.status_code == 302
    assert response.location.startswith(f'/quizy/count_me_in/{uuid}/6')


def test_quizy_count_me_in_page_is_presented(test_client_logged_in: FlaskClient) -> None:
    uuid = '12345678-abcd-effe-dcba-876543210099'
    response = test_client_logged_in.get(f'/quizy/count_me_in/{uuid}/6')
    assert response.status_code == 200
    assert f'So you have scored 6 points in quiz {uuid}' in response.text
