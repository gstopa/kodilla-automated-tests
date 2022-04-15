from typing import List, Set

import requests.exceptions
from requests import get
from quizy.data_models import DIFFICULTIES, QuizQuestion


def generate_questions(difficulty: str) -> List[QuizQuestion]:
    if difficulty not in DIFFICULTIES:
        raise ValueError
    try:
        response = get(f'https://opentdb.com/api.php?amount=10&difficulty={difficulty}&type=boolean')
    except requests.exceptions.ConnectionError:
        raise ConnectionError
    return [
        QuizQuestion(question=question['question'], correct_answer=question['correct_answer'])
        for question in response.json()['results']
    ]
