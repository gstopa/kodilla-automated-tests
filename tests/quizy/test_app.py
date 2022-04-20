def test_home_page_is_presented(test_client) -> None:
    response = test_client.get('/')
    assert response.status_code == 200
    assert "Those are the quizzes!" in response.text
