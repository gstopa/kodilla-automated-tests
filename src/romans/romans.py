import re


ROMAN_NUMERAL_REGEX = re.compile(
    r'''
    ^
    M{0,3}              # up to 3 thousands
    (CM|CD|D?C{0,3})    # 900, 400, 500-800 or 0-300
    (XC|XL|L?X{0,3})    # 90, 40, 50-80 or 0-30
    (IX|IV|V?I{0,3})    # 9, 4, 5-8 or 0-3
    $
    ''',
    re.VERBOSE
)
ROMANS_TO_DECIMAL_LOOKUP = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}
DECIMAL_TO_ROMANS_LOOKUP = {
    1: "I",
    4: "IV",
    5: "V",
    9: "IX",
    10: "X",
    40: "XL",
    50: "L",
    90: "XC",
    100: "C",
    200: "CC",
    400: "CD",
    500: "D",
    900: "CM",
    1000: "M",
}


def decimal_to_romans(number: int) -> str:
    if not isinstance(number, int):
        raise TypeError(f"Expected number to be an integer, got {type(number)}!")
    if number not in range(1, 4000):
        raise ValueError(f"Expected number to be in range [1; 3999], got {number}!")
    romans = []
    major_decimals = list(DECIMAL_TO_ROMANS_LOOKUP.keys())
    major_decimals.sort(reverse=True)
    for decimal in major_decimals:  # pragma: no branch
        while number >= decimal:
            romans.append(DECIMAL_TO_ROMANS_LOOKUP[decimal])
            number -= decimal
        if number == 0:
            break
    return "".join(romans)


def is_invalid_romans_numeral(romans: str) -> bool:
    return not bool(ROMAN_NUMERAL_REGEX.search(romans))


def translate_from_one_less_into_additive_only_roman_numeral(romans: str) -> str:
    romans = romans.replace("CM", "DCCCC")
    romans = romans.replace("CD", "CCCC")
    romans = romans.replace("XC", "LXXXX")
    romans = romans.replace("XL", "XXXX")
    romans = romans.replace("IX", "VIIII")
    romans = romans.replace("IV", "IIII")
    return romans


def romans_to_decimal(romans: str) -> int:
    if not isinstance(romans, str):
        raise TypeError(f"Expected romans to be a string, got {type(romans)}!")
    if len(romans) == 0:
        raise ValueError("String romans is empty!")
    if is_invalid_romans_numeral(romans):
        raise ValueError(f"Invalid romans numeral, got '{romans}'!")
    romans = translate_from_one_less_into_additive_only_roman_numeral(romans)
    whole_number = 0
    for roman in romans:
        whole_number += ROMANS_TO_DECIMAL_LOOKUP[roman]
    return whole_number
