from itertools import count
from typing import Iterator, List


def possible_factors() -> Iterator[int]:
    yield 2
    for value in count(3, step=2):  # pragma: no branch
        yield value


def prime_factors(number: int) -> List[int]:
    if not isinstance(number, int):
        raise ValueError(f"Expected integer, got {type(number)}!")
    factors_to_check = possible_factors()
    found_factors = []
    for factor in factors_to_check:  # pragma: no branch
        while number % factor == 0:
            found_factors.append(factor)
            number //= factor
        if number == 1:
            break
    return found_factors