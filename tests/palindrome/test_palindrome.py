import pytest
from collections import namedtuple
from palindrome.palindrome import is_palindrome


@pytest.mark.parametrize("case_sensitive", [True, False])
@pytest.mark.parametrize("whitespace_sensitive", [True, False])
@pytest.mark.parametrize("punctuation_sensitive", [True, False])
def test_non_string_data_raises_valueerror(
        case_sensitive: bool,
        whitespace_sensitive: bool,
        punctuation_sensitive: bool,
) -> None:
    TestCaseNoOptions = namedtuple(
        typename='TestCaseNoOptions',
        field_names=["expectation", "data"]
    )
    test_cases = [
        TestCaseNoOptions(expectation="Expected string, got <class 'NoneType'>!", data=None),
        TestCaseNoOptions(expectation="Expected string, got <class 'bytes'>!", data=b""),
        TestCaseNoOptions(expectation="Expected string, got <class 'bytearray'>!", data=bytearray()),
        TestCaseNoOptions(expectation="Expected string, got <class 'tuple'>!", data=tuple()),
        TestCaseNoOptions(expectation="Expected string, got <class 'list'>!", data=[]),
        TestCaseNoOptions(expectation="Expected string, got <class 'int'>!", data=0),
        TestCaseNoOptions(expectation="Expected string, got <class 'float'>!", data=0.0),
    ]
    for expectation, data in test_cases:
        with pytest.raises(ValueError) as value_error:
            is_palindrome(data, case_sensitive, whitespace_sensitive, punctuation_sensitive)
        assert str(value_error.value) == expectation, \
            f"Expected '{expectation}', got '{str(value_error.value)}' for '{data=}' and "\
            f"options '{case_sensitive=}', '{whitespace_sensitive=}', '{punctuation_sensitive=}'!"


@pytest.mark.parametrize("case_sensitive", [True, False])
@pytest.mark.parametrize("whitespace_sensitive", [True, False])
@pytest.mark.parametrize("punctuation_sensitive", [True, False])
def test_empty_string_is_a_palindrome(
        case_sensitive: bool,
        whitespace_sensitive: bool,
        punctuation_sensitive: bool,
) -> None:
    expectation, data = True, ""
    result = is_palindrome(data, case_sensitive, whitespace_sensitive, punctuation_sensitive)
    assert result == expectation,\
        f"Expected '{expectation}', got '{result}' for '{data=}' and "\
        f"options '{case_sensitive=}', '{whitespace_sensitive=}', '{punctuation_sensitive=}'!"


@pytest.mark.parametrize("case_sensitive", [True, False])
@pytest.mark.parametrize("whitespace_sensitive", [True, False])
@pytest.mark.parametrize("punctuation_sensitive", [True, False])
def test_strict_palindromes_that_are_not_affected_by_options(
        case_sensitive: bool,
        whitespace_sensitive: bool,
        punctuation_sensitive: bool,
) -> None:
    TestCaseNoOptions = namedtuple(
        typename='TestCaseNoOptions',
        field_names=["expectation", "data"]
    )
    test_cases = [
        TestCaseNoOptions(expectation=True, data="abba"),  # lower case even length
        TestCaseNoOptions(expectation=True, data="towot"),  # lower case odd length
        TestCaseNoOptions(expectation=True, data="ave eva"),  # with white space
        TestCaseNoOptions(expectation=True, data="ABBA"),  # upper case
        TestCaseNoOptions(expectation=True, data="AbbA"),  # mixed case
        TestCaseNoOptions(expectation=True, data="xml:lmx"),  # with punctuation inside
        TestCaseNoOptions(expectation=True, data="!abba!"),  # with punctuation outside
    ]
    for expectation, data in test_cases:
        result = is_palindrome(data, case_sensitive, whitespace_sensitive, punctuation_sensitive)
        assert result == expectation, \
            f"Expected '{expectation}', got '{result}' for '{data=}' and "\
            f"options '{case_sensitive=}', '{whitespace_sensitive=}', '{punctuation_sensitive=}'!"


@pytest.mark.parametrize("whitespace_sensitive", [True, False])
@pytest.mark.parametrize("punctuation_sensitive", [True, False])
def test_palindromes_option_case_sensitive(whitespace_sensitive: bool, punctuation_sensitive: bool) -> None:
    TestCaseCaseSensitive = namedtuple(
        typename='TestCaseCaseSensitive',
        field_names=["expectation", "data", "case_sensitive"]
    )
    test_cases = [
        TestCaseCaseSensitive(expectation=False, data="Atak kata", case_sensitive=True),
        TestCaseCaseSensitive(expectation=True, data="Atak kata", case_sensitive=False),
    ]
    for expectation, data, case_sensitive in test_cases:
        result = is_palindrome(data, case_sensitive, whitespace_sensitive, punctuation_sensitive)
        assert result == expectation, \
            f"Expected '{expectation}', got '{result}' for '{data=}' and "\
            f"options '{case_sensitive=}', '{whitespace_sensitive=}', '{punctuation_sensitive=}'!"


@pytest.mark.parametrize("case_sensitive", [True, False])
@pytest.mark.parametrize("punctuation_sensitive", [True, False])
def test_palindromes_option_whitespace_sensitive(case_sensitive: bool, punctuation_sensitive: bool) -> None:
    TestCaseWhitespaceSensitive = namedtuple(
        typename='TestCaseWhitespaceSensitive',
        field_names=["expectation", "data", "whitespace_sensitive"],
    )
    test_cases = [
        TestCaseWhitespaceSensitive(expectation=False, data="moc owocom", whitespace_sensitive=True),
        TestCaseWhitespaceSensitive(expectation=True, data="moc owocom", whitespace_sensitive=False),
    ]
    for expectation, data, whitespace_sensitive in test_cases:
        result = is_palindrome(data, case_sensitive, whitespace_sensitive, punctuation_sensitive)
        assert result == expectation, \
            f"Expected '{expectation}', got '{result}' for '{data=}' and "\
            f"options '{case_sensitive=}', '{whitespace_sensitive=}', '{punctuation_sensitive=}'!"


@pytest.mark.parametrize("case_sensitive", [True, False])
@pytest.mark.parametrize("whitespace_sensitive", [True, False])
def test_palindromes_option_punctuation_sensitive(case_sensitive: bool, whitespace_sensitive: bool) -> None:
    TestCasePunctuationSensitive = namedtuple(
        typename='TestCasePunctuationSensitive',
        field_names=["expectation", "data", "punctuation_sensitive"],
    )
    test_cases = [
        TestCasePunctuationSensitive(expectation=False, data="atak kata.", punctuation_sensitive=True),
        TestCasePunctuationSensitive(expectation=True, data="atak kata.", punctuation_sensitive=False),
    ]
    for expectation, data, punctuation_sensitive in test_cases:
        result = is_palindrome(data, case_sensitive, whitespace_sensitive, punctuation_sensitive)
        assert result == expectation, \
            f"Expected '{expectation}', got '{result}' for '{data=}' and "\
            f"options '{case_sensitive=}', '{whitespace_sensitive=}', '{punctuation_sensitive=}'!"


def test_palindromes_all_options_mixed() -> None:
    TestCaseAllOptions = namedtuple(
        typename='TestCaseAllOptions',
        field_names=["expectation", "data", "case_sensitive", "whitespace_sensitive", "punctuation_sensitive"]
    )
    test_cases = [
        TestCaseAllOptions(False, "Moc owocom!", case_sensitive=True, whitespace_sensitive=True, punctuation_sensitive=True),
        TestCaseAllOptions(False, "Moc owocom!", case_sensitive=False, whitespace_sensitive=True, punctuation_sensitive=True),
        TestCaseAllOptions(False, "Moc owocom!", case_sensitive=True, whitespace_sensitive=False, punctuation_sensitive=True),
        TestCaseAllOptions(False, "Moc owocom!", case_sensitive=True, whitespace_sensitive=True, punctuation_sensitive=False),
        TestCaseAllOptions(False, "Moc owocom!", case_sensitive=False, whitespace_sensitive=False, punctuation_sensitive=True),
        TestCaseAllOptions(False, "Moc owocom!", case_sensitive=False, whitespace_sensitive=True, punctuation_sensitive=False),
        TestCaseAllOptions(False, "Moc owocom!", case_sensitive=True, whitespace_sensitive=False, punctuation_sensitive=False),
        TestCaseAllOptions(True, "Moc owocom!", case_sensitive=False, whitespace_sensitive=False, punctuation_sensitive=False),
    ]
    for expectation, data, case_sensitive, whitespace_sensitive, punctuation_sensitive in test_cases:
        result = is_palindrome(data, case_sensitive, whitespace_sensitive, punctuation_sensitive)
        assert result == expectation, \
            f"Expected '{expectation}', got '{result}' for '{data=}' and "\
            f"options '{case_sensitive=}', '{whitespace_sensitive=}', '{punctuation_sensitive=}'!"
