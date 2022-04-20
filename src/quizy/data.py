"""Quizy database of Quizzes and ranking."""
from dataclasses import dataclass
from typing import Dict, List, Optional
from uuid import uuid4

from quizy.data_models import (
    POINTS_MULTIPLIER,
    QuizQuestion,
    QuizResult,
    QuizTest,
)


@dataclass
class QuizyData:
    """Quizy database"""

    quizzes: Dict[str, QuizTest]
    quizzes_taken: List[QuizResult]

    def get_ranking(self) -> List[QuizResult]:
        """
        Sorts ranking descending and gives it to you.

        :return:
            Sorted ranking
        """
        return sorted(
            self.quizzes_taken, key=lambda result: result.score, reverse=True
        )

    def calculate_quiz_score(
        self, quiz_uuid: str, answers: Dict[str, str]
    ) -> int:
        """
        Checks the answers and sums points for correct answers.

        :param quiz_uuid:
            Quiz UUID
        :param answers:
            Answers given by user
        :return:
            Points scored in Quiz
        """
        quiz = self.quizzes[quiz_uuid]
        multiplier = POINTS_MULTIPLIER[quiz.difficulty]
        questions = quiz.questions
        questions_points = [
            multiplier
            for key in questions
            if questions[key].correct_answer == answers[key]
        ]
        return sum(questions_points)

    def add_score_to_ranking(
        self, quiz_uuid: str, user_id: int, score: int
    ) -> None:
        """
        Add new ranking position.

        :param quiz_uuid:
            Quiz UUID
        :param user_id:
            User's ID
        :param score:
            Points scored in Quiz
        :return:
            None
        """
        quiz_result = QuizResult(uuid=quiz_uuid, user_id=user_id, score=score)
        self.quizzes_taken.append(quiz_result)

    def create_new_quiz(
        self, difficulty: str, questions: List[QuizQuestion]
    ) -> str:
        """
        Creates and adds to database new Quiz.

        :param difficulty:
            Quiz difficulty: 'easy', 'medium', 'hard'
        :param questions:
            Questions that will be in new Quiz
        :return:
            Quiz UUID
        """
        quiz_uuid = str(uuid4())
        quiz_questions = {
            str(index): question for index, question in enumerate(questions)
        }
        self.quizzes[quiz_uuid] = QuizTest(
            uuid=quiz_uuid, difficulty=difficulty, questions=quiz_questions
        )
        return quiz_uuid

    def get_quiz_questions(
        self, quiz_uuid: str
    ) -> Optional[Dict[str, QuizQuestion]]:
        """
        Retrieves Quiz questions for specified Quiz by uuid.

        :param quiz_uuid:
            Quiz UUID
        :return:
            Quiz questions for Quiz with quiz_uuid;
            None when Quiz with quiz_uuid doesn't exist.
        """
        if quiz_uuid in self.quizzes:
            return self.quizzes[quiz_uuid].questions
        return None
