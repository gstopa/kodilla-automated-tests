from typing import List
from requests import get
from quizy.data_models import QuizQuestion


def generate_questions(difficulty: str) -> List[QuizQuestion]:
    response = get(f'https://opentdb.com/api.php?amount=10&difficulty={difficulty}&type=boolean')
    return [
        QuizQuestion(question=question['question'], correct_answer=question['correct_answer'])
        for question in response.json()['results']
    ]
