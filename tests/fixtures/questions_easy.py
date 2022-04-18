from typing import Any, Dict, List
import pytest
from quizy.data_models import QuizQuestion


@pytest.fixture
def easy_questions_json() -> Dict[str, Any]:
    return {
        'response_code': 0,
        'results': [
            {
                'category': 'History',
                'type': 'boolean',
                'difficulty': 'easy',
                'question': 'The Cold War ended with Joseph Stalin&#039;s death.',
                'correct_answer': 'False',
                'incorrect_answers': ['True']
            },
            {
                'category': 'Entertainment: Video Games',
                'type': 'boolean',
                'difficulty': 'easy',
                'question': 'English new wave musician Gary Numan founded the video game development company Facepunch Studios in March 2009.',
                'correct_answer': 'False',
                'incorrect_answers': ['True']
            },
            {
                'category': 'History',
                'type': 'boolean',
                'difficulty': 'easy',
                'question': 'The Spitfire originated from a racing plane.',
                'correct_answer': 'True',
                'incorrect_answers': ['False']},
            {
                'category': 'General Knowledge',
                'type': 'boolean',
                'difficulty': 'easy',
                'question': 'It is automatically considered entrapment in the United States if the police sell you illegal substances without revealing themselves.',
                'correct_answer': 'False',
                'incorrect_answers': ['True']},
            {
                'category': 'Entertainment: Film',
                'type': 'boolean',
                'difficulty': 'easy',
                'question': 'Samuel L. Jackson had the words, &#039;Bad Motherf*cker&#039; in-scripted on his lightsaber during the filming of Star Wars.',
                'correct_answer': 'True',
                'incorrect_answers': ['False']},
            {
                'category': 'Entertainment: Video Games',
                'type': 'boolean',
                'difficulty': 'easy',
                'question': 'Valve&#039;s &quot;Portal&quot; and &quot;Half-Life&quot; franchises exist within the same in-game universe.',
                'correct_answer': 'True',
                'incorrect_answers': ['False']},
            {
                'category': 'History',
                'type': 'boolean',
                'difficulty': 'easy',
                'question': 'Kublai Khan is the grandchild of Genghis Khan?',
                'correct_answer': 'True',
                'incorrect_answers': ['False']},
            {
                'category': 'Entertainment: Television',
                'type': 'boolean',
                'difficulty': 'easy',
                'question': 'Klingons express emotion in art through opera and poetry.',
                'correct_answer': 'True',
                'incorrect_answers': ['False']},
            {
                'category': 'Science: Mathematics',
                'type': 'boolean',
                'difficulty': 'easy',
                'question': 'The sum of any two odd integers is odd.',
                'correct_answer': 'False',
                'incorrect_answers': ['True']},
            {
                'category': 'Geography',
                'type': 'boolean',
                'difficulty': 'easy',
                'question': 'There is an island in Japan called Ōkunoshima, A.K.A. &quot;Rabbit Island&quot;, so named because of it&#039;s huge population of rabbits.',
                'correct_answer': 'True',
                'incorrect_answers': ['False']
             }
        ]
    }


@pytest.fixture
def easy_quiz_questions() -> List[QuizQuestion]:
    return [
        QuizQuestion(question='The Cold War ended with Joseph Stalin&#039;s death.', correct_answer='False'),
        QuizQuestion(question='English new wave musician Gary Numan founded the video game development company Facepunch Studios in March 2009.', correct_answer='False'),
        QuizQuestion(question='The Spitfire originated from a racing plane.', correct_answer='True'),
        QuizQuestion(question='It is automatically considered entrapment in the United States if the police sell you illegal substances without revealing themselves.', correct_answer='False'),
        QuizQuestion(question='Samuel L. Jackson had the words, &#039;Bad Motherf*cker&#039; in-scripted on his lightsaber during the filming of Star Wars.', correct_answer='True'),
        QuizQuestion(question='Valve&#039;s &quot;Portal&quot; and &quot;Half-Life&quot; franchises exist within the same in-game universe.', correct_answer='True'),
        QuizQuestion(question='Kublai Khan is the grandchild of Genghis Khan?', correct_answer='True'),
        QuizQuestion(question='Klingons express emotion in art through opera and poetry.', correct_answer='True'),
        QuizQuestion(question='The sum of any two odd integers is odd.', correct_answer='False'),
        QuizQuestion(question='There is an island in Japan called Ōkunoshima, A.K.A. &quot;Rabbit Island&quot;, so named because of it&#039;s huge population of rabbits.', correct_answer='True'),
    ]


@pytest.fixture
def easy_quiz_answers_all_correct() -> Dict[str, str]:
    return {
        '0': 'False',
        '1': 'False',
        '2': 'True',
        '3': 'False',
        '4': 'True',
        '5': 'True',
        '6': 'True',
        '7': 'True',
        '8': 'False',
        '9': 'True',
    }


@pytest.fixture
def easy_quiz_answers_all_incorrect() -> Dict[str, str]:
    return {
        '0': 'True',
        '1': 'True',
        '2': 'False',
        '3': 'True',
        '4': 'False',
        '5': 'False',
        '6': 'False',
        '7': 'False',
        '8': 'True',
        '9': 'False',
    }


@pytest.fixture
def easy_quiz_answers_five_correct() -> Dict[str, str]:
    return {
        '0': 'True',
        '1': 'True',
        '2': 'False',
        '3': 'True',
        '4': 'False',
        '5': 'True',
        '6': 'True',
        '7': 'True',
        '8': 'False',
        '9': 'True',
    }
