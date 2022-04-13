from typing import Any, Dict, List
import pytest
from quizy.data_models import QuizQuestion


@pytest.fixture
def hard_questions_json() -> Dict[str, Any]:
    return {
        'response_code': 0,
        'results': [
            {
                'category': 'History',
                'type': 'boolean',
                'difficulty': 'hard',
                'question': 'Japan was part of the Allied Powers during World War I.',
                'correct_answer': 'True',
                'incorrect_answers': ['False']
            },
            {
                'category': 'Entertainment: Video Games',
                'type': 'boolean',
                'difficulty': 'hard',
                'question': 'The first &quot;Metal Gear&quot; game was released for the PlayStation 1.',
                'correct_answer': 'False',
                'incorrect_answers': ['True']
            },
            {
                'category': 'Science: Mathematics',
                'type': 'boolean',
                'difficulty': 'hard',
                'question': 'If you could fold a piece of paper in half 50 times, its&#039; thickness will be 3/4th the distance from the Earth to the Sun.',
                'correct_answer': 'True',
                'incorrect_answers': ['False']
            },
            {
                'category': 'Entertainment: Video Games',
                'type': 'boolean',
                'difficulty': 'hard',
                'question': 'In Undertale, having a &quot;Fun Value&quot; set to 56-57 will play the &quot;Wrong Number Song Call&quot;.',
                'correct_answer': 'False',
                'incorrect_answers': ['True']
            },
            {
                'category': 'General Knowledge',
                'type': 'boolean',
                'difficulty': 'hard',
                'question': 'In Scandinavian languages, the letter &Aring; means river.',
                'correct_answer': 'True',
                'incorrect_answers': ['False']
            },
            {
                'category': 'Politics',
                'type': 'boolean',
                'difficulty': 'hard',
                'question': 'Joko Widodo has appeared in the cover of a TIME magazine.',
                'correct_answer': 'True',
                'incorrect_answers': ['False']
            },
            {
                'category': 'Entertainment: Japanese Anime & Manga',
                'type': 'boolean',
                'difficulty': 'hard',
                'question': 'Druid is a mage class in &quot;Log Horizon&quot;.',
                'correct_answer': 'False',
                'incorrect_answers': ['True']
            },
            {
                'category': 'Entertainment: Board Games',
                'type': 'boolean',
                'difficulty': 'hard',
                'question': 'The board game Go has more possible legal positions than the number of atoms in the visible universe.',
                'correct_answer': 'True',
                'incorrect_answers': ['False']
            },
            {
                'category': 'Entertainment: Music',
                'type': 'boolean',
                'difficulty': 'hard',
                'question': 'The song Scatman&#039;s World was released after Scatman (Ski-Ba-Bop-Ba-Dop-Bop).',
                'correct_answer': 'True',
                'incorrect_answers': ['False']
            },
            {
                'category': 'Geography',
                'type': 'boolean',
                'difficulty': 'hard',
                'question': 'Only one country in the world starts with the letter Q.',
                'correct_answer': 'True',
                'incorrect_answers': ['False']
            }
        ]
    }


@pytest.fixture
def hard_quiz_questions() -> List[QuizQuestion]:
    return [
        QuizQuestion(question='Japan was part of the Allied Powers during World War I.', correct_answer='True'),
        QuizQuestion(question='The first &quot;Metal Gear&quot; game was released for the PlayStation 1.', correct_answer='False'),
        QuizQuestion(question='If you could fold a piece of paper in half 50 times, its&#039; thickness will be 3/4th the distance from the Earth to the Sun.', correct_answer='True'),
        QuizQuestion(question='In Undertale, having a &quot;Fun Value&quot; set to 56-57 will play the &quot;Wrong Number Song Call&quot;.', correct_answer='False'),
        QuizQuestion(question='In Scandinavian languages, the letter &Aring; means river.', correct_answer='True'),
        QuizQuestion(question='Joko Widodo has appeared in the cover of a TIME magazine.', correct_answer='True'),
        QuizQuestion(question='Druid is a mage class in &quot;Log Horizon&quot;.', correct_answer='False'),
        QuizQuestion(question='The board game Go has more possible legal positions than the number of atoms in the visible universe.', correct_answer='True'),
        QuizQuestion(question='The song Scatman&#039;s World was released after Scatman (Ski-Ba-Bop-Ba-Dop-Bop).', correct_answer='True'),
        QuizQuestion(question='Only one country in the world starts with the letter Q.', correct_answer='True'),
    ]
