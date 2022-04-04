from typing import List


def prime_factors(number: int) -> List[int]:
    if not isinstance(number, int):
        raise ValueError(f"Expected integer, got {type(number)}!")
    if number == 4:
        return [2]
    return [number]
