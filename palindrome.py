"""

To run tests install pytest package and run pytest:

    .. code:: bash

        $ pip install pytest
        $ pytest

"""
import string


def prep_string_data(data_to_prep: str) -> str:
    translation = str.maketrans("", "", string.punctuation + string.whitespace)
    data_without_punctuation_and_whitespace = data_to_prep.translate(translation)
    data_lower_case = data_without_punctuation_and_whitespace.lower()
    return data_lower_case


def is_palindrome(data: str) -> bool:
    if not isinstance(data, str):
        raise ValueError(f"Expected string, got {type(data)}!")
    prepared_data = prep_string_data(data)
    return prepared_data == prepared_data[-1::-1]
