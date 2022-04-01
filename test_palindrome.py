import pytest
from collections import namedtuple
from palindrome import is_palindrome


TestCase = namedtuple('TestCase', ["case", "expectation"])


def test_non_string_data_raises_valueerror() -> None:
    test_cases = [
        TestCase(case=None, expectation="Expected string, got <class 'NoneType'>!"),
        TestCase(case=b"", expectation="Expected string, got <class 'bytes'>!"),
        TestCase(case=bytearray(), expectation="Expected string, got <class 'bytearray'>!"),
        TestCase(case=tuple(), expectation="Expected string, got <class 'tuple'>!"),
        TestCase(case=[], expectation="Expected string, got <class 'list'>!"),
        TestCase(case=0, expectation="Expected string, got <class 'int'>!"),
        TestCase(case=0.0, expectation="Expected string, got <class 'float'>!"),
    ]
    for case, expectation in test_cases:
        with pytest.raises(ValueError) as value_error:
            is_palindrome(case)
        assert str(value_error.value) == expectation


def test_empty_string_is_a_palindrome() -> None:
    case, expectation = "", True
    assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"


def test_string_single_word_palindromes() -> None:
    test_cases = {
        # all lower case
        "abba": True,  # even length
        "towot": True,  # odd length
        # all upper case
        "ABBA": True,  # even length
        "TOWOT": True,  # odd length
        # mixed case
        "Abba": True,  # even length
        "TowOt": True,  # odd length
    }
    for case, expectation in test_cases.items():
        assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"


def test_string_single_word_non_palindromes() -> None:
    test_cases = {
        # all lower case
        "intel": False,  # odd length
        "spacje": False,  # even length
        # all upper case
        "INTEL": False,  # odd length
        "SPACJE": False,  # even length
        # mixed case
        "Intel": False,  # odd length
        "Spacje": False,  # even length
    }
    for case, expectation in test_cases.items():
        assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"


def test_string_multiple_word_palindromes() -> None:
    test_cases = {
        # same spacing
        "sator arepo tenet opera rotas": True,
        # different_spacing
        "was it a cat i saw": True,
    }
    for case, expectation in test_cases.items():
        assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"


def test_string_multiple_word_non_palindromes() -> None:
    test_cases = {
        # same spacing
        "ala ma psa": False,
        # different_spacing
        "was it a dog i saw": False,
    }
    for case, expectation in test_cases.items():
        assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"


def test_string_multiple_words_palindromes_with_punctuation() -> None:
    test_cases = {
        "Madam, I'm Adam!": True,
        "Was it a cat I saw?": True,
        "Race fast, safe car.": True,
    }
    for case, expectation in test_cases.items():
        assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"


def test_string_multiple_words_non_palindromes_with_punctuation() -> None:
    test_cases = {
        "Man, it's a hot one!": False,
        "Who is it?": False,
        "In ancient times cats were worshipped as gods; they have not forgotten this.": False,
    }
    for case, expectation in test_cases.items():
        assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"
