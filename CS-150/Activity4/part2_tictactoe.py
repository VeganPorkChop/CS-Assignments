"""
Original author: Graham Giblert-Schroeer
Reviewed by: Anastasia Kurdia
Last modified: 02/02/2026

A series of functions related to tic-tac-toe to practice with nested loops
"""

import copy  # used for testing


def board_to_string(board):
    """Creates a formatted string of the given board for printing

    Args:
        board (list[list[str]]): a square table containing only ' ', 'X', and 'O'

    Returns:
        str: a string representation of board
    """
    # Implemented for you to help with experimenting/debugging
    cols = len(board[0])  # all rows must be the same length
    result = ''

    dashes = '-' * (cols * 4 + 1)  # a line of dashes
    for row in board:
        # convert the entire row into a nicely formatted string
        # note the use of join to separate columns
        result += dashes + '\n'
        result += f'| {" | ".join(row)} |\n'
    result += dashes

    return result


def count_xs(board):
    """Calculates the number of 'X' letters in the board

    board is not changed

    Args:
        board (list[list[str]]): a square table containing only ' ', 'X', and 'O'

    Returns:
        int: the number of 'X' letters on the board
    """
    total = 0
    for row in board:
        for char in row:
            if char == 'X':
                total+=1
    return total


def count_os(board):
    """Calculates the number of 'O' letters in the board

    board is not changed

    Args:
        board (list[list[str]]): a square table containing only ' ', 'X', and 'O'

    Returns:
        int: the number of 'O' letters on the board
    """
    total = 0
    for row in board:
        for char in row:
            if char == 'O':
                total+=1
    return total


def is_valid_board(board):
    """Returns whether or not board is a valid tic-tac-toe board

    board is not changed

    A board can only be valid if there are 0 or 1 more Xs than Os
    (Note: we assume that the board is square and contains only letters,
           so this is not part of the definition of "valid board")

    Args:
        board (list[list[str]]): a square table containing only ' ', 'X', and 'O'

    Returns:
        bool: True if board is a valid board, and False otherwise

    """
    
    return (count_xs(board)-count_os(board) == 0 or count_xs(board)-count_os(board) == 1)


def is_row_win(board, player):
    """Returns whether or not player has a winning row

    board is not changed

    A player has a winning row if every symbol on a single row belongs to that player

    Args:
        board (list[list[str]]): a square table containing only ' ', 'X', and 'O'
        player (str): a character 'X' or 'O' indicating which player we are checking

    Returns:
        bool: True if player has a winning row, and false otherwise
    """
    return_val = False
    for row in board:
        for char in row:
            return_val = True
            if char !=player:
                return_val = False
                break
        if return_val:
            return return_val


    return return_val


def is_col_win(board, player):
    """Returns whether or not player has a winning column

    board is not changed

    A player has a winning column if every symbol on a single column belongs to that player

    Args:
        board (list[list[str]]): a square table containing only ' ', 'X', and 'O'
        player (str): a character 'X' or 'O' indicating which player we are checking

    Returns:
        bool: True if player has a winning column, and false otherwise
    """
    return_val = False

    new_board =[[0 for _ in range(len(board[0]))] for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[i])):
            new_board[j][i] = board[i][j]

    for col in new_board:
        for char in col:
            return_val = True
            if char != player:
                return_val = False
                break
        if return_val:
            return return_val
    return False


def is_diag_win(board, player):
    """Returns whether or not player has a winning diagonal

    board is not changed

    A player has a winning diagonal if every symbol on a single diagonal belongs to that player
    Note that we only consider diagonals from the upper-left to lower-right
      or from the upper-right to the lower-left of the table for this function

    Args:
        board (list[list[str]]): a square table containing only ' ', 'X', and 'O'
        player (str): a character 'X' or 'O' indicating which player we are checking

    Returns:
        bool: True if player has a winning diagonal, and false otherwise
    """
    return_val_a = False
    for i in range(len(board)):
        return_val_a = True
        if board[i][i] != player:
            return_val_a = False
            break

    return_val_b = False
    for i in range(len(board)):
        return_val_b = True
        if board[len(board)-i-1][i] != player:
            return_val_b = False
            break

    return return_val_a or return_val_b


def winning_player(board):
    """Returns which player has won the game, or an empty string if neither has won

    board is not changed

    A player wins tic-tac-toe if they have a winning row, column, or diagonal
    If the board is invalid, then neither player is considered to have won
    If both players would be considered to have won, return X

    Args:
        board (list[list[str]]): a square table containing only ' ', 'X', and 'O'

    Returns:
        str: 'X' if the 'X' player won, 'O' if the 'O' player won, or ' ' otherwise
    """
    return_val = ' '
    if is_valid_board(board) and (is_row_win(board, 'X') or is_col_win(board, 'X') or is_diag_win(board, 'X')):
        return_val = 'X'
    elif is_valid_board(board) and (is_row_win(board, 'O') or is_col_win(board, 'O') or is_diag_win(board, 'O')):
        return_val = 'O'
    return return_val


# ---------------------------------------------------------------
# Test cases
# These are implemented for you
# ---------------------------------------------------------------


def test_board_to_string():
    """
    Test cases for board_to_string
    """
    fn_name = 'board_to_string'

    inp = [['X', 'X', 'O'], [' ', ' ', 'X'], ['O', ' ', ' ']]
    # note the formatting without extra spacing
    expected = '''
-------------
| X | X | O |
-------------
|   |   | X |
-------------
| O |   |   |
-------------
'''.strip()
    result = board_to_string(inp)
    assert expected == result, f'expected {expected} for {fn_name}({inp}), got {result}'

    inp = [['X']]
    # note the formatting without extra spacing
    expected = '''
-----
| X |
-----
'''.strip()
    result = board_to_string(inp)
    assert expected == result, f'expected {expected} for {fn_name}({inp}), got {result}'

    inp = [['X', 'O', 'X', 'O'], ['O', 'X', 'O', 'X'],
           [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
    # note the formatting without extra spacing
    expected = '''
-----------------
| X | O | X | O |
-----------------
| O | X | O | X |
-----------------
|   |   |   |   |
-----------------
|   |   |   |   |
-----------------
'''.strip()
    result = board_to_string(inp)
    error_message = f'expected {expected} for {fn_name}({inp}), got {result}'
    assert expected == result, error_message

    print(f'tests for {fn_name} passed')


def test_count_xs():
    """
    Test cases for count_xs
    """
    fn_name = 'count_xs'
    arg_name = 'board'

    # Test basic case
    inp = [['X', 'X', 'O'],
           [' ', ' ', 'X'],
           ['O', ' ', ' ']]
    expected = 3
    original = copy.deepcopy(inp)

    result = count_xs(inp)
    assert expected == result, f'expected {expected} for {fn_name}({original}), got {result}'
    assert original == inp, f'{arg_name} was modified in {fn_name}, now contains {inp}'

    # Test single-element board
    inp = [['X']]
    expected = 1
    original = copy.deepcopy(inp)

    result = count_xs(inp)
    assert expected == result, f'expected {expected} for {fn_name}({original}), got {result}'
    assert original == inp, f'{arg_name} was modified in {fn_name}, now contains {inp}'

    # Test only Os and spaces
    inp = [['O', 'O'],
           [' ', 'O']]
    expected = 0
    original = copy.deepcopy(inp)

    result = count_xs(inp)
    assert expected == result, f'expected {expected} for {fn_name}({original}), got {result}'
    assert original == inp, f'{arg_name} was modified in {fn_name}, now contains {inp}'

    print(f'tests for {fn_name} passed')


def test_count_os():
    """
    Test cases for count_os
    """
    fn_name = 'count_os'
    arg_name = 'board'

    # Test basic case
    expected = 2
    inp = [['X', 'X', 'O'],
           [' ', ' ', 'X'],
           ['O', ' ', ' ']]
    original = copy.deepcopy(inp)

    result = count_os(inp)
    assert expected == result, f'expected {expected} for {fn_name}({original}), got {result}'
    assert original == inp, f'{arg_name} was modified in {fn_name}, now contains {inp}'

    # Test single-element board
    expected = 0
    inp = [['X']]
    original = copy.deepcopy(inp)

    result = count_os(inp)
    assert expected == result, f'expected {expected} for {fn_name}({original}), got {result}'
    assert original == inp, f'{arg_name} was modified in {fn_name}, now contains {inp}'

    # Test only Os and spaces
    expected = 3
    inp = [['O', 'O'],
           [' ', 'O']]
    original = copy.deepcopy(inp)

    result = count_os(inp)
    assert expected == result, f'expected {expected} for {fn_name}({original}), got {result}'
    assert original == inp, f'{arg_name} was modified in {fn_name}, now contains {inp}'

    print(f'tests for {fn_name} passed')


def test_is_valid_board():
    """
    Test cases for is_valid_board
    """
    fn_name = 'is_valid_board'
    arg_name = 'board'

    # Test basic case
    inp = [['X', 'X', 'O'],
           [' ', 'O', 'X'],
           ['O', ' ', ' ']]
    expected = True
    original = copy.deepcopy(inp)

    result = is_valid_board(inp)
    assert expected == result, f'expected {expected} for {fn_name}({original}), got {result}'
    assert original == inp, f'{arg_name} was modified in {fn_name}, now contains {inp}'

    # Test single-element board
    inp = [['X']]
    expected = True
    original = copy.deepcopy(inp)

    result = is_valid_board(inp)
    assert expected == result, f'expected {expected} for {fn_name}({original}), got {result}'
    assert original == inp, f'{arg_name} was modified in {fn_name}, now contains {inp}'

    # Test only Os and spaces
    inp = [['O', 'O'],
           [' ', 'O']]
    expected = False
    original = copy.deepcopy(inp)

    result = is_valid_board(inp)
    assert expected == result, f'expected {expected} for {fn_name}({original}), got {result}'
    assert original == inp, f'{arg_name} was modified in {fn_name}, now contains {inp}'

    # Test more Os than Xs
    inp = [['O', 'X'],
           [' ', 'O']]
    expected = False
    original = copy.deepcopy(inp)

    result = is_valid_board(inp)
    assert expected == result, f'expected {expected} for {fn_name}({original}), got {result}'
    assert original == inp, f'{arg_name} was modified in {fn_name}, now contains {inp}'

    # Test 2 more Xs than Os
    inp = [['O', 'X'],
           ['X', 'X']]
    expected = False
    original = copy.deepcopy(inp)

    result = is_valid_board(inp)
    assert expected == result, f'expected {expected} for {fn_name}({original}), got {result}'
    assert original == inp, f'{arg_name} was modified in {fn_name}, now contains {inp}'

    print(f'tests for {fn_name} passed')


def test_is_row_win():
    """
    Test cases for is_row_win
    """
    fn_name = 'is_row_win'
    arg_name = 'board'

    # Test basic no-win
    inp1 = [['X', 'X', 'O'],
            [' ', ' ', 'X'],
            ['O', ' ', ' ']]
    inp2 = 'X'
    expected = False
    original = copy.deepcopy(inp1)

    result = is_row_win(inp1, inp2)
    assert expected == result, f'expected {expected} for {fn_name}({original}, {inp2}), got {result}'
    assert original == inp1, f'{arg_name} was modified in {fn_name}, now contains {inp1}'

    # Test single-element board
    inp1 = [['X']]
    inp2 = 'X'
    expected = True
    original = copy.deepcopy(inp1)

    result = is_row_win(inp1, inp2)
    assert expected == result, f'expected {expected} for {fn_name}({original}, {inp2}), got {result}'
    assert original == inp1, f'{arg_name} was modified in {fn_name}, now contains {inp1}'

    # Test basic win
    inp1 = [['O', 'O'],
            [' ', 'O']]
    inp2 = 'O'
    expected = True
    original = copy.deepcopy(inp1)

    result = is_row_win(inp1, inp2)
    assert expected == result, f'expected {expected} for {fn_name}({original}, {inp2}), got {result}'
    assert original == inp1, f'{arg_name} was modified in {fn_name}, now contains {inp1}'

    # Test loss with given player
    inp1 = [['O', 'O'],
            [' ', 'O']]
    inp2 = 'X'
    expected = False
    original = copy.deepcopy(inp1)

    result = is_row_win(inp1, inp2)
    assert expected == result, f'expected {expected} for {fn_name}({original}, {inp2}), got {result}'
    assert original == inp1, f'{arg_name} was modified in {fn_name}, now contains {inp1}'

    # Test win on non-first row
    inp1 = [['X', 'X', 'O'],
            ['X', 'X', 'X'],
            ['O', ' ', ' ']]
    inp2 = 'X'
    expected = True
    original = copy.deepcopy(inp1)

    result = is_row_win(inp1, inp2)
    assert expected == result, f'expected {expected} for {fn_name}({original}, {inp2}), got {result}'
    assert original == inp1, f'{arg_name} was modified in {fn_name}, now contains {inp1}'

    # Test win on column but not row
    inp1 = [['X', 'X', 'O'],
            ['O', 'X', 'O'],
            ['O', 'X', ' ']]
    inp2 = 'X'
    expected = False
    original = copy.deepcopy(inp1)

    result = is_row_win(inp1, inp2)
    assert expected == result, f'expected {expected} for {fn_name}({original}, {inp2}), got {result}'
    assert original == inp1, f'{arg_name} was modified in {fn_name}, now contains {inp1}'

    print(f'tests for {fn_name} passed')


def test_is_col_win():
    """
    Test cases for is_col_win
    """
    fn_name = 'is_col_win'
    arg_name = 'board'

    # Test basic no-win
    inp1 = [['X', 'X', 'O'],
            [' ', ' ', 'X'],
            ['O', ' ', ' ']]
    inp2 = 'X'
    expected = False
    original = copy.deepcopy(inp1)

    result = is_col_win(inp1, inp2)
    assert expected == result, f'expected {expected} for {fn_name}({original}, {inp2}), got {result}'
    assert original == inp1, f'{arg_name} was modified in {fn_name}, now contains {inp1}'

    # Test single-element board
    inp1 = [['X']]
    inp2 = 'X'
    expected = True
    original = copy.deepcopy(inp1)

    result = is_col_win(inp1, inp2)
    assert expected == result, f'expected {expected} for {fn_name}({original}, {inp2}), got {result}'
    assert original == inp1, f'{arg_name} was modified in {fn_name}, now contains {inp1}'

    # Test basic win
    inp1 = [['O', 'O'],
            [' ', 'O']]
    inp2 = 'O'
    expected = True
    original = copy.deepcopy(inp1)

    result = is_col_win(inp1, inp2)
    assert expected == result, f'expected {expected} for {fn_name}({original}, {inp2}), got {result}'
    assert original == inp1, f'{arg_name} was modified in {fn_name}, now contains {inp1}'

    # Test loss with given player
    inp1 = [['O', 'O'],
            [' ', 'O']]
    inp2 = 'X'
    expected = False
    original = copy.deepcopy(inp1)

    result = is_col_win(inp1, inp2)
    assert expected == result, f'expected {expected} for {fn_name}({original}, {inp2}), got {result}'
    assert original == inp1, f'{arg_name} was modified in {fn_name}, now contains {inp1}'

    # Test win on row but not column
    inp1 = [['X', 'X', 'O'],
            ['X', 'X', 'X'],
            ['O', ' ', ' ']]
    inp2 = 'X'
    expected = False
    original = copy.deepcopy(inp1)

    result = is_col_win(inp1, inp2)
    assert expected == result, f'expected {expected} for {fn_name}({original}, {inp2}), got {result}'
    assert original == inp1, f'{arg_name} was modified in {fn_name}, now contains {inp1}'

    # Test win on non-first column
    inp1 = [['X', 'X', 'O'],
            ['O', 'X', 'O'],
            ['O', 'X', ' ']]
    inp2 = 'X'
    expected = True
    original = copy.deepcopy(inp1)

    result = is_col_win(inp1, inp2)
    assert expected == result, f'expected {expected} for {fn_name}({original}, {inp2}), got {result}'
    assert original == inp1, f'{arg_name} was modified in {fn_name}, now contains {inp1}'

    print(f'tests for {fn_name} passed')


def test_is_diag_win():
    """
    Test cases for is_diag_win
    """
    fn_name = 'is_diag_win'
    arg_name = 'board'

    # Test basic no-win
    inp1 = [['X', 'X', 'O'],
            [' ', ' ', 'X'],
            ['O', ' ', ' ']]
    inp2 = 'X'
    expected = False
    original = copy.deepcopy(inp1)

    result = is_diag_win(inp1, inp2)
    assert expected == result, f'expected {expected} for {fn_name}({original}, {inp2}), got {result}'
    assert original == inp1, f'{arg_name} was modified in {fn_name}, now contains {inp1}'

    # Test single-element board
    inp1 = [['X']]
    inp2 = 'X'
    expected = True
    original = copy.deepcopy(inp1)

    result = is_diag_win(inp1, inp2)
    assert expected == result, f'expected {expected} for {fn_name}({original}, {inp2}), got {result}'
    assert original == inp1, f'{arg_name} was modified in {fn_name}, now contains {inp1}'

    # Test basic win
    inp1 = [['O', 'O'],
            [' ', 'O']]
    inp2 = 'O'
    expected = True
    original = copy.deepcopy(inp1)

    result = is_diag_win(inp1, inp2)
    assert expected == result, f'expected {expected} for {fn_name}({original}, {inp2}), got {result}'
    assert original == inp1, f'{arg_name} was modified in {fn_name}, now contains {inp1}'

    # Test loss with given player
    inp1 = [['O', 'O'],
            [' ', 'O']]
    inp2 = 'X'
    expected = False
    original = copy.deepcopy(inp1)

    result = is_diag_win(inp1, inp2)
    assert expected == result, f'expected {expected} for {fn_name}({original}, {inp2}), got {result}'
    assert original == inp1, f'{arg_name} was modified in {fn_name}, now contains {inp1}'

    # Test basic win on diagonal
    inp1 = [['X', 'X', 'O'],
            [' ', 'X', 'O'],
            ['O', ' ', 'X']]
    inp2 = 'X'
    expected = True
    original = copy.deepcopy(inp1)

    result = is_diag_win(inp1, inp2)
    assert expected == result, f'expected {expected} for {fn_name}({original}, {inp2}), got {result}'
    assert original == inp1, f'{arg_name} was modified in {fn_name}, now contains {inp1}'

    # Test win on row and column, but not diagonal
    inp1 = [['X', 'X', 'X'],
            ['O', 'O', 'X'],
            ['O', 'O', 'X']]
    inp2 = 'X'
    expected = False
    original = copy.deepcopy(inp1)

    result = is_diag_win(inp1, inp2)
    assert expected == result, f'expected {expected} for {fn_name}({original}, {inp2}), got {result}'
    assert original == inp1, f'{arg_name} was modified in {fn_name}, now contains {inp1}'

    # Test win on other diagonal
    inp1 = [['O', 'O', 'X'],
            [' ', 'X', 'O'],
            ['X', ' ', 'X']]
    inp2 = 'X'
    expected = True
    original = copy.deepcopy(inp1)

    result = is_diag_win(inp1, inp2)
    assert expected == result, f'expected {expected} for {fn_name}({original}, {inp2}), got {result}'
    assert original == inp1, f'{arg_name} was modified in {fn_name}, now contains {inp1}'

    print(f'tests for {fn_name} passed')


def test_winning_player():
    """
    Test cases for winning_player
    """
    fn_name = 'winning_player'
    arg_name = 'board'

    # Test basic no-win
    inp = [['X', 'X', 'O'],
           [' ', ' ', 'X'],
           ['O', ' ', ' ']]
    expected = ' '
    original = copy.deepcopy(inp)

    result = winning_player(inp)
    assert expected == result, f'expected {expected} for {fn_name}({original}), got {result}'
    assert original == inp, f'{arg_name} was modified in {fn_name}, now contains {inp}'

    # Test single-element board
    inp = [['X']]
    expected = 'X'
    original = copy.deepcopy(inp)

    result = winning_player(inp)
    assert expected == result, f'expected {expected} for {fn_name}({original}), got {result}'
    assert original == inp, f'{arg_name} was modified in {fn_name}, now contains {inp}'

    # Test basic win
    inp = [['X', 'X'],
           [' ', 'O']]
    expected = 'X'
    original = copy.deepcopy(inp)

    result = winning_player(inp)
    assert expected == result, f'expected {expected} for {fn_name}({original}), got {result}'
    assert original == inp, f'{arg_name} was modified in {fn_name}, now contains {inp}'

    # Test win on row
    inp = [['X', 'X', 'X'],
           [' ', 'O', 'O'],
           ['O', ' ', ' ']]
    expected = 'X'
    original = copy.deepcopy(inp)

    result = winning_player(inp)
    assert expected == result, f'expected {expected} for {fn_name}({original}), got {result}'
    assert original == inp, f'{arg_name} was modified in {fn_name}, now contains {inp}'

    # Test both players winning
    inp = [['O', 'O', 'O'],
           ['X', 'X', 'X'],
           [' ', ' ', ' ']]
    expected = 'X'
    original = copy.deepcopy(inp)

    result = winning_player(inp)
    assert expected == result, f'expected {expected} for {fn_name}({original}), got {result}'
    assert original == inp, f'{arg_name} was modified in {fn_name}, now contains {inp}'

    # Test column win
    inp = [['O', ' ', 'X'],
           ['O', 'X', 'O'],
           ['O', 'X', 'X']]
    expected = 'O'
    original = copy.deepcopy(inp)

    result = winning_player(inp)
    assert expected == result, f'expected {expected} for {fn_name}({original}), got {result}'
    assert original == inp, f'{arg_name} was modified in {fn_name}, now contains {inp}'

    # Test diagonal win
    inp = [['O', 'O', 'X'],
           [' ', 'X', 'O'],
           ['X', ' ', 'X']]
    expected = 'X'
    original = copy.deepcopy(inp)

    result = winning_player(inp)
    assert expected == result, f'expected {expected} for {fn_name}({original}), got {result}'
    assert original == inp, f'{arg_name} was modified in {fn_name}, now contains {inp}'

    # Test invalid board
    inp = [['X', 'X', 'X'],
           ['X', 'X', 'X'],
           ['X', 'X', 'X']]
    expected = ' '
    original = copy.deepcopy(inp)

    result = winning_player(inp)
    assert expected == result, f'expected {expected} for {fn_name}({original}), got {result}'
    assert original == inp, f'{arg_name} was modified in {fn_name}, now contains {inp}'

    print(f'tests for {fn_name} passed')


def test_all():
    # run all of our tests (one at a time)
    test_board_to_string()
    test_count_xs()
    test_count_os()
    test_is_valid_board()
    test_is_row_win()
    test_is_col_win()
    test_is_diag_win()
    test_winning_player()
    print('All tests passed!')


if __name__ == "__main__":
    test_all()
