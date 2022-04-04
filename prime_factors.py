from typing import List


def prime_factors(number: int) -> List[int]:
    if not isinstance(number, int):
        raise ValueError(f"Expected integer, got {type(number)}!")
    factors = []
    if number % 2 == 0:
        factors.append(2)
    if number % 3 == 0:
        factors.append(3)
    if factors:
        return factors
    return [number]
