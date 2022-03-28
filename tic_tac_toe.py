"""

>>> import sys; sys.tracebacklimit = 0
>>> def run_test_cases(test_cases):
...     for board, expectation in test_cases.items():
...         response = tic_tac_toe_winner(board)
...         assert response == expectation, f"Expected {expectation!r} for {board!r} got {response!r}"

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

# Unrealistic scenarios that can be interpreted as X or O win
# So most probably those should be some exceptions
>>> test_cases_unrealistic_wins = {
...     'XXX'
...     '   '
...     '   ': 'X',
...
...     '   '
...     'XXX'
...     '   ': 'X',
...
...     '   '
...     '   '
...     'XXX': 'X',
...
...     'X  '
...     'X  '
...     'X  ': 'X',
...
...     ' X '
...     ' X '
...     ' X ': 'X',
...
...     '  X'
...     '  X'
...     '  X': 'X',
...
...     'X  '
...     ' X '
...     '  X': 'X',
...
...     '  X'
...     ' X '
...     'X  ': 'X',
...
...     'OOO'
...     '   '
...     '   ': 'O',
...
...     '   '
...     'OOO'
...     '   ': 'O',
...
...     '   '
...     '   '
...     'OOO': 'O',
...
...     'O  '
...     'O  '
...     'O  ': 'O',
...
...     ' O '
...     ' O '
...     ' O ': 'O',
...
...     '  O'
...     '  O'
...     '  O': 'O',
...
...     'O  '
...     ' O '
...     '  O': 'O',
...
...     '  O'
...     ' O '
...     'O  ': 'O',
... }
>>> run_test_cases(test_cases_unrealistic_wins)


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
    def get_winner(x: str) -> Optional[str]:
        counter: Set[str] = set(x)
        if len(counter) == 1:
            a_winner: str = counter.pop()
            if a_winner == ' ':
                return None
            return a_winner
        return None

    if winner := get_winner(board[0:3]):
        return winner
    if winner := get_winner(board[3:6]):
        return winner
    if winner := get_winner(board[6:9]):
        return winner
    if winner := get_winner(board[0::3]):
        return winner
    if winner := get_winner(board[1::3]):
        return winner
    if winner := get_winner(board[2::3]):
        return winner
    if winner := get_winner(board[0::4]):
        return winner
    if winner := get_winner(board[2:7:2]):
        return winner
    return None
