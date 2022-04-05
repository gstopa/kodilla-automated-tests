from romans.romans import to_romans


def test_to_romans_convert_1_to_i() -> None:
    assert to_romans(number=1) == "I"
