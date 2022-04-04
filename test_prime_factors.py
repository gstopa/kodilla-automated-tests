from prime_factors import prime_factors


def test_prime_factors_returns_list() -> None:
    result = prime_factors(number=2)
    assert isinstance(result, list), \
        f"Expected result to be a list, got {type(result)}!"
