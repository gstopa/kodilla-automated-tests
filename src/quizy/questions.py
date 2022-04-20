"""Quiz questions generator based on Open Trivia Database."""
from typing import List

import requests.exceptions
from requests import get

from quizy.data_models import DIFFICULTIES, QuizQuestion


def generate_questions(difficulty: str) -> List[QuizQuestion]:
    """
    Generates Quiz questions using Open Trivia Database.

    :param difficulty:
        Quiz difficulty: 'easy', 'medium', 'hard'
    :return:
        Quiz questions
    """
    if difficulty not in DIFFICULTIES:
        raise ValueError
    try:
        response = get(
            "https://opentdb.com/api.php"
            f"?amount=10&difficulty={difficulty}&type=boolean"
        )
    except requests.exceptions.ConnectionError as connection_error:
        raise ConnectionError from connection_error
    return [
        QuizQuestion(
            question=question["question"],
            correct_answer=question["correct_answer"],
        )
        for question in response.json()["results"]
    ]
