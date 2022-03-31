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
    data_stripped_from_whitespace = data_to_prep.strip()
    data_without_punctuation = data_stripped_from_whitespace.translate(str.maketrans("", "", string.punctuation))
    data_case_insensitive = data_without_punctuation.lower()
    data_no_spaces = ''.join(data_case_insensitive.split())
    return data_no_spaces


def compare(data_to_compare: str) -> bool:
    begin = 0
    end = len(data_to_compare)
    begin_half, reminder = divmod(end, 2)
    if reminder == 0:
        end_half = begin_half - 1
    else:
        end_half = begin_half
    return data_to_compare[begin:begin_half] == data_to_compare[end:end_half:-1]


def is_palindrome(data: Any) -> bool:
    string_data = translate_data_to_unambiguous_string(data)
    prepared_data = prep_string_data(string_data)
    return compare(prepared_data)
