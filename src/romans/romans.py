def to_romans(number: int) -> str:
    if not isinstance(number, int):
        raise TypeError(f"Expected number to be an integer, got {type(number)}!")
    if number not in range(1, 4000):
        raise ValueError(f"Expected number to be in range [1; 3999], got {number}!")
    return "I"
