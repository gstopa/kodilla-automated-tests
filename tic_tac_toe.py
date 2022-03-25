"""

# No wins
# Empty board
>>> tic_tac_toe_winner(board_state='         ')

# Long no wins
>>> tic_tac_toe_winner(board_state='xoxooxxxo')
>>> tic_tac_toe_winner(board_state='xoxxoxoxo')

# 5 moves no wins
>>> tic_tac_toe_winner(board_state='x x o x o')
>>> tic_tac_toe_winner(board_state='o x oxx  ')

# Unrealistic scenarios that can be interpreted as X or O win
# So most probably those should be some exceptions
>>> tic_tac_toe_winner(board_state='xxx      ')
'X'
>>> tic_tac_toe_winner(board_state='   xxx   ')
'X'
>>> tic_tac_toe_winner(board_state='      xxx')
'X'
>>> tic_tac_toe_winner(board_state='ooo      ')
'O'
>>> tic_tac_toe_winner(board_state='   ooo   ')
'O'
>>> tic_tac_toe_winner(board_state='      ooo')
'O'
>>> tic_tac_toe_winner(board_state='x  x  x  ')
'X'
>>> tic_tac_toe_winner(board_state=' x  x  x ')
'X'
>>> tic_tac_toe_winner(board_state='  x  x  x')
'X'
>>> tic_tac_toe_winner(board_state='o  o  o  ')
'O'
>>> tic_tac_toe_winner(board_state=' o  o  o ')
'O'
>>> tic_tac_toe_winner(board_state='  o  o  o')
'O'
>>> tic_tac_toe_winner(board_state='x   x   x')
'X'
>>> tic_tac_toe_winner(board_state='  x x x  ')
'X'
>>> tic_tac_toe_winner(board_state='o   o   o')
'O'
>>> tic_tac_toe_winner(board_state='  o o o  ')
'O'

# Realistic short wins
# Xes row wins
>>> tic_tac_toe_winner(board_state='xxxoo    ')
'X'
>>> tic_tac_toe_winner(board_state='oo xxx   ')
'X'
>>> tic_tac_toe_winner(board_state='oo    xxx')
'X'

# Oes row wins
>>> tic_tac_toe_winner(board_state='oooxx x  ')
'O'
>>> tic_tac_toe_winner(board_state='xx ooox  ')
'O'
>>> tic_tac_toe_winner(board_state='xx x  ooo')
'O'

# Xes column wins
>>> tic_tac_toe_winner(board_state='xoox  x  ')
'X'
>>> tic_tac_toe_winner(board_state=' x  x oxo')
'X'
>>> tic_tac_toe_winner(board_state='oox  x  x')
'X'

# Oes column wins
>>> tic_tac_toe_winner(board_state='oxxox o  ')
'O'
>>> tic_tac_toe_winner(board_state='xoxxo  o ')
'O'
>>> tic_tac_toe_winner(board_state='xxox o  o')
'O'

# Xes diagonal wins
>>> tic_tac_toe_winner(board_state='xoo x   x')
'X'
>>> tic_tac_toe_winner(board_state='oox x x  ')
'X'

# Oes diagonal wins
>>> tic_tac_toe_winner(board_state='oxxxo   o')
'O'
>>> tic_tac_toe_winner(board_state='xxoxo o  ')
'O'

# Realistic long single wins
# Xes row wins
>>> tic_tac_toe_winner(board_state='xxxxoooxo')
'X'
>>> tic_tac_toe_winner(board_state='xxxxoooox')
'X'
>>> tic_tac_toe_winner(board_state='xxxoxoxoo')
'X'
>>> tic_tac_toe_winner(board_state='xxxoxooox')
'X'
>>> tic_tac_toe_winner(board_state='xxxooxxoo')
'X'
>>> tic_tac_toe_winner(board_state='xxxooxoxo')
'X'
>>> tic_tac_toe_winner(board_state='xooxxxoxo')
'X'
>>> tic_tac_toe_winner(board_state='oxoxxxxoo')
'X'
>>> tic_tac_toe_winner(board_state='oxoxxxoox')
'X'
>>> tic_tac_toe_winner(board_state='ooxxxxoxo')
'X'
>>> tic_tac_toe_winner(board_state='xoooxoxxx')
'X'
>>> tic_tac_toe_winner(board_state='xooooxxxx')
'X'
>>> tic_tac_toe_winner(board_state='oxoxooxxx')
'X'
>>> tic_tac_toe_winner(board_state='oxoooxxxx')
'X'
>>> tic_tac_toe_winner(board_state='ooxxooxxx')
'X'
>>> tic_tac_toe_winner(board_state='ooxoxoxxx')
'X'

# Xes column wins
>>> tic_tac_toe_winner(board_state='xxoxooxox')
'X'
>>> tic_tac_toe_winner(board_state='xxoxoxxoo')
'X'
>>> tic_tac_toe_winner(board_state='xoxxooxxo')
'X'
>>> tic_tac_toe_winner(board_state='xooxoxxxo')
'X'
>>> tic_tac_toe_winner(board_state='oxxxxooxo')
'X'
>>> tic_tac_toe_winner(board_state='xxooxxoxo')
'X'
>>> tic_tac_toe_winner(board_state='oxooxxxxo')
'X'
>>> tic_tac_toe_winner(board_state='oxoxxooxx')
'X'
>>> tic_tac_toe_winner(board_state='xoxooxoxx')
'X'
>>> tic_tac_toe_winner(board_state='ooxxoxoxx')
'X'
>>> tic_tac_toe_winner(board_state='oxxxoxoox')
'X'
>>> tic_tac_toe_winner(board_state='oxxooxxox')
'X'

# Oes row wins
>>> tic_tac_toe_winner(board_state='ooo xxxox')
'O'
>>> tic_tac_toe_winner(board_state=' xxoooxox')
'O'
>>> tic_tac_toe_winner(board_state=' xxxoxooo')
'O'

# Oes column wins
>>> tic_tac_toe_winner(board_state='oxxoo oxx')
'O'
>>> tic_tac_toe_winner(board_state='xoxoo xox')
'O'
>>> tic_tac_toe_winner(board_state='xxo ooxxo')
'O'

# Xes diagonal wins
>>> tic_tac_toe_winner(board_state='xxooxoxox')
'X'
>>> tic_tac_toe_winner(board_state='xoxoxoxxo')
'X'

# Oes diagonal wins
>>> tic_tac_toe_winner(board_state='oxo oxxxo')
'O'
>>> tic_tac_toe_winner(board_state='oxo oxoxx')
'O'


"""

from typing import Optional, Set


def tic_tac_toe_winner(board_state: str) -> Optional[str]:
    """

    :param board_state:
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
            return a_winner.upper()
        return None

    if winner := get_winner(board_state[0:3]):
        return winner
    if winner := get_winner(board_state[3:6]):
        return winner
    if winner := get_winner(board_state[6:9]):
        return winner
    if winner := get_winner(board_state[0::3]):
        return winner
    if winner := get_winner(board_state[1::3]):
        return winner
    if winner := get_winner(board_state[2::3]):
        return winner
    if winner := get_winner(board_state[0::4]):
        return winner
    if winner := get_winner(board_state[2:7:2]):
        return winner
    return None
