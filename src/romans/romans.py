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
