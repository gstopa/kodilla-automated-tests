"""

>>> def run_tests(test_cases):
...     for case, expectation in test_cases.items():
...         assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"

>>> none_is_not_a_palindrome = {
...     None: False,
... }
>>> run_tests(none_is_not_a_palindrome)

>>> empty_input = {
...     "": True,
...     b"": True,
...     tuple(): True,
... }
>>> run_tests(empty_input)
>>> case, expectation = [], True
>>> assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"
>>> case, expectation = bytearray(), True
>>> assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"

>>> string_single_word_palindromes = {
...     # all lower case
...     "abba": True,
...     "anilina": True,
...     "radar": True,
...     "xanax": True,
...     "towot": True,
...     # all upper case
...     "ABBA": True,
...     "ANILINA": True,
...     "RADAR": True,
...     "XANAX": True,
...     "TOWOT": True,
...     # mixed case
...     "Abba": True,
...     "Anilina": True,
...     "Radar": True,
...     "Xanax": True,
...     "TowOt": True,
... }
>>> run_tests(string_single_word_palindromes)

>>> string_single_word_non_palindromes = {
...     # all lower case
...     "aabba": False,
...     "qanilina": False,
...     "raadar": False,
...     "xaxnax": False,
...     "tawot": False,
...     # all upper case
...     "AABBA": False,
...     "QANILINA": False,
...     "RAADAR": False,
...     "XAXNAX": False,
...     "TAWOT": False,
...     # mixed case
...     "Aabba": False,
...     "QAnilina": False,
...     "RaAdar": False,
...     "XaXnax": False,
...     "TAwOt": False,
... }
>>> run_tests(string_single_word_non_palindromes)

>>> string_multiple_word_palindromes_with_same_spacing = {
...     # all lower case
...     "ave eva": True,
...     "sator arepo tenet opera rotas": True,
...     "devil lived": True,
...     # all upper case
...     "AVE EVA": True,
...     "SATOR AREPO TENET OPERA ROTAS": True,
...     "DEVIL LIVED": True,
...     # mixed case
...     "Ave Eva": True,
...     "Sator arepo tenet opera rotas": True,
...     "Devil lived": True,
... }
>>> run_tests(string_multiple_word_palindromes_with_same_spacing)

>>> string_multiple_word_palindromes_with_different_spacing = {
...     # all lower case
...     "do geese see god": True,
...     "was it a cat i saw": True,
...     # all upper case
...     "DO GEESE SEE GOD": True,
...     "WAS IT A CAT I SAW": True,
...     # mixed case
...     "Do geese see God": True,
...     "Was it a cat I saw": True,
... }
>>> run_tests(string_multiple_word_palindromes_with_different_spacing)

>>> string_multiple_word_non_palindromes = {
...     # all lower case
...     "aave eva": False,
...     "sator arepo tneet opera rotas": False,
...     "do geese see good": False,
...     "satan lived": False,
...     "was it a dog i saw": False,
...     # all upper case
...     "AAVE EVA": False,
...     "SATOR AREPO TNEET OPERA ROTAS": False,
...     "DO GEESE SEE GOOD": False,
...     "SATAN LIVED": False,
...     "WAS IT A DOG I SAW": False,
...     # mixed case
...     "AAve Eva": False,
...     "Sator arepo tneet opera rotas": False,
...     "Do geese see Good": False,
...     "Satan lived": False,
...     "Was it a dog I saw": False,
... }
>>> run_tests(string_multiple_word_non_palindromes)

>>> string_single_words_with_surrounding_spaces = {
...     # all lower case
...     " abba": True,
...     "towot ": True,
...     "   abba": True,
...     "towot   ": True,
...     " abba ": True,
...     " towot ": True,
...     "   abba ": True,
...     " towot   ": True,
...     " aabba": False,
...     " aabba ": False,
...     "aabba ": False,
...     # all upper case
...     " ABBA": True,
...     "TOWOT ": True,
...     "   ABBA": True,
...     "TOWOT   ": True,
...     " ABBA ": True,
...     " TOWOT ": True,
...     "   ABBA ": True,
...     " TOWOT   ": True,
...     " AABBA": False,
...     " AABBA ": False,
...     "AABBA ": False,
...     # mixed case
...     " Abba": True,
...     "TowOt ": True,
...     "   Abba": True,
...     "TowOt   ": True,
...     " Abba ": True,
...     " TowOt ": True,
...     "   Abba ": True,
...     " TowOt   ": True,
...     " AAbba": False,
...     " AAbba ": False,
...     "AAbba ": False,
... }
>>> run_tests(string_single_words_with_surrounding_spaces)

>>> string_multiple_words_with_surrounding_spaces = {
...     # all lower case
...     " ave eva": True,
...     "sator arepo tenet opera rotas ": True,
...     " devil lived ": True,
...     " aave eva": False,
...     "aave eva ": False,
...     " aave eva ": False,
...     # all upper case
...     "   AVE EVA": True,
...     "SATOR AREPO TENET OPERA ROTAS   ": True,
...     "   DEVIL LIVED   ": True,
...     " AAVE EVA": False,
...     "AAVE EVA ": False,
...     " AAVE EVA ": False,
...     # mixed case
...     " Ave Eva   ": True,
...     "   Sator arepo tenet opera rotas ": True,
...     "  Devil lived   ": True,
...     " AAve eva": False,
...     "AAve eva ": False,
...     " AAve eva ": False,
... }
>>> run_tests(string_multiple_words_with_surrounding_spaces)

>>> string_single_words_with_surrounding_punctuation = {
...     # all lower case
...     "abba!": True,
...     "towot?": True,
...     "abba.": True,
...     "!towot": True,
...     "?abba": True,
...     ".towot": True,
...     "!towot!": True,
...     "?abba?": True,
...     ".towot.": True,
...     "aabba!": False,
...     "aabba?": False,
...     "aabba.": False,
...     "!aabba": False,
...     "?aabba": False,
...     ".aabba": False,
...     "!aabba!": False,
...     "?aabba?": False,
...     ".aabba.": False,
...     # all upper case
...     "ABBA!": True,
...     "TOWOT?": True,
...     "ABBA.": True,
...     "!TOWOT": True,
...     "?ABBA": True,
...     ".TOWOT": True,
...     "!TOWOT!": True,
...     "?ABBA?": True,
...     ".TOWOT.": True,
...     "AABBA!": False,
...     "AABBA?": False,
...     "AABBA.": False,
...     "!AABBA": False,
...     "?AABBA": False,
...     ".AABBA": False,
...     "!AABBA!": False,
...     "?AABBA?": False,
...     ".AABBA.": False,
...     # mixed case
...     "Abba!": True,
...     "TowOt?": True,
...     "Abba.": True,
...     "!TowOt": True,
...     "?Abba": True,
...     ".TowOt": True,
...     "!TowOt!": True,
...     "?Abba?": True,
...     ".TowOt.": True,
...     "AAbba!": False,
...     "AAbba?": False,
...     "AAbba.": False,
...     "!AAbba": False,
...     "?AAbba": False,
...     ".AAbba": False,
...     "!AAbba!": False,
...     "?AAbba?": False,
...     ".AAbba.": False,
... }
>>> run_tests(string_single_words_with_surrounding_punctuation)

>>> string_multiple_words_with_surrounding_punctuation = {
...     # all lower case
...     "ave eva!": True,
...     "sator arepo tenet opera rotas?": True,
...     "devil lived.": True,
...     "aave eva!": False,
...     "aave eva?": False,
...     "aave eva.": False,
...     # all upper case
...     "!AVE EVA": True,
...     "?SATOR AREPO TENET OPERA ROTAS": True,
...     ".DEVIL LIVED": True,
...     "!AAVE EVA": False,
...     "?AAVE EVA": False,
...     ".AAVE EVA": False,
...     # mixed case
...     "!Ave Eva!": True,
...     "?Sator arepo tenet opera rotas?": True,
...     ".Devil lived.": True,
...     "!AAve eva!": False,
...     "?AAve eva?": False,
...     ".AAve eva.": False,
... }
>>> run_tests(string_multiple_words_with_surrounding_punctuation)

>>> string_single_words_with_surrounding_punctuation_and_spaces = {
...     # all lower case leading space
...     " abba!": True,
...     " towot?": True,
...     " abba.": True,
...     " !towot": True,
...     " ?abba": True,
...     " .towot": True,
...     " !towot!": True,
...     " ?abba?": True,
...     " .towot.": True,
...     " aabba!": False,
...     " aabba?": False,
...     " aabba.": False,
...     " !aabba": False,
...     " ?aabba": False,
...     " .aabba": False,
...     " !aabba!": False,
...     " ?aabba?": False,
...     " .aabba.": False,
...     # all upper case trailing space
...     "ABBA! ": True,
...     "TOWOT? ": True,
...     "ABBA. ": True,
...     "!TOWOT ": True,
...     "?ABBA ": True,
...     ".TOWOT ": True,
...     "!TOWOT! ": True,
...     "?ABBA? ": True,
...     ".TOWOT. ": True,
...     "AABBA! ": False,
...     "AABBA? ": False,
...     "AABBA. ": False,
...     "!AABBA ": False,
...     "?AABBA ": False,
...     ".AABBA ": False,
...     "!AABBA! ": False,
...     "?AABBA? ": False,
...     ".AABBA. ": False,
...     # mixed case both leading and trailing space
...     " Abba! ": True,
...     " TowOt? ": True,
...     " Abba. ": True,
...     " !TowOt ": True,
...     " ?Abba ": True,
...     " .TowOt ": True,
...     " !TowOt! ": True,
...     " ?Abba? ": True,
...     " .TowOt. ": True,
...     " AAbba! ": False,
...     " AAbba? ": False,
...     " AAbba. ": False,
...     " !AAbba ": False,
...     " ?AAbba ": False,
...     " .AAbba ": False,
...     " !AAbba! ": False,
...     " ?AAbba? ": False,
...     " .AAbba. ": False,
... }
>>> run_tests(string_single_words_with_surrounding_punctuation_and_spaces)

>>> string_multiple_words_with_surrounding_punctuation_and_spaces = {
...     # all lower case leading space
...     "   ave eva!": True,
...     "   sator arepo tenet opera rotas?": True,
...     "   devil lived.": True,
...     "   aave eva!": False,
...     "   aave eva?": False,
...     "   aave eva.": False,
...     # all upper case trailing space
...     "!AVE EVA   ": True,
...     "?SATOR AREPO TENET OPERA ROTAS   ": True,
...     ".DEVIL LIVED   ": True,
...     "!AAVE EVA   ": False,
...     "?AAVE EVA   ": False,
...     ".AAVE EVA   ": False,
...     # mixed case both leading and trailing space
...     "   !Ave Eva!   ": True,
...     "   ?Sator arepo tenet opera rotas?   ": True,
...     "   .Devil lived.   ": True,
...     "   !AAve eva!   ": False,
...     "   ?AAve eva?   ": False,
...     "   .AAve eva.   ": False,
... }
>>> run_tests(string_multiple_words_with_surrounding_punctuation_and_spaces)

>>> string_multiple_words_with_inside_punctuation = {
...     "Madam, I'm Adam": True,
...     "Madam in Eden, I'm Adam": True,
...     "Madam in Heaven, I'm Adam": False,
... }
>>> run_tests(string_multiple_words_with_inside_punctuation)

>>> tuple_of_characters = {
...     ("a", "b", "b", "a"): True,
...     ("t", "o", "w", "o", "t"): True,
...     ("a", "b", "b", "a", " "): True,
...     ("a", "b", "b", "a", "a"): False,
... }
>>> run_tests(tuple_of_characters)

# list of characters
>>> case, expectation = ["a", "b", "b", "a"], True
>>> assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"
>>> case, expectation = ["t", "o", "w", "o", "t"], True
>>> assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"
>>> case, expectation = ["a", "b", "b", "a", " "], True
>>> assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"
>>> case, expectation = ["a", "b", "b", "a", "a"], False
>>> assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"

>>> tuple_of_words = {
...     ("devil", "lived"): True,
...     ("sator", "arepo", "tenet", "opera", "rotas"): True,
...     ("devil", "lived", "!"): True,
...     ("sator", "arepo", "tenet", "arepo", "rotas"): False,
... }
>>> run_tests(tuple_of_words)

# list of words
>>> case, expectation = ["devil", "lived"], True
>>> assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"
>>> case, expectation = ["sator", "arepo", "tenet", "opera", "rotas"], True
>>> assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"
>>> case, expectation = ["devil", "lived", "!"], True
>>> assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"
>>> case, expectation = ["sator", "arepo", "tenet", "arepo", "rotas"], False
>>> assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"

>>> bytes_instead_strings = {
...     b"abba": True,
...     b"towot": True,
...     b"abba ": True,
...     b"abbaa": False,
... }
>>> run_tests(bytes_instead_strings)

# bytearray
>>> case, expectation = bytearray("abba", "UTF-8"), True
>>> assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"
>>> case, expectation = bytearray("towot", "UTF-8"), True
>>> assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"
>>> case, expectation = bytearray("abba ", "UTF-8"), True
>>> assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"
>>> case, expectation = bytearray("abbaa", "UTF-8"), False
>>> assert is_palindrome(case) == expectation, f"Expected '{expectation}' for '{case}'!"

>>> integers = {
...     0: True,
...     1: True,
...     11: True,
...     121: True,
...     12321: True,
...     1010101: True,
...     10: False,
...     12: False,
...     112: False,
...     123: False,
...     13321: False,
...     1020101: False,
... }
>>> run_tests(integers)

>>> floats = {
...     0.0: True,
...     1.1: True,
...     11.11: True,
...     121.121: True,
...     123.321: True,
...     10101.10101: True,
...     1.0: False,
...     10.0: False,
...     10.1: False,
...     123.123: False,
...     13.321: False,
...     102.0101: False,
... }
>>> run_tests(floats)

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
