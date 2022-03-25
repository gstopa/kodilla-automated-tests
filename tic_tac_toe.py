"""

>>> import sys; sys.tracebacklimit = 0
>>> def run_test_cases(test_cases):
...     for board, expectation in test_cases.items():
...         response = tic_tac_toe_winner(board)
...         assert response == expectation, f"Expected {expectation!r} for {board!r} got {response!r}"

>>> test_cases_no_wins = {
...     '         ': None,
...     'XOXOOXXXO': None,
...     'XOXXOXOXO': None,
...     'X X O X O': None,
...     'O X OXX  ': None,
... }
>>> run_test_cases(test_cases_no_wins)

# Unrealistic scenarios that can be interpreted as X or O win
# So most probably those should be some exceptions
>>> test_cases_unrealistic_wins = {
...     'XXX      ': 'X',
...     '   XXX   ': 'X',
...     '      XXX': 'X',
...     'X  X  X  ': 'X',
...     ' X  X  X ': 'X',
...     '  X  X  X': 'X',
...     'X   X   X': 'X',
...     '  X X X  ': 'X',
...     'OOO      ': 'O',
...     '   OOO   ': 'O',
...     '      OOO': 'O',
...     'O  O  O  ': 'O',
...     ' O  O  O ': 'O',
...     '  O  O  O': 'O',
...     'O   O   O': 'O',
...     '  O O O  ': 'O',
... }
>>> run_test_cases(test_cases_unrealistic_wins)


>>> test_cases_realistic_short_wins = {
...     'XXXOO    ': 'X',
...     'OO XXX   ': 'X',
...     'OO    XXX': 'X',
...     'XOOX  X  ': 'X',
...     ' X  X OXO': 'X',
...     'OOX  X  X': 'X',
...     'XOO X   X': 'X',
...     'OOX X X  ': 'X',
...     'OOOXX X  ': 'O',
...     'XX OOOX  ': 'O',
...     'XX X  OOO': 'O',
...     'OXXOX O  ': 'O',
...     'XOXXO  O ': 'O',
...     'XXOX O  O': 'O',
...     'OXXXO   O': 'O',
...     'XXOXO O  ': 'O',
... }
>>> run_test_cases(test_cases_realistic_short_wins)


>>> test_cases_realistic_long_single_wins = {
...     'XXXXOOOXO': 'X',
...     'XXXXOOOOX': 'X',
...     'XXXOXOXOO': 'X',
...     'XXXOXOOOX': 'X',
...     'XXXOOXXOO': 'X',
...     'XXXOOXOXO': 'X',
...     'XOOXXXOXO': 'X',
...     'OXOXXXXOO': 'X',
...     'OXOXXXOOX': 'X',
...     'OOXXXXOXO': 'X',
...     'XOOOXOXXX': 'X',
...     'XOOOOXXXX': 'X',
...     'OXOXOOXXX': 'X',
...     'OXOOOXXXX': 'X',
...     'OOXXOOXXX': 'X',
...     'XXOXOOXOX': 'X',
...     'XXOXOXXOO': 'X',
...     'XOXXOOXXO': 'X',
...     'XOOXOXXXO': 'X',
...     'OXXXXOOXO': 'X',
...     'XXOOXXOXO': 'X',
...     'OXOOXXXXO': 'X',
...     'OXOXXOOXX': 'X',
...     'XOXOOXOXX': 'X',
...     'OOXXOXOXX': 'X',
...     'OXXXOXOOX': 'X',
...     'OXXOOXXOX': 'X',
...     'XXOOXOXOX': 'X',
...     'XOXOXOXXO': 'X',
...     'OOO XXXOX': 'O',
...     ' XXOOOXOX': 'O',
...     ' XXXOXOOO': 'O',
...     'OXXOO OXX': 'O',
...     'XOXOO XOX': 'O',
...     'XXO OOXXO': 'O',
...     'OXO OXXXO': 'O',
...     'OXO OXOXX': 'O',
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
