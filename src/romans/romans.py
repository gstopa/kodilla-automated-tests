ROMANS_CHARACTERS = {'I', 'V', 'X', 'L', 'C', 'D', 'M'}
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


def contains_invalid_characters(romans: str) -> bool:
    return ROMANS_CHARACTERS | set(romans) != ROMANS_CHARACTERS


def romans_to_decimal(romans: str) -> int:
    if not isinstance(romans, str):
        raise TypeError(f"Expected romans to be a string, got {type(romans)}!")
    if len(romans) == 0:
        raise ValueError("String romans is empty!")
    if contains_invalid_characters(romans):
        raise ValueError(
            "String romans contains invalid characters!"
            f"\nValid characters are 'I', 'V', 'X', 'L', 'C', 'D', 'M'; got '{romans}'!"
        )
    number = 0
    for roman in romans:
        number += ROMANS_TO_DECIMAL_LOOKUP[roman]
    return number
