"""

To run tests install pytest package and run pytest:

    .. code:: bash

        $ pip install pytest
        $ pytest

"""
import string


def is_palindrome(
        data: str,
        case_sensitive: bool = True,
        whitespace_sensitive: bool = True,
        punctuation_sensitive: bool = True,
) -> bool:
    if not isinstance(data, str):
        raise ValueError(f"Expected string, got {type(data)}!")
    prepared_data = data
    if not case_sensitive:
        prepared_data = prepared_data.lower()
    if not whitespace_sensitive:
        prepared_data = prepared_data.translate(str.maketrans("", "", string.whitespace))
    if not punctuation_sensitive:
        prepared_data = prepared_data.translate(str.maketrans("", "", string.punctuation))
    return prepared_data == prepared_data[-1::-1]
