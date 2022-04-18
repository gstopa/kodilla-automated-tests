def test_ranking_show_page_is_presented(test_client) -> None:
    response = test_client.get('/ranking/show')
    assert response.status_code == 200
    assert "This is the quizzes ranking!" in response.text


def test_ranking_json_page_is_presented(test_client) -> None:
    response = test_client.get('/ranking/json')
    assert response.status_code == 200
    assert response.is_json
    assert 'ranking' in response.json


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
