"""

To run tests install pytest package and run pytest:

    .. code:: bash

        $ pip install pytest
        $ pytest

"""
import string
from collections.abc import Iterable
from typing import Any


def translate_data_to_unambiguous_string(data_to_translate: Any) -> str:
    if isinstance(data_to_translate, str):
        return data_to_translate
    if isinstance(data_to_translate, (bytes, bytearray)):
        return data_to_translate.decode()
    if isinstance(data_to_translate, Iterable):
        return "".join(data_to_translate)
    if isinstance(data_to_translate, float):
        float_with_dot_replaced_with_palindrome = str(data_to_translate).replace(".", "DOTOD")
        return float_with_dot_replaced_with_palindrome
    return str(data_to_translate)


def prep_string_data(data_to_prep: str) -> str:
    translation = str.maketrans("", "", string.punctuation + string.whitespace)
    data_without_punctuation_and_whitespace = data_to_prep.translate(translation)
    data_lower_case = data_without_punctuation_and_whitespace.lower()
    return data_lower_case


def is_palindrome(data: Any) -> bool:
    string_data = translate_data_to_unambiguous_string(data)
    prepared_data = prep_string_data(string_data)
    return prepared_data == prepared_data[-1::-1]
