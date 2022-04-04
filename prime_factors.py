from typing import List


def prime_factors(number: int) -> List[int]:
    if isinstance(number, float):
        raise ValueError("Expected integer, got <class 'float'>!")
    if isinstance(number, str):
        raise ValueError("Expected integer, got <class 'str'>!")
    if isinstance(number, list):
        raise ValueError(f"Expected integer, got <class 'list'>!")
    return []
