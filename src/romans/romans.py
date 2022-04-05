def to_romans(number: int) -> str:
    if not isinstance(number, int):
        raise TypeError(f"Expected number to be an integer, got {type(number)}!")
    return "I"
