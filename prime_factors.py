from typing import List


def prime_factors(number: int) -> List[int]:
    if not isinstance(number, int):
        raise ValueError(f"Expected integer, got {type(number)}!")
    factors = []
    while number % 2 == 0:
        factors.append(2)
        number /= 2
    while number % 3 == 0:
        factors.append(3)
        number /= 3
    if number % 5 == 0:
        factors.append(5)
    if factors:
        return factors
    return [number]
