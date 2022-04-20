from typing import List, Dict

import pytest
from pytest_lazyfixture import lazy_fixture

from quizy.data import QuizyData
from quizy.data_models import QuizQuestion


@pytest.fixture(name='quizy_data')
def fixture_quizy_data() -> QuizyData:
    return QuizyData(quizzes={}, quizzes_taken=[])


def test_new_quizy_data_has_empty_ranking(quizy_data: QuizyData) -> None:
    ranking = quizy_data.get_ranking()
    assert len(ranking) == 0


def test_after_adding_a_score_ranking_is_not_empty(quizy_data: QuizyData) -> None:
    quizy_data.add_score_to_ranking(quiz_uuid='12345678-abcd-effe-dcba-876543210099', user_id=666, score=6)
    ranking = quizy_data.get_ranking()
    assert len(ranking) == 1
    quizy_data.add_score_to_ranking(quiz_uuid='12345678-abcd-effe-dcba-876543210909', user_id=666, score=6)
    quizy_data.add_score_to_ranking(quiz_uuid='12345678-abcd-effe-dcba-876543219009', user_id=666, score=6)
    ranking = quizy_data.get_ranking()
    assert len(ranking) == 3


def test_new_quizy_data_has_no_quizzes(quizy_data: QuizyData) -> None:
    quiz_questions = quizy_data.get_quiz_questions(quiz_uuid='12345678-abcd-effe-dcba-876543210099')
    assert quiz_questions is None


def test_after_creating_quiz_can_get_its_questions(
        quizy_data: QuizyData,
        easy_quiz_questions: List[QuizQuestion],
) -> None:
    uuid = quizy_data.create_new_quiz('easy', easy_quiz_questions)
    quiz_questions = quizy_data.get_quiz_questions(quiz_uuid=uuid)
    assert easy_quiz_questions == list(quiz_questions.values())


@pytest.mark.parametrize(
    'easy_quiz_answers,expected_score',
    [
        (lazy_fixture('easy_quiz_answers_all_correct'), 10),
        (lazy_fixture('easy_quiz_answers_all_incorrect'), 0),
        (lazy_fixture('easy_quiz_answers_five_correct'), 5),
    ],
)
def test_calculate_easy_quiz_score(
        quizy_data: QuizyData,
        easy_quiz_questions: List[QuizQuestion],
        easy_quiz_answers: Dict[str, str],
        expected_score: int
) -> None:
    uuid = quizy_data.create_new_quiz(difficulty='easy', questions=easy_quiz_questions)
    score = quizy_data.calculate_quiz_score(quiz_uuid=uuid, answers=easy_quiz_answers)
    assert score == expected_score


@pytest.mark.parametrize(
    'medium_quiz_answers,expected_score',
    [
        (lazy_fixture('medium_quiz_answers_all_correct'), 30),
        (lazy_fixture('medium_quiz_answers_all_incorrect'), 0),
        (lazy_fixture('medium_quiz_answers_five_correct'), 15),
    ],
)
def test_calculate_medium_quiz_score(
        quizy_data: QuizyData,
        medium_quiz_questions: List[QuizQuestion],
        medium_quiz_answers: Dict[str, str],
        expected_score: int
) -> None:
    uuid = quizy_data.create_new_quiz(difficulty='medium', questions=medium_quiz_questions)
    score = quizy_data.calculate_quiz_score(quiz_uuid=uuid, answers=medium_quiz_answers)
    assert score == expected_score


@pytest.mark.parametrize(
    'hard_quiz_answers,expected_score',
    [
        (lazy_fixture('hard_quiz_answers_all_correct'), 60),
        (lazy_fixture('hard_quiz_answers_all_incorrect'), 0),
        (lazy_fixture('hard_quiz_answers_five_correct'), 30),
    ],
)
def test_calculate_hard_quiz_score(
        quizy_data: QuizyData,
        hard_quiz_questions: List[QuizQuestion],
        hard_quiz_answers: Dict[str, str],
        expected_score: int
) -> None:
    uuid = quizy_data.create_new_quiz(difficulty='hard', questions=hard_quiz_questions)
    score = quizy_data.calculate_quiz_score(quiz_uuid=uuid, answers=hard_quiz_answers)
    assert score == expected_score
