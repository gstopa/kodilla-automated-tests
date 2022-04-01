import pytest
from collections import namedtuple
from palindrome import is_palindrome


TestCase = namedtuple(
    typename='TestCase',
    field_names=["expectation", "data", "case_sensitive", "whitespace_sensitive", "punctuation_sensitive"],
)


def test_non_string_data_raises_valueerror() -> None:
    options = {
        "case_sensitive": False,
        "whitespace_sensitive": False,
        "punctuation_sensitive": False,
    }
    test_cases = [
        TestCase(expectation="Expected string, got <class 'NoneType'>!", data=None, **options),
        TestCase(expectation="Expected string, got <class 'bytes'>!", data=b"", **options),
        TestCase(expectation="Expected string, got <class 'bytearray'>!", data=bytearray(), **options),
        TestCase(expectation="Expected string, got <class 'tuple'>!", data=tuple(), **options),
        TestCase(expectation="Expected string, got <class 'list'>!", data=[], **options),
        TestCase(expectation="Expected string, got <class 'int'>!", data=0, **options),
        TestCase(expectation="Expected string, got <class 'float'>!", data=0.0, **options),
    ]
    for expectation, data, case_sensitive, whitespace_sensitive, punctuation_sensitive in test_cases:
        with pytest.raises(ValueError) as value_error:
            is_palindrome(data, case_sensitive, whitespace_sensitive, punctuation_sensitive)
        assert str(value_error.value) == expectation, \
            (
                f"Expected '{expectation}' for '{data}' and "
                f"options {case_sensitive=}, {whitespace_sensitive=}, {punctuation_sensitive=}!"
            )


def test_empty_string_is_a_palindrome() -> None:
    expectation, data = True, ""
    assert is_palindrome(data, case_sensitive=False, whitespace_sensitive=False, punctuation_sensitive=False) == expectation, f"Expected '{expectation}' for '{data}'!"
    assert is_palindrome(data, case_sensitive=True, whitespace_sensitive=True, punctuation_sensitive=True) == expectation, f"Expected '{expectation}' for '{data}'!"


def test_string_single_word_palindromes_case_insensitive() -> None:
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
        assert is_palindrome(case, case_sensitive=False, whitespace_sensitive=False, punctuation_sensitive=False) == expectation, f"Expected '{expectation}' for '{case}'!"
        assert is_palindrome(case, case_sensitive=False, whitespace_sensitive=True, punctuation_sensitive=True) == expectation, f"Expected '{expectation}' for '{case}'!"


def test_string_single_word_non_palindromes_due_to_case_sensitive() -> None:
    test_cases = {
        # mixed case
        "Abba": False,  # even length
        "TowOt": False,  # odd length
    }
    for case, expectation in test_cases.items():
        assert is_palindrome(case, case_sensitive=True, whitespace_sensitive=False, punctuation_sensitive=False) == expectation, f"Expected '{expectation}' for '{case}'!"
        assert is_palindrome(case, case_sensitive=True, whitespace_sensitive=True, punctuation_sensitive=True) == expectation, f"Expected '{expectation}' for '{case}'!"


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
        assert is_palindrome(case, case_sensitive=False, whitespace_sensitive=False, punctuation_sensitive=False) == expectation, f"Expected '{expectation}' for '{case}'!"
        assert is_palindrome(case, case_sensitive=True, whitespace_sensitive=True, punctuation_sensitive=True) == expectation, f"Expected '{expectation}' for '{case}'!"


def test_string_multiple_word_palindromes_whitespace_insensitive() -> None:
    test_cases = {
        # same spacing
        "sator arepo tenet opera rotas": True,
        # different_spacing
        "was it a cat i saw": True,
    }
    for case, expectation in test_cases.items():
        assert is_palindrome(case, case_sensitive=False, whitespace_sensitive=False, punctuation_sensitive=False) == expectation, f"Expected '{expectation}' for '{case}'!"
        assert is_palindrome(case, case_sensitive=True, whitespace_sensitive=False, punctuation_sensitive=True) == expectation, f"Expected '{expectation}' for '{case}'!"


def test_string_multiple_word_non_palindromes_due_to_whitespace_sensitive() -> None:
    test_cases = {
        # same spacing
        "sator arepo tenet  opera rotas": False,
        # different_spacing
        "was it a cat i saw": False,
    }
    for case, expectation in test_cases.items():
        assert is_palindrome(case, case_sensitive=False, whitespace_sensitive=True, punctuation_sensitive=False) == expectation, f"Expected '{expectation}' for '{case}'!"
        assert is_palindrome(case, case_sensitive=True, whitespace_sensitive=True, punctuation_sensitive=True) == expectation, f"Expected '{expectation}' for '{case}'!"


def test_string_multiple_word_non_palindromes() -> None:
    test_cases = {
        # same spacing
        "ala ma psa": False,
        # different_spacing
        "was it a dog i saw": False,
    }
    for case, expectation in test_cases.items():
        assert is_palindrome(case, case_sensitive=False, whitespace_sensitive=False, punctuation_sensitive=False) == expectation, f"Expected '{expectation}' for '{case}'!"
        assert is_palindrome(case, case_sensitive=True, whitespace_sensitive=True, punctuation_sensitive=True) == expectation, f"Expected '{expectation}' for '{case}'!"


def test_string_multiple_words_palindromes_punctuation_insensitive() -> None:
    test_cases = {
        "Madam, I'm Adam!": True,
        "Was it a cat I saw?": True,
        "Race fast, safe car.": True,
    }
    for case, expectation in test_cases.items():
        assert is_palindrome(case, case_sensitive=False, whitespace_sensitive=False, punctuation_sensitive=False) == expectation, f"Expected '{expectation}' for '{case}'!"


def test_string_multiple_words_non_palindromes_due_to_punctuation_sensitive() -> None:
    test_cases = {
        "Madam, I'm Adam!": False,
        "Was it a cat I saw?": False,
        "Race fast, safe car.": False,
    }
    for case, expectation in test_cases.items():
        assert is_palindrome(case, case_sensitive=False, whitespace_sensitive=False, punctuation_sensitive=True) == expectation, f"Expected '{expectation}' for '{case}'!"


def test_string_multiple_words_non_palindromes_with_punctuation() -> None:
    test_cases = {
        "Man, it's a hot one!": False,
        "Who is it?": False,
        "In ancient times cats were worshipped as gods; they have not forgotten this.": False,
    }
    for case, expectation in test_cases.items():
        assert is_palindrome(case, case_sensitive=False, whitespace_sensitive=False, punctuation_sensitive=False) == expectation, f"Expected '{expectation}' for '{case}'!"
        assert is_palindrome(case, case_sensitive=True, whitespace_sensitive=True, punctuation_sensitive=True) == expectation, f"Expected '{expectation}' for '{case}'!"
