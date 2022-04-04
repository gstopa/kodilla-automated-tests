from typing import List


def prime_factors(number: int) -> List[int]:
    if isinstance(number, float):
        raise ValueError("Expected integer, got <class 'float'>!")
    if isinstance(number, str):
        raise ValueError("Expected integer, got <class 'str'>!")
    return []
