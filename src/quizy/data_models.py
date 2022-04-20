from dataclasses import dataclass
from typing import Dict, Set


POINTS_MULTIPLIER: Dict[str, int] = {
    'easy': 1,
    'medium': 3,
    'hard': 6,
}
DIFFICULTIES: Set[str] = set(POINTS_MULTIPLIER.keys())


@dataclass
class QuizQuestion:
    question: str
    correct_answer: str


@dataclass
class QuizTest:
    uuid: str
    difficulty: str
    questions: Dict[str, QuizQuestion]


@dataclass
class QuizResult:
    uuid: str
    user_id: int
    score: int
