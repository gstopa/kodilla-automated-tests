import responses
from quizy.questions import generate_questions


@responses.activate
def test_generate_easy_questions(easy_questions_json, easy_quiz_questions) -> None:
    responses.add(
        responses.GET,
        'https://opentdb.com/api.php?amount=10&difficulty=easy&type=boolean',
        json=easy_questions_json,
        status=200,
    )
    assert generate_questions(difficulty='easy') == easy_quiz_questions


@responses.activate
def test_generate_medium_questions(medium_questions_json, medium_quiz_questions) -> None:
    responses.add(
        responses.GET,
        'https://opentdb.com/api.php?amount=10&difficulty=medium&type=boolean',
        json=medium_questions_json,
        status=200,
    )
    assert generate_questions(difficulty='medium') == medium_quiz_questions


@responses.activate
def test_generate_hard_questions(hard_questions_json, hard_quiz_questions) -> None:
    responses.add(
        responses.GET,
        'https://opentdb.com/api.php?amount=10&difficulty=hard&type=boolean',
        json=hard_questions_json,
        status=200,
    )
    assert generate_questions(difficulty='hard') == hard_quiz_questions
