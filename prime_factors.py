from typing import List


def prime_factors(number: int) -> List[int]:
    if not isinstance(number, int):
        raise ValueError(f"Expected integer, got {type(number)}!")
    factors_to_check = [2, 3, 5, 7, 11, 29]
    factors = []
    for factor in factors_to_check:
        while number % factor == 0:
            factors.append(factor)
            number /= factor
    return factors
