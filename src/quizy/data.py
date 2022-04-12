from typing import Dict, List
from uuid import uuid4
from quizy.data_models import QuizResult, QuizTest


POINTS_MULTIPLIER: Dict[str, int] = {
    'easy': 1,
    'medium': 3,
    'hard': 6,
}


QUIZZES: Dict[str, QuizTest] = {}
QUIZZES_TAKEN: List[QuizResult] = []


def get_ranking(sort: bool = True, reverse: bool = True) -> list:
    ranking = QUIZZES_TAKEN
    if sort:
        ranking = sorted(QUIZZES_TAKEN, key=lambda result: result.score, reverse=reverse)
    return ranking


def calculate_quiz_score(quiz_uuid, answers):
    quiz = QUIZZES[quiz_uuid]
    multiplier = POINTS_MULTIPLIER[quiz.difficulty]
    questions = quiz.questions
    questions_points = [
        multiplier
        for key in questions
        if questions[key].correct_answer == answers[key]
    ]
    return sum(questions_points)


def add_score_to_ranking(quiz_uuid, user_id, score):
    quiz_result = QuizResult(uuid=quiz_uuid, user_id=user_id, score=score)
    QUIZZES_TAKEN.append(quiz_result)


def create_new_quiz(difficulty, questions) -> str:
    quiz_uuid = str(uuid4())
    quiz_questions = {
        str(index): question
        for index, question in enumerate(questions)
    }
    QUIZZES[quiz_uuid] = QuizTest(uuid=quiz_uuid, difficulty=difficulty, questions=quiz_questions)
    return quiz_uuid


def get_quiz_questions(uuid):
    if uuid in QUIZZES:
        return QUIZZES[uuid].questions
    return None
