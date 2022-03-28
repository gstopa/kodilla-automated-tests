"""

>>> import sys; sys.tracebacklimit = 0
>>> import pytest
>>> def run_test_cases(test_cases):
...     for board, expectation in test_cases.items():
...         response = tic_tac_toe_winner(board)
...         assert response == expectation, f"Expected {expectation!r} for {board!r} got {response!r}"
>>> def run_invalid_test_cases(test_cases):
...     for board, expectation in test_cases.items():
...         with pytest.raises(expectation):
...             response = tic_tac_toe_winner(board)

>>> test_cases_no_wins = {
...     '   '
...     '   '
...     '   ': None,
...
...     'XOX'
...     'OOX'
...     'XXO': None,
...
...     'XOX'
...     'XOX'
...     'OXO': None,
...
...     'X X'
...     ' O '
...     'X O': None,
...
...     'O X'
...     ' OX'
...     'X  ': None,
... }
>>> run_test_cases(test_cases_no_wins)

>>> test_cases_invalid = {
...     '': ValueError,
...     ' '*8: ValueError,
...     ' '*10: ValueError,
...
...     ' a '
...     '   '
...     '   ': ValueError,
...
...     'x  '
...     '   '
...     '   ': ValueError,
...
...     '  o'
...     '   '
...     '   ': ValueError,
...
...     '   '
...     ' 1 '
...     '   ': ValueError,
...
...     '   '
...     '   '
...     '  0': ValueError,
...
...     'XXX'
...     'XXX'
...     'XXX': ValueError,
...
...     'OOO'
...     'OOO'
...     'OOO': ValueError,
...
...     'XXX'
...     '   '
...     '   ': ValueError,
...
...     '   '
...     'XXX'
...     '   ': ValueError,
...
...     '   '
...     '   '
...     'XXX': ValueError,
...
...     'X  '
...     'X  '
...     'X  ': ValueError,
...
...     ' X '
...     ' X '
...     ' X ': ValueError,
...
...     '  X'
...     '  X'
...     '  X': ValueError,
...
...     'X  '
...     ' X '
...     '  X': ValueError,
...
...     '  X'
...     ' X '
...     'X  ': ValueError,
...
...     'OOO'
...     '   '
...     '   ': ValueError,
...
...     '   '
...     'OOO'
...     '   ': ValueError,
...
...     '   '
...     '   '
...     'OOO': ValueError,
...
...     'O  '
...     'O  '
...     'O  ': ValueError,
...
...     ' O '
...     ' O '
...     ' O ': ValueError,
...
...     '  O'
...     '  O'
...     '  O': ValueError,
...
...     'O  '
...     ' O '
...     '  O': ValueError,
...
...     '  O'
...     ' O '
...     'O  ': ValueError,
...
...     'XXX'
...     'OOO'
...     '   ': ValueError,
... }
>>> run_invalid_test_cases(test_cases_invalid)


>>> test_cases_realistic_short_wins = {
...     'XXX'
...     'OO '
...     '   ': 'X',
...
...     'OO '
...     'XXX'
...     '   ': 'X',
...
...     'OO '
...     '   '
...     'XXX': 'X',
...
...     'XOO'
...     'X  '
...     'X  ': 'X',
...
...     ' X '
...     ' X '
...     'OXO': 'X',
...
...     'OOX'
...     '  X'
...     '  X': 'X',
...
...     'XOO'
...     ' X '
...     '  X': 'X',
...
...     'OOX'
...     ' X '
...     'X  ': 'X',
...
...     'OOO'
...     'XX '
...     'X  ': 'O',
...
...     'XX '
...     'OOO'
...     'X  ': 'O',
...
...     'XX '
...     'X  '
...     'OOO': 'O',
...
...     'OXX'
...     'OX '
...     'O  ': 'O',
...
...     'XOX'
...     'XO '
...     ' O ': 'O',
...
...     'XXO'
...     'X O'
...     '  O': 'O',
...
...     'OXX'
...     'XO '
...     '  O': 'O',
...
...     'XXO'
...     'XO '
...     'O  ': 'O',
... }
>>> run_test_cases(test_cases_realistic_short_wins)


>>> test_cases_realistic_long_single_wins = {
...     'XXX'
...     'XOO'
...     'OXO': 'X',
...
...     'XXX'
...     'XOO'
...     'OOX': 'X',
...
...     'XXX'
...     'OXO'
...     'XOO': 'X',
...
...     'XXX'
...     'OXO'
...     'OOX': 'X',
...
...     'XXX'
...     'OOX'
...     'XOO': 'X',
...
...     'XXX'
...     'OOX'
...     'OXO': 'X',
...
...     'XOO'
...     'XXX'
...     'OXO': 'X',
...
...     'OXO'
...     'XXX'
...     'XOO': 'X',
...
...     'OXO'
...     'XXX'
...     'OOX': 'X',
...
...     'OOX'
...     'XXX'
...     'OXO': 'X',
...
...     'XOO'
...     'OXO'
...     'XXX': 'X',
...
...     'XOO'
...     'OOX'
...     'XXX': 'X',
...
...     'OXO'
...     'XOO'
...     'XXX': 'X',
...
...     'OXO'
...     'OOX'
...     'XXX': 'X',
...
...     'OOX'
...     'XOO'
...     'XXX': 'X',
...
...     'XXO'
...     'XOO'
...     'XOX': 'X',
...
...     'XXO'
...     'XOX'
...     'XOO': 'X',
...
...     'XOX'
...     'XOO'
...     'XXO': 'X',
...
...     'XOO'
...     'XOX'
...     'XXO': 'X',
...
...     'OXX'
...     'XXO'
...     'OXO': 'X',
...
...     'XXO'
...     'OXX'
...     'OXO': 'X',
...
...     'OXO'
...     'OXX'
...     'XXO': 'X',
...
...     'OXO'
...     'XXO'
...     'OXX': 'X',
...
...     'XOX'
...     'OOX'
...     'OXX': 'X',
...
...     'OOX'
...     'XOX'
...     'OXX': 'X',
...
...     'OXX'
...     'XOX'
...     'OOX': 'X',
...
...     'OXX'
...     'OOX'
...     'XOX': 'X',
...
...     'XXO'
...     'OXO'
...     'XOX': 'X',
...
...     'XOX'
...     'OXO'
...     'XXO': 'X',
...
...     'OOO'
...     ' XX'
...     'XOX': 'O',
...
...     ' XX'
...     'OOO'
...     'XOX': 'O',
...
...     ' XX'
...     'XOX'
...     'OOO': 'O',
...
...     'OXX'
...     'OO '
...     'OXX': 'O',
...
...     'XOX'
...     'OO '
...     'XOX': 'O',
...
...     'XXO'
...     ' OO'
...     'XXO': 'O',
...
...     'OXO'
...     ' OX'
...     'XXO': 'O',
...
...     'OXO'
...     ' OX'
...     'OXX': 'O',
... }
>>> run_test_cases(test_cases_realistic_long_single_wins)

"""

from typing import Optional, Set


def tic_tac_toe_winner(board: str) -> Optional[str]:
    """

    :param board:
        9 element string of 'x', 'o', and ' ' (space) representation of game board;
        first 3 elements are the first row,
        second 3 elements are the second row,
        third 3 elements are the third row.

    :return:
        'X' when xes won,
        'O' when oes won,
        None when neither won
    """
    def is_correct_length(board: str) -> bool:
        return len(board) == 9

    def is_correct_characters(board: str) -> bool:
        possible_characters = {' ', 'X', 'O'}
        return set(board) | possible_characters == possible_characters

    def is_correct_number_of_xes_and_oes(board: str) -> bool:
        number_of_xes = board.count('X')
        number_of_oes = board.count('O')
        if (number_of_xes - number_of_oes == 0
                or number_of_xes - number_of_oes == 1):
            return True
        return False

    def get_winner(x: str) -> Optional[str]:
        counter: Set[str] = set(x)
        if len(counter) == 1:
            a_winner: str = counter.pop()
            if a_winner == ' ':
                return None
            return a_winner
        return None

    if not is_correct_length(board):
        raise ValueError(f"Invalid length!\nExpected 9 elements; got {len(board)}!")
    if not is_correct_characters(board):
        raise ValueError(f"Invalid characters found!\nExpected only ' ', 'X', 'O'; got '{board}'!")
    if not is_correct_number_of_xes_and_oes(board):
        raise ValueError(
            "Invalid number of Xes and Oes!\n"
            "Expected that there are the same number of both or one more 'X'; "
            f"got {board.count('X')} X(es) and {board.count('O')} O(es)!"
        )

    winner_possibilities = [
        get_winner(board[0:3]),  # row 1
        get_winner(board[3:6]),  # row 2
        get_winner(board[6:9]),  # row 3
        get_winner(board[0::3]),  # column 1
        get_winner(board[1::3]),  # column 2
        get_winner(board[2::3]),  # column 3
        get_winner(board[0::4]),  # diagonal NW-SE
        get_winner(board[2:7:2]),  # diagonal NE-SW
    ]
    x_wins = True if 'X' in winner_possibilities else False
    o_wins = True if 'O' in winner_possibilities else False
    if x_wins and o_wins:
        raise ValueError(f"Invalid board!\nExpected Xes or Oes to win; got both wins '{board}'!")
    if x_wins:
        return 'X'
    if o_wins:
        return 'O'
    return None
