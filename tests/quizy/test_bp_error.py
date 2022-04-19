from flask.testing import FlaskClient


def test_error_opentdb_page(test_client: FlaskClient) -> None:
    response = test_client.get('/error/opentdb')
    assert response.status_code == 200
    assert 'Open Trivia Database is not accessible at the moment!' in response.text
    assert 'Please try again later!' in response.text
