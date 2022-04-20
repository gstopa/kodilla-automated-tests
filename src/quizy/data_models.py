"""Quizy data containers."""
from dataclasses import dataclass
from typing import Dict, Set

POINTS_MULTIPLIER: Dict[str, int] = {
    "easy": 1,
    "medium": 3,
    "hard": 6,
}
DIFFICULTIES: Set[str] = set(POINTS_MULTIPLIER.keys())


@dataclass
class QuizQuestion:
    """Quiz question"""

    question: str
    correct_answer: str


@dataclass
class QuizTest:
    """Quiz test"""

    uuid: str
    difficulty: str
    questions: Dict[str, QuizQuestion]


@dataclass
class QuizResult:
    """Quiz results"""

    uuid: str
    user_id: int
    score: int
