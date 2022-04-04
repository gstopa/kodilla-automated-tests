from typing import Any, List
import pytest
from prime_factors import prime_factors


def test_prime_factors_returns_list() -> None:
    result = prime_factors(number=2)
    assert isinstance(result, list), \
        f"Expected result to be a list, got {type(result)}!"


@pytest.mark.parametrize(
    "data,expectation",
    [
        (2.0, "Expected integer, got <class 'float'>!"),
        ("2.0", "Expected integer, got <class 'str'>!"),
        ([], "Expected integer, got <class 'list'>!"),
    ],
)
def test_prime_factors_raises_valueerror_when_number_is_not_an_integer(data: Any, expectation: str) -> None:
    with pytest.raises(ValueError) as value_error:
        prime_factors(number=data)
    assert str(value_error.value) == expectation, \
        f"Expected '{expectation}', got '{str(value_error.value)}' for '{data}'!"


@pytest.mark.parametrize("data", [2, 11])
def test_prime_factors_prime_numbers_return_only_itself(data: int) -> None:
    result = prime_factors(number=data)
    assert result == [data], \
        f"Expected result=[{data}], got {result=}!"


@pytest.mark.parametrize("data", [4, 6])
def test_prime_factors_even_numbers_returns_at_least_one_2(data: int) -> None:
    result = prime_factors(number=data)
    assert 2 in result, \
        f"Expected result has at least one 2, got {result=}!"


@pytest.mark.parametrize("data", [9, 6])
def test_prime_factors_numbers_that_are_multiple_of_three_returns_at_least_one_3(data: int) -> None:
    result = prime_factors(number=data)
    assert 3 in result, \
        f"Expected result has at least one 3, got {result=}!"


@pytest.mark.parametrize("data", [10, 15])
def test_prime_factors_numbers_that_are_multiple_of_five_returns_at_least_one_5(data: int) -> None:
    result = prime_factors(number=data)
    assert 5 in result, \
        f"Expected result has at least one 5, got {result=}!"


@pytest.mark.parametrize(
    "data,expectation",
    [
        (4, [2, 2]),
        (16, [2, 2, 2, 2]),
    ],
)
def test_prime_factors_complex_numbers_with_multiple_2_factors(data: int, expectation: List[int]) -> None:
    result = prime_factors(number=data)
    assert result == expectation, \
        f"Expected result={expectation}, got {result=}!"


@pytest.mark.parametrize(
    "data,expectation",
    [
        (9, [3, 3]),
        (81, [3, 3, 3, 3]),
    ],
)
def test_prime_factors_complex_numbers_with_multiple_3_factors(data: int, expectation: List[int]) -> None:
    result = prime_factors(number=data)
    assert result == expectation, \
        f"Expected result={expectation}, got {result=}!"


@pytest.mark.parametrize(
    "data,expectation",
    [
        (25, [5, 5]),
        (625, [5, 5, 5, 5]),
    ],
)
def test_prime_factors_complex_numbers_with_multiple_5_factors(data: int, expectation: List[int]) -> None:
    result = prime_factors(number=data)
    assert result == expectation, \
        f"Expected result={expectation}, got {result=}!"


@pytest.mark.parametrize(
    "data,expectation",
    [
        (70, [2, 5, 7]),
        (66, [2, 3, 11]),
    ],
)
def test_prime_factors_complex_numbers_with_single_different_factors(data: int, expectation: List[int]) -> None:
    result = prime_factors(number=data)
    assert result == expectation, \
        f"Expected result={expectation}, got {result=}!"


@pytest.mark.parametrize(
    "data,expectation",
    [
        (174, [2, 3, 29]),
    ],
)
def test_prime_factors_complex_big_numbers(data: int, expectation: List[int]) -> None:
    result = prime_factors(number=data)
    assert result == expectation, \
        f"Expected result={expectation}, got {result=}!"
