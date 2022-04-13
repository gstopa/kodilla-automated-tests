from dataclasses import dataclass
from typing import Dict


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
