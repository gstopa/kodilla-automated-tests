from prime_factors import prime_factors


def test_prime_factors() -> None:
    result = prime_factors(number=0)
    assert isinstance(result, list)
