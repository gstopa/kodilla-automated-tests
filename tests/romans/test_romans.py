from typing import Any

import pytest

from romans.romans import to_romans


@pytest.mark.parametrize("data", [1.0, "1", []])
def test_to_romans_raises_typeerror_when_number_is_not_integer(data: Any) -> None:
    with pytest.raises(TypeError):
        to_romans(number=data)


@pytest.mark.parametrize("data", [-1, 0, 4000, 4001])
def test_to_romans_raises_valueerror_when_number_not_in_range_1_to_3999_both_inclusive(data: int) -> None:
    with pytest.raises(ValueError):
        to_romans(number=data)


@pytest.mark.parametrize(
    "data,expectation",
    [
        (1, "I"),
        (5, "V"),
        (10, "X"),
        (50, "L"),
        (100, "C"),
        (500, "D"),
        (1000, "M"),
    ],
)
def test_to_romans_convert_number_into_single_roman_character(data: int, expectation: str) -> None:
    assert to_romans(number=data) == expectation


@pytest.mark.parametrize(
    "data,expectation",
    [
        (4, "IV"),
        (9, "IX"),
        (40, "XL"),
        (90, "XC"),
        (400, "CD"),
        (900, "CM"),
    ],
)
def test_to_romans_convert_number_into_complex_one_less_than_roman_characters(data: int, expectation: str) -> None:
    assert to_romans(number=data) == expectation
