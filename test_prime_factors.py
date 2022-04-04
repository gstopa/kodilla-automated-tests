import pytest
from prime_factors import prime_factors


def test_prime_factors_returns_list() -> None:
    result = prime_factors(number=2)
    assert isinstance(result, list), \
        f"Expected result to be a list, got {type(result)}!"


def test_prime_factors_raises_valueerror_when_number_is_not_an_integer() -> None:
    expectation = "Expected integer, got <class 'float'>!"
    with pytest.raises(ValueError) as value_error:
        prime_factors(number=2.0)
    assert str(value_error.value) == expectation, \
        f"Expected '{expectation}', got '{str(value_error.value)}' for '2.0'!"
    expectation = "Expected integer, got <class 'str'>!"
    with pytest.raises(ValueError) as value_error:
        prime_factors(number="2.0")
    assert str(value_error.value) == expectation, \
        f"Expected '{expectation}', got '{str(value_error.value)}' for '\"2.0\"'!"
