from typing import Any, Dict, List
import pytest
from quizy.data_models import QuizQuestion


@pytest.fixture
def medium_questions_json() -> Dict[str, Any]:
    return {
        'response_code': 0,
        'results': [
            {
                'category': 'Science: Computers',
                'type': 'boolean',
                'difficulty': 'medium',
                'question': 'FLAC stands for &quot;Free Lossless Audio Condenser&quot;&#039;',
                'correct_answer': 'False',
                'incorrect_answers': ['True']
            },
            {
                'category': 'Entertainment: Music',
                'type': 'boolean',
                'difficulty': 'medium',
                'question': 'Arcade Fire&#039;s &#039;The Suburbs&#039; won the Album of the Year award in the 2011 Grammys.',
                'correct_answer': 'True',
                'incorrect_answers': ['False']
            },
            {
                'category': 'Science: Mathematics',
                'type': 'boolean',
                'difficulty': 'medium',
                'question': '111,111,111 x 111,111,111 = 12,345,678,987,654,321',
                'correct_answer': 'True',
                'incorrect_answers': ['False']
            },
            {
                'category': 'Mythology',
                'type': 'boolean',
                'difficulty': 'medium',
                'question': 'The Japanese god Izanagi successfully returned his wife Izanami from the Underworld.',
                'correct_answer': 'False',
                'incorrect_answers': ['True']
            },
            {
                'category': 'Science: Computers',
                'type': 'boolean',
                'difficulty': 'medium',
                'question': 'The first dual-core CPU was the Intel Pentium D.',
                'correct_answer': 'False',
                'incorrect_answers': ['True']
            },
            {
                'category': 'Entertainment: Video Games',
                'type': 'boolean',
                'difficulty': 'medium',
                'question': 'In Rocket League, you can play Basketball.',
                'correct_answer': 'True',
                'incorrect_answers': ['False']
            },
            {
                'category': 'Politics',
                'type': 'boolean',
                'difficulty': 'medium',
                'question': 'The State of Queensland, Australia voted NO to a referendum for daylight savings in 1992.',
                'correct_answer': 'True',
                'incorrect_answers': ['False']
            },
            {
                'category': 'Entertainment: Video Games',
                'type': 'boolean',
                'difficulty': 'medium',
                'question': 'The Fiat Multipla is a drivable car in &quot;Forza Horizon 3&quot;.',
                'correct_answer': 'False',
                'incorrect_answers': ['True']
            },
            {
                'category': 'Entertainment: Video Games',
                'type': 'boolean',
                'difficulty': 'medium',
                'question': '&quot;Return to Castle Wolfenstein&quot; was the only game of the Wolfenstein series where you don&#039;t play as William &quot;B.J.&quot; Blazkowicz.',
                'correct_answer': 'False',
                'incorrect_answers': ['True']
            },
            {
                'category': 'Sports',
                'type': 'boolean',
                'difficulty': 'medium',
                'question': 'ATP tennis hosted several tournaments on carpet court before being replaced to reduce injuries.',
                'correct_answer': 'True',
                'incorrect_answers': ['False']
            }
        ]
    }


@pytest.fixture
def medium_quiz_questions() -> List[QuizQuestion]:
    return [
        QuizQuestion(question='FLAC stands for &quot;Free Lossless Audio Condenser&quot;&#039;', correct_answer='False'),
        QuizQuestion(question='Arcade Fire&#039;s &#039;The Suburbs&#039; won the Album of the Year award in the 2011 Grammys.', correct_answer='True'),
        QuizQuestion(question='111,111,111 x 111,111,111 = 12,345,678,987,654,321', correct_answer='True'),
        QuizQuestion(question='The Japanese god Izanagi successfully returned his wife Izanami from the Underworld.', correct_answer='False'),
        QuizQuestion(question='The first dual-core CPU was the Intel Pentium D.', correct_answer='False'),
        QuizQuestion(question='In Rocket League, you can play Basketball.', correct_answer='True'),
        QuizQuestion(question='The State of Queensland, Australia voted NO to a referendum for daylight savings in 1992.', correct_answer='True'),
        QuizQuestion(question='The Fiat Multipla is a drivable car in &quot;Forza Horizon 3&quot;.', correct_answer='False'),
        QuizQuestion(question='&quot;Return to Castle Wolfenstein&quot; was the only game of the Wolfenstein series where you don&#039;t play as William &quot;B.J.&quot; Blazkowicz.', correct_answer='False'),
        QuizQuestion(question='ATP tennis hosted several tournaments on carpet court before being replaced to reduce injuries.', correct_answer='True'),
    ]


@pytest.fixture
def medium_quiz_answers_all_correct() -> Dict[str, str]:
    return {
        '0': 'False',
        '1': 'True',
        '2': 'True',
        '3': 'False',
        '4': 'False',
        '5': 'True',
        '6': 'True',
        '7': 'False',
        '8': 'False',
        '9': 'True',
    }


@pytest.fixture
def medium_quiz_answers_all_incorrect() -> Dict[str, str]:
    return {
        '0': 'True',
        '1': 'False',
        '2': 'False',
        '3': 'True',
        '4': 'True',
        '5': 'False',
        '6': 'False',
        '7': 'True',
        '8': 'True',
        '9': 'False',
    }


@pytest.fixture
def medium_quiz_answers_five_correct() -> Dict[str, str]:
    return {
        '0': 'True',
        '1': 'False',
        '2': 'False',
        '3': 'True',
        '4': 'True',
        '5': 'True',
        '6': 'True',
        '7': 'False',
        '8': 'False',
        '9': 'True',
    }
