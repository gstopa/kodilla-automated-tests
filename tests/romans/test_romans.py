from typing import Any

import pytest

from romans.romans import decimal_to_romans, romans_to_decimal


@pytest.mark.parametrize("data", [1.0, "1", []])
def test_decimal_to_romans_raises_typeerror_when_number_is_not_integer(data: Any) -> None:
    with pytest.raises(TypeError):
        decimal_to_romans(number=data)


@pytest.mark.parametrize("data", [-1, 0, 4000, 4001])
def test_decimal_to_romans_raises_valueerror_when_number_not_in_range_1_to_3999_both_inclusive(data: int) -> None:
    with pytest.raises(ValueError):
        decimal_to_romans(number=data)


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
def test_decimal_to_romans_convert_number_into_single_roman_character(data: int, expectation: str) -> None:
    assert decimal_to_romans(number=data) == expectation


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
def test_decimal_to_romans_convert_number_into_complex_one_less_than_roman_characters(data: int, expectation: str) -> None:
    assert decimal_to_romans(number=data) == expectation


@pytest.mark.parametrize(
    "data,expectation",
    [
        (2000, "MM"),
        (1100, "MC"),
        (200, "CC"),
        (3999, "MMMCMXCIX"),
        (3888, "MMMDCCCLXXXVIII"),
        (3333, "MMMCCCXXXIII"),
        (2777, "MMDCCLXXVII"),
        (2222, "MMCCXXII"),
        (1666, "MDCLXVI"),
        (1111, "MCXI"),
    ],
)
def test_decimal_to_romans_convert_number_into_complex_roman_characters(data: int, expectation: str) -> None:
    assert decimal_to_romans(number=data) == expectation


@pytest.mark.parametrize("data", [1.0, 1, []])
def test_romans_to_decimal_raises_typeerror_when_romans_is_not_string(data: Any) -> None:
    with pytest.raises(TypeError):
        romans_to_decimal(romans=data)


def test_romans_to_decimal_raises_valueerror_when_romans_is_empty_string() -> None:
    with pytest.raises(ValueError):
        romans_to_decimal(romans="")


@pytest.mark.parametrize("data", ["qwerty", "ivxlcdm"])
def test_romans_to_decimal_raises_valueerror_when_romans_contain_non_romans_characters(data: str) -> None:
    with pytest.raises(ValueError):
        romans_to_decimal(romans=data)


@pytest.mark.parametrize(
    "data,expectation",
    [
        ("I", 1),
        ("V", 5),
        ("X", 10),
        ("L", 50),
        ("C", 100),
        ("D", 500),
        ("M", 1000),
    ],
)
def test_romans_to_decimal_convert_single_roman_character_to_number(data: str, expectation: int) -> None:
    assert romans_to_decimal(romans=data) == expectation


@pytest.mark.parametrize(
    "data,expectation",
    [
        ("MCXI", 1111),
        ("MMCCXXII", 2222),
        ("MMMCCCXXXIII", 3333),
        ("DLV", 555),
    ],
)
def test_romans_to_decimal_convert_complex_additive_only_roman_characters_to_number(data: str, expectation: int) -> None:
    assert romans_to_decimal(romans=data) == expectation
