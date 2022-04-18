from dataclasses import dataclass
from typing import Dict, List, Optional
from uuid import uuid4

from flask import Flask

from quizy.data_models import POINTS_MULTIPLIER, QuizQuestion, QuizResult, QuizTest


@dataclass
class QuizyData:
    quizzes: Dict[str, QuizTest]
    quizzes_taken: List[QuizResult]

    def get_ranking(self) -> List[QuizResult]:
        return sorted(self.quizzes_taken, key=lambda result: result.score, reverse=True)

    def calculate_quiz_score(self, quiz_uuid: str, answers: Dict[str, str]) -> int:
        quiz = self.quizzes[quiz_uuid]
        multiplier = POINTS_MULTIPLIER[quiz.difficulty]
        questions = quiz.questions
        questions_points = [
            multiplier
            for key in questions
            if questions[key].correct_answer == answers[key]
        ]
        return sum(questions_points)

    def add_score_to_ranking(self, quiz_uuid: str, user_id: int, score: int) -> None:
        quiz_result = QuizResult(uuid=quiz_uuid, user_id=user_id, score=score)
        self.quizzes_taken.append(quiz_result)

    def create_new_quiz(self, difficulty: str, questions: List[QuizQuestion]) -> str:
        quiz_uuid = str(uuid4())
        quiz_questions = {
            str(index): question
            for index, question in enumerate(questions)
        }
        self.quizzes[quiz_uuid] = QuizTest(uuid=quiz_uuid, difficulty=difficulty, questions=quiz_questions)
        return quiz_uuid

    def get_quiz_questions(self, quiz_uuid: str) -> Optional[Dict[str, QuizQuestion]]:
        if quiz_uuid in self.quizzes:
            return self.quizzes[quiz_uuid].questions
        return None


def init_app(app: Flask) -> None:
    app.config['QuizyData'] = QuizyData(quizzes={}, quizzes_taken=[])
