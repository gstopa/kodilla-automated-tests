from typing import Any
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


def test_prime_factors_prime_numbers_return_only_itself() -> None:
    result = prime_factors(number=2)
    assert result == [2], \
        f"Expected result=[2], got {result=}!"
