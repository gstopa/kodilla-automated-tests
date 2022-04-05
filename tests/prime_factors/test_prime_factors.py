from typing import Any, List
import pytest
from prime_factors.prime_factors import prime_factors


@pytest.mark.parametrize("data", [2.0, "2.0", []])
def test_prime_factors_raises_valueerror_when_number_is_not_an_integer(data: Any) -> None:
    with pytest.raises(ValueError):
        prime_factors(number=data)


@pytest.mark.parametrize("data", [2, 11])
def test_prime_factors_prime_numbers_return_only_itself(data: int) -> None:
    result = prime_factors(number=data)
    assert result == [data]


@pytest.mark.parametrize(
    "data,expectation",
    [
        (4, [2, 2]),
        (16, [2, 2, 2, 2]),
    ],
)
def test_prime_factors_complex_numbers_with_multiple_2_factors(data: int, expectation: List[int]) -> None:
    result = prime_factors(number=data)
    assert result == expectation


@pytest.mark.parametrize(
    "data,expectation",
    [
        (9, [3, 3]),
        (81, [3, 3, 3, 3]),
    ],
)
def test_prime_factors_complex_numbers_with_multiple_3_factors(data: int, expectation: List[int]) -> None:
    result = prime_factors(number=data)
    assert result == expectation


@pytest.mark.parametrize(
    "data,expectation",
    [
        (25, [5, 5]),
        (625, [5, 5, 5, 5]),
    ],
)
def test_prime_factors_complex_numbers_with_multiple_5_factors(data: int, expectation: List[int]) -> None:
    result = prime_factors(number=data)
    assert result == expectation


@pytest.mark.parametrize(
    "data,expectation",
    [
        (70, [2, 5, 7]),
        (66, [2, 3, 11]),
    ],
)
def test_prime_factors_complex_numbers_with_single_different_factors(data: int, expectation: List[int]) -> None:
    result = prime_factors(number=data)
    assert result == expectation


@pytest.mark.parametrize(
    "data,expectation",
    [
        (174, [2, 3, 29]),
        (3958159172, [2, 2, 11, 2347, 38329]),
    ],
)
def test_prime_factors_complex_big_numbers(data: int, expectation: List[int]) -> None:
    result = prime_factors(number=data)
    assert result == expectation
