from palindrome import is_palindrome


def test_none_is_not_a_palindrome() -> None:
    case, expectation = None, False
    assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"


def test_empty_input_is_a_palindrome() -> None:
    case, expectation = "", True
    assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"
    case, expectation = b"", True
    assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"
    case, expectation = tuple(), True
    assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"
    case, expectation = [], True
    assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"
    case, expectation = bytearray(), True
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


def test_tuple_of_characters() -> None:
    test_cases = {
        ("a", "b", "b", "a"): True,
        ("t", "o", "w", "o", "t"): True,
        ("a", "b", "b", "a", " "): True,
        ("a", "b", "b", "a", "a"): False,
    }
    for case, expectation in test_cases.items():
        assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"


def test_list_of_characters() -> None:
    case, expectation = ["a", "b", "b", "a"], True
    assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"
    case, expectation = ["t", "o", "w", "o", "t"], True
    assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"
    case, expectation = ["a", "b", "b", "a", " "], True
    assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"
    case, expectation = ["a", "b", "b", "a", "a"], False
    assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"


def test_tuple_of_words() -> None:
    test_cases = {
        ("devil", "lived"): True,
        ("sator", "arepo", "tenet", "opera", "rotas"): True,
        ("devil", "lived", "!"): True,
        ("sator", "arepo", "tenet", "arepo", "rotas"): False,
    }
    for case, expectation in test_cases.items():
        assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"


def test_list_of_words() -> None:
    case, expectation = ["devil", "lived"], True
    assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"
    case, expectation = ["sator", "arepo", "tenet", "opera", "rotas"], True
    assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"
    case, expectation = ["devil", "lived", "!"], True
    assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"
    case, expectation = ["sator", "arepo", "tenet", "arepo", "rotas"], False
    assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"


def test_bytes_instead_strings() -> None:
    test_cases = {
        b"abba": True,
        b"towot": True,
        b"abba ": True,
        b"abbaa": False,
    }
    for case, expectation in test_cases.items():
        assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"


def test_bytearray_instead_strings() -> None:
    case, expectation = bytearray("abba", "UTF-8"), True
    assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"
    case, expectation = bytearray("towot", "UTF-8"), True
    assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"
    case, expectation = bytearray("abba ", "UTF-8"), True
    assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"
    case, expectation = bytearray("abbaa", "UTF-8"), False
    assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"


def test_integers() -> None:
    test_cases = {
        0: True,
        1: True,
        11: True,
        121: True,
        12321: True,
        1010101: True,
        10: False,
        12: False,
        112: False,
        123: False,
        13321: False,
        1020101: False,
    }
    for case, expectation in test_cases.items():
        assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"


def test_floats() -> None:
    test_cases = {
        0.0: True,
        1.1: True,
        11.11: True,
        121.121: True,
        123.321: True,
        10101.10101: True,
        1.0: False,
        10.0: False,
        10.1: False,
        123.123: False,
        13.321: False,
        102.0101: False,
    }
    for case, expectation in test_cases.items():
        assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"
