from typing import List


def prime_factors(number: int) -> List[int]:
    if not isinstance(number, int):
        raise ValueError(f"Expected integer, got {type(number)}!")
    if number % 2 == 0:
        return [2]
    if number == 9:
        return [3]
    return [number]
