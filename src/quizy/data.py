from typing import Dict, List, Optional
from uuid import uuid4
from quizy.data_models import QuizQuestion, QuizResult, QuizTest


POINTS_MULTIPLIER: Dict[str, int] = {
    'easy': 1,
    'medium': 3,
    'hard': 6,
}


QUIZZES: Dict[str, QuizTest] = {}
QUIZZES_TAKEN: List[QuizResult] = []


def get_ranking() -> List[QuizResult]:
    return sorted(QUIZZES_TAKEN, key=lambda result: result.score, reverse=True)


def calculate_quiz_score(quiz_uuid: str, answers: Dict[str, str]) -> int:
    quiz = QUIZZES[quiz_uuid]
    multiplier = POINTS_MULTIPLIER[quiz.difficulty]
    questions = quiz.questions
    questions_points = [
        multiplier
        for key in questions
        if questions[key].correct_answer == answers[key]
    ]
    return sum(questions_points)


def add_score_to_ranking(quiz_uuid: str, user_id: int, score: int) -> None:
    quiz_result = QuizResult(uuid=quiz_uuid, user_id=user_id, score=score)
    QUIZZES_TAKEN.append(quiz_result)


def create_new_quiz(difficulty: str, questions: List[QuizQuestion]) -> str:
    quiz_uuid = str(uuid4())
    quiz_questions = {
        str(index): question
        for index, question in enumerate(questions)
    }
    QUIZZES[quiz_uuid] = QuizTest(uuid=quiz_uuid, difficulty=difficulty, questions=quiz_questions)
    return quiz_uuid


def get_quiz_questions(uuid: str) -> Optional[Dict[str, QuizQuestion]]:
    if uuid in QUIZZES:
        return QUIZZES[uuid].questions
    return None
