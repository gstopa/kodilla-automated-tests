from prime_factors import prime_factors


def test_prime_factors_returns_list() -> None:
    result = prime_factors(number=0)
    assert isinstance(result, list)
