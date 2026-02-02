"""
(You don't need to replace the header on this file)
Original author: Dietrich Geisler
Reviewed by: Anastasia Kurdia
Last modified: 02/01/2026

A collection of small functions to give more practice with loops/nested lists
"""

import copy  # used for testing

def adjacent_sum(lst):
    """Creates new list where each element is the sum of adjacent elements in lst

    lst is not modified

    Elements on either end of the result will only be the sum of two numbers
      or one number in the case of an input with a single number

    For example, adjacent_sum([1, 2, 3]) would produce:
        [1 + 2, 1 + 2 + 3, 2 + 3] == [3, 6, 5]

    Args:
        lst (list[int]): the list to sum over

    Returns:
        list[int]: a new list of the sums of adjacent elements
    """
    # note: this question is very tricky with list comprehensions,
    #   and demonstrates a case where they are explicitly not recommended
    # if you want to try, consider using a comprehension over range instead

    # Implement me!
    return []


# ---------------------------------------------------------------
# "Hard" functions start here
# ---------------------------------------------------------------

def adjacent_sum_table(table):
    """Creates a copy of table where each element sums adjacent (orthogonal) elements

    table is not modified by this function

    orthogonal refers to elements immediately above, below, left, and right a
      given element of the table, but does not include diagonally adjacent

    elements on the edges of the table only sum elements next to them
      they don't "loop around" the table

    Args:
        table (list[list[int]]): the table to sum over

    Returns:
        list[list[int]]: a new table representing the sum of adjacent elements
    """
    
    # Implement me!
    return []


def matrix_multiply(matrix1, matrix2):
    """Multiplies matrix1 by matrix2

    Uses the usual definition of matrix multiply: https://en.wikipedia.org/wiki/Matrix_multiplication

    Each matrix must be a rectangular table
    And we assume that the number of columns of matrix1 matches the number of rows of matrix2

    matrix1 and matrix2 are not modified by this function

    We use integers for this function for simplicity when testing

    Hint: you probably want three nested for loops

    Args:
        matrix1 (list[list[int]]): the first mxn matrix
        matrix2 (list[list[int]]): the second nxp matrix

    Returns:
        list[list[int]]: a new matrix containing the result of matrix1 * matrix2
    """
    
    # Implement me!
    return []

# ---------------------------------------------------------------
# Test cases for all functions in part2_subadjacent.py
# These are implemented for you
# ---------------------------------------------------------------


def test_adjacent_sum():
    """
    Test cases for adjacent_sum
    """
    fn_name = 'adjacent_sum'
    arg_name = 'lst'

    # Basic case
    inp = [1, 2, 3]
    expected = [3, 6, 5]
    original = copy.deepcopy(inp)

    result = adjacent_sum(inp)
    assert expected == result, f'expected {expected} for {fn_name}({original}), got {result}'
    assert original == inp, f'{arg_name} was modified in {fn_name}, now contains {inp}'

    # single-element list
    inp = [1]
    expected = [1]
    original = copy.deepcopy(inp)

    result = adjacent_sum(inp)
    assert expected == result, f'expected {expected} for {fn_name}({original}), got {result}'
    assert original == inp, f'{arg_name} was modified in {fn_name}, now contains {inp}'

    # duplicate numbers, zero
    inp = [2, 2, 4, 0, -1]
    expected = [4, 8, 6, 3, -1]
    original = copy.deepcopy(inp)

    result = adjacent_sum(inp)
    assert expected == result, f'expected {expected} for {fn_name}({original}), got {result}'
    assert original == inp, f'{arg_name} was modified in {fn_name}, now contains {inp}'

    print(f'tests for {fn_name} passed')


def test_adjacent_sum_table():
    """
    Test cases for adjacent_sum_table
    """
    fn_name = 'adjacent_sum_table'
    arg_name = 'table'

    # 1x1 case
    inp = [[1]]
    expected = [[1]]
    original = copy.deepcopy(inp)

    result = adjacent_sum_table(inp)
    assert expected == result, f'expected {expected} for {fn_name}({original}), got {result}'
    assert original == inp, f'{arg_name} was modified in {fn_name}, now contains {inp}'

    # 2x2 case
    inp = [[1, 2],
           [3, 4]]
    expected = [[6, 7],
                [8, 9]]
    original = copy.deepcopy(inp)

    result = adjacent_sum_table(inp)
    assert expected == result, f'expected {expected} for {fn_name}({original}), got {result}'
    assert original == inp, f'{arg_name} was modified in {fn_name}, now contains {inp}'

    # empty table
    inp = []
    expected = []
    original = copy.deepcopy(inp)

    result = adjacent_sum_table(inp)
    assert expected == result, f'expected {expected} for {fn_name}({original}), got {result}'
    assert original == inp, f'{arg_name} was modified in {fn_name}, now contains {inp}'

    # empty inner lists
    inp = [[], []]
    expected = [[], []]
    original = copy.deepcopy(inp)

    result = adjacent_sum_table(inp)
    assert expected == result, f'expected {expected} for {fn_name}({original}), got {result}'
    assert original == inp, f'{arg_name} was modified in {fn_name}, now contains {inp}'

    # 3x2 case
    inp = [[-1, 2],
           [-4, -5],
           [2, 1]]
    expected = [[-3, -4],
                [-8, -6],
                [-1, -2]]
    original = copy.deepcopy(inp)

    result = adjacent_sum_table(inp)
    assert expected == result, f'expected {expected} for {fn_name}({original}), got {result}'
    assert original == inp, f'{arg_name} was modified in {fn_name}, now contains {inp}'

    print(f'tests for {fn_name} passed')


def test_matrix_multiply():
    """
    Test cases for matrix_multiply
    """
    fn_name = 'matrix_multiply'
    arg_name1 = 'matrix1'
    arg_name2 = 'matrix2'

    # 1x1 test
    inp1 = [[-1]]
    inp2 = [[2]]
    expected = [[-2]]
    original1 = copy.deepcopy(inp1)
    original2 = copy.deepcopy(inp2)

    result = matrix_multiply(inp1, inp2)
    assert expected == result, f'expected {expected} for {fn_name}({original1}, {original2}), got {result}'
    assert original1 == inp1, f'{arg_name1} was modified in {fn_name}, now contains {inp1}'
    assert original2 == inp2, f'{arg_name2} was modified in {fn_name}, now contains {inp1}'

    # 2x2 test
    inp1 = [[1, 2], [3, 4]]
    inp2 = [[-2, -3], [0, 4]]
    expected = [[-2, 5], [-6, 7]]
    original1 = copy.deepcopy(inp1)
    original2 = copy.deepcopy(inp2)

    result = matrix_multiply(inp1, inp2)
    assert expected == result, f'expected {expected} for {fn_name}({original1}, {original2}), got {result}'
    assert original1 == inp1, f'{arg_name1} was modified in {fn_name}, now contains {inp1}'
    assert original2 == inp2, f'{arg_name2} was modified in {fn_name}, now contains {inp1}'

    # rectangle test
    inp1 = [[1, 2], [3, 4], [5, 6]]
    inp2 = [[-2, -3, -4], [0, 4, -1]]
    expected = [[-2, 5, -6], [-6, 7, -16], [-10, 9, -26]]
    original1 = copy.deepcopy(inp1)
    original2 = copy.deepcopy(inp2)

    result = matrix_multiply(inp1, inp2)
    assert expected == result, f'expected {expected} for {fn_name}({original1}, {original2}), got {result}'
    assert original1 == inp1, f'{arg_name1} was modified in {fn_name}, now contains {inp1}'
    assert original2 == inp2, f'{arg_name2} was modified in {fn_name}, now contains {inp1}'

    # This likely needs more tests (are you convinced?)

    print(f'tests for {fn_name} passed')


def test_all():
    test_adjacent_sum()
    test_adjacent_sum_table()
    test_matrix_multiply()
    print('All tests passed!')


if __name__ == "__main__":
    test_all()
