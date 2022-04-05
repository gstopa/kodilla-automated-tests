from typing import Any

import pytest

from romans.romans import to_romans


def test_to_romans_convert_1_to_i() -> None:
    assert to_romans(number=1) == "I"


@pytest.mark.parametrize("data", [1.0, "1", []])
def test_to_romans_raises_typeerror_when_number_is_not_integer(data: Any) -> None:
    with pytest.raises(TypeError):
        to_romans(number=data)
