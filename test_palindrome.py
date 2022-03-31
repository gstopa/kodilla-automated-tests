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
        "abba": True,
        "anilina": True,
        "radar": True,
        "xanax": True,
        "towot": True,
        # all upper case
        "ABBA": True,
        "ANILINA": True,
        "RADAR": True,
        "XANAX": True,
        "TOWOT": True,
        # mixed case
        "Abba": True,
        "Anilina": True,
        "Radar": True,
        "Xanax": True,
        "TowOt": True,
    }
    for case, expectation in test_cases.items():
        assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"


def test_string_single_word_non_palindromes() -> None:
    test_cases = {
        # all lower case
        "aabba": False,
        "qanilina": False,
        "raadar": False,
        "xaxnax": False,
        "tawot": False,
        # all upper case
        "AABBA": False,
        "QANILINA": False,
        "RAADAR": False,
        "XAXNAX": False,
        "TAWOT": False,
        # mixed case
        "Aabba": False,
        "QAnilina": False,
        "RaAdar": False,
        "XaXnax": False,
        "TAwOt": False,
    }
    for case, expectation in test_cases.items():
        assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"


def test_string_multiple_word_palindromes_with_same_spacing() -> None:
    test_cases = {
        # all lower case
        "ave eva": True,
        "sator arepo tenet opera rotas": True,
        "devil lived": True,
        # all upper case
        "AVE EVA": True,
        "SATOR AREPO TENET OPERA ROTAS": True,
        "DEVIL LIVED": True,
        # mixed case
        "Ave Eva": True,
        "Sator arepo tenet opera rotas": True,
        "Devil lived": True,
    }
    for case, expectation in test_cases.items():
        assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"


def test_string_multiple_word_palindromes_with_different_spacing() -> None:
    test_cases = {
        # all lower case
        "do geese see god": True,
        "was it a cat i saw": True,
        # all upper case
        "DO GEESE SEE GOD": True,
        "WAS IT A CAT I SAW": True,
        # mixed case
        "Do geese see God": True,
        "Was it a cat I saw": True,
    }
    for case, expectation in test_cases.items():
        assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"


def test_string_multiple_word_non_palindromes() -> None:
    test_cases = {
        # all lower case
        "aave eva": False,
        "sator arepo tneet opera rotas": False,
        "do geese see good": False,
        "satan lived": False,
        "was it a dog i saw": False,
        # all upper case
        "AAVE EVA": False,
        "SATOR AREPO TNEET OPERA ROTAS": False,
        "DO GEESE SEE GOOD": False,
        "SATAN LIVED": False,
        "WAS IT A DOG I SAW": False,
        # mixed case
        "AAve Eva": False,
        "Sator arepo tneet opera rotas": False,
        "Do geese see Good": False,
        "Satan lived": False,
        "Was it a dog I saw": False,
    }
    for case, expectation in test_cases.items():
        assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"


def test_string_single_words_with_surrounding_spaces() -> None:
    test_cases = {
        # all lower case
        " abba": True,
        "towot ": True,
        "   abba": True,
        "towot   ": True,
        " abba ": True,
        " towot ": True,
        "   abba ": True,
        " towot   ": True,
        " aabba": False,
        " aabba ": False,
        "aabba ": False,
        # all upper case
        " ABBA": True,
        "TOWOT ": True,
        "   ABBA": True,
        "TOWOT   ": True,
        " ABBA ": True,
        " TOWOT ": True,
        "   ABBA ": True,
        " TOWOT   ": True,
        " AABBA": False,
        " AABBA ": False,
        "AABBA ": False,
        # mixed case
        " Abba": True,
        "TowOt ": True,
        "   Abba": True,
        "TowOt   ": True,
        " Abba ": True,
        " TowOt ": True,
        "   Abba ": True,
        " TowOt   ": True,
        " AAbba": False,
        " AAbba ": False,
        "AAbba ": False,
    }
    for case, expectation in test_cases.items():
        assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"


def test_string_multiple_words_with_surrounding_spaces() -> None:
    test_cases = {
        # all lower case
        " ave eva": True,
        "sator arepo tenet opera rotas ": True,
        " devil lived ": True,
        " aave eva": False,
        "aave eva ": False,
        " aave eva ": False,
        # all upper case
        "   AVE EVA": True,
        "SATOR AREPO TENET OPERA ROTAS   ": True,
        "   DEVIL LIVED   ": True,
        " AAVE EVA": False,
        "AAVE EVA ": False,
        " AAVE EVA ": False,
        # mixed case
        " Ave Eva   ": True,
        "   Sator arepo tenet opera rotas ": True,
        "  Devil lived   ": True,
        " AAve eva": False,
        "AAve eva ": False,
        " AAve eva ": False,
    }
    for case, expectation in test_cases.items():
        assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"


def test_string_single_words_with_surrounding_punctuation() -> None:
    test_cases = {
        # all lower case
        "abba!": True,
        "towot?": True,
        "abba.": True,
        "!towot": True,
        "?abba": True,
        ".towot": True,
        "!towot!": True,
        "?abba?": True,
        ".towot.": True,
        "aabba!": False,
        "aabba?": False,
        "aabba.": False,
        "!aabba": False,
        "?aabba": False,
        ".aabba": False,
        "!aabba!": False,
        "?aabba?": False,
        ".aabba.": False,
        # all upper case
        "ABBA!": True,
        "TOWOT?": True,
        "ABBA.": True,
        "!TOWOT": True,
        "?ABBA": True,
        ".TOWOT": True,
        "!TOWOT!": True,
        "?ABBA?": True,
        ".TOWOT.": True,
        "AABBA!": False,
        "AABBA?": False,
        "AABBA.": False,
        "!AABBA": False,
        "?AABBA": False,
        ".AABBA": False,
        "!AABBA!": False,
        "?AABBA?": False,
        ".AABBA.": False,
        # mixed case
        "Abba!": True,
        "TowOt?": True,
        "Abba.": True,
        "!TowOt": True,
        "?Abba": True,
        ".TowOt": True,
        "!TowOt!": True,
        "?Abba?": True,
        ".TowOt.": True,
        "AAbba!": False,
        "AAbba?": False,
        "AAbba.": False,
        "!AAbba": False,
        "?AAbba": False,
        ".AAbba": False,
        "!AAbba!": False,
        "?AAbba?": False,
        ".AAbba.": False,
    }
    for case, expectation in test_cases.items():
        assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"


def test_string_multiple_words_with_surrounding_punctuation() -> None:
    test_cases = {
        # all lower case
        "ave eva!": True,
        "sator arepo tenet opera rotas?": True,
        "devil lived.": True,
        "aave eva!": False,
        "aave eva?": False,
        "aave eva.": False,
        # all upper case
        "!AVE EVA": True,
        "?SATOR AREPO TENET OPERA ROTAS": True,
        ".DEVIL LIVED": True,
        "!AAVE EVA": False,
        "?AAVE EVA": False,
        ".AAVE EVA": False,
        # mixed case
        "!Ave Eva!": True,
        "?Sator arepo tenet opera rotas?": True,
        ".Devil lived.": True,
        "!AAve eva!": False,
        "?AAve eva?": False,
        ".AAve eva.": False,
    }
    for case, expectation in test_cases.items():
        assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"


def test_string_single_words_with_surrounding_punctuation_and_spaces    () -> None:
    test_cases = {
        # all lower case leading space
        " abba!": True,
        " towot?": True,
        " abba.": True,
        " !towot": True,
        " ?abba": True,
        " .towot": True,
        " !towot!": True,
        " ?abba?": True,
        " .towot.": True,
        " aabba!": False,
        " aabba?": False,
        " aabba.": False,
        " !aabba": False,
        " ?aabba": False,
        " .aabba": False,
        " !aabba!": False,
        " ?aabba?": False,
        " .aabba.": False,
        # all upper case trailing space
        "ABBA! ": True,
        "TOWOT? ": True,
        "ABBA. ": True,
        "!TOWOT ": True,
        "?ABBA ": True,
        ".TOWOT ": True,
        "!TOWOT! ": True,
        "?ABBA? ": True,
        ".TOWOT. ": True,
        "AABBA! ": False,
        "AABBA? ": False,
        "AABBA. ": False,
        "!AABBA ": False,
        "?AABBA ": False,
        ".AABBA ": False,
        "!AABBA! ": False,
        "?AABBA? ": False,
        ".AABBA. ": False,
        # mixed case both leading and trailing space
        " Abba! ": True,
        " TowOt? ": True,
        " Abba. ": True,
        " !TowOt ": True,
        " ?Abba ": True,
        " .TowOt ": True,
        " !TowOt! ": True,
        " ?Abba? ": True,
        " .TowOt. ": True,
        " AAbba! ": False,
        " AAbba? ": False,
        " AAbba. ": False,
        " !AAbba ": False,
        " ?AAbba ": False,
        " .AAbba ": False,
        " !AAbba! ": False,
        " ?AAbba? ": False,
        " .AAbba. ": False,
    }
    for case, expectation in test_cases.items():
        assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"


def test_string_multiple_words_with_surrounding_punctuation_and_spaces() -> None:
    test_cases = {
        # all lower case leading space
        "   ave eva!": True,
        "   sator arepo tenet opera rotas?": True,
        "   devil lived.": True,
        "   aave eva!": False,
        "   aave eva?": False,
        "   aave eva.": False,
        # all upper case trailing space
        "!AVE EVA   ": True,
        "?SATOR AREPO TENET OPERA ROTAS   ": True,
        ".DEVIL LIVED   ": True,
        "!AAVE EVA   ": False,
        "?AAVE EVA   ": False,
        ".AAVE EVA   ": False,
        # mixed case both leading and trailing space
        "   !Ave Eva!   ": True,
        "   ?Sator arepo tenet opera rotas?   ": True,
        "   .Devil lived.   ": True,
        "   !AAve eva!   ": False,
        "   ?AAve eva?   ": False,
        "   .AAve eva.   ": False,
    }
    for case, expectation in test_cases.items():
        assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"


def test_string_multiple_words_with_inside_punctuation() -> None:
    test_cases = {
        "Madam, I'm Adam": True,
        "Madam in Eden, I'm Adam": True,
        "Madam in Heaven, I'm Adam": False,
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
