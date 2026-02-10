"""
Original author: Graham Gilbert-Schroeer
Reviewed by: Anastasia Kurdia
Last modified: 02/02/2026

Part 1 (Loops version)

A collection of functions to practice iteration and nested iteration using
standard for-loops (no list comprehensions required).
"""

import copy  # used for testing


def double_numbers(lst):
    """Creates a copy of lst with each number doubled

    lst is not modified

    Args:
        lst (list[int]): the list to work over

    Returns:
        list[int]: a new list with each element of lst doubled
    """
    return_list = []
    for num in lst:
        return_list.append(2*num)
    return return_list


def double_numbers_table(table):
    """Creates a copy of table with each number doubled

    table is not modified
    Every row in table must be the same length

    Args:
        table (list[list[int]]): the table to work over

    Returns:
        list[list[int]]: a new list with each element of table doubled
    """
    if len(table) is 0:
        return []
    return_table = [[],[]]
    for row in range(len(table)):
        for num in range(len(table[row])):
            return_table[row].append(2*table[row][num])
    return return_table


def negate(lst):
    """
    Negates every number in lst (in-place)

    Args:
        lst (list[int]): the list to negate each number in

    Returns:
        None
    """
    for pos in range(len(lst)):
        lst[pos] = (lst[pos]*-1)
    


def negate_table(table):
    """
    Negates every number in table (in-place)

    Every row in table must be the same length

    Args:
        table (list[list[int]]): the table to negate each number in

    Returns:
        None
    """
    for row in range(len(table)):
        for col in range(len(table[row])):
            table[row][col] = (-1*table[row][col])
    


def get_lowercase(lst):
    """
    Creates a single string of all the lowercase letters inside of lst

    lst is not modified
    
    Args:
        lst (list[str]): the list to search

    Returns:
        str: a string containing all lowercase letters in
             all strings of lst, in the order they appear
    """
    return_str = ""
    for word in lst:
        for char in word:
            if char.islower():
                return_str += char
    return return_str


def make_lower(lst):
    """Creates a new list where each string is converted to lowercase

    lst is not modified.

    Args:
        lst (list[str]): the list of strings to convert

    Returns:
        list[str]: a new list with all strings converted to lowercase
    """
    return_list = []
    for char in lst:
        return_list.append(char.lower())
    return return_list


def sum_rows(table):
    """Creates a new list of the sums of each row of the given table

    Table must be a list of lists of integers.

    Args:
        table (list[list[int]]): the table to sum over

    Returns:
        list[int]: a new list where each element is the sum of a row in table
    """
    # Note: you can use the builtin "sum" operation for this function
    # https://docs.python.org/3.11/library/functions.html#sum
    # I would encourage you to try without that operation for more practice

    # Implement me!
    x = len(table)
    return_list = [[0] for row in range(x)]
    for i in range(len(table)):
        temp_total = 0
        for num in table[i]:
            temp_total+=num
        return_list[i] = temp_total
    return return_list


def add_row_sum(table):
    """Adds the sum of each row to each element of that row in the given table (in-place)

    Args:
        table (list[list[int]]): the table to update

    Returns:
        None
    """
    lst = sum_rows(table)
    for i in range(len(table)):
        for j in range(len(table[0])):
            table[i][j] += lst[i]


# ---------------------------------------------------------------
# Test cases
# These are implemented for you
# ---------------------------------------------------------------


def test_double_numbers():
    """
    Test cases for double numbers
    """
    fn_name = "double_numbers"
    arg_name = "lst"

    # basic case
    inp = [1, 2, 3]
    expected = [2, 4, 6]
    original = copy.deepcopy(inp)

    result = double_numbers(inp)
    assert expected == result, f"expected {expected} for {fn_name}({original}), got {result}"
    assert original == inp, f"{arg_name} was modified in {fn_name}, now contains {inp}"

    # empty list
    inp = []
    expected = []
    original = copy.deepcopy(inp)

    result = double_numbers(inp)
    assert expected == result, f"expected {expected} for {fn_name}({original}), got {result}"
    assert original == inp, f"{arg_name} was modified in {fn_name}, now contains {inp}"

    # negative numbers, zero
    inp = [-20, -30, 0, 10]
    expected = [-40, -60, 0, 20]
    original = copy.deepcopy(inp)

    result = double_numbers(inp)
    assert expected == result, f"expected {expected} for {fn_name}({original}), got {result}"
    assert original == inp, f"{arg_name} was modified in {fn_name}, now contains {inp}"

    print(f"tests for {fn_name} passed")


def test_double_numbers_table():
    """
    Test cases for double numbers table
    """
    fn_name = "double_numbers_table"
    arg_name = "table"

    # square table
    inp = [[1, 2], [3, 4]]
    expected = [[2, 4], [6, 8]]
    original = copy.deepcopy(inp)

    result = double_numbers_table(inp)
    assert expected == result, f"expected {expected} for {fn_name}({original}), got {result}"
    assert original == inp, f"{arg_name} was modified in {fn_name}, now contains {inp}"

    # empty table
    inp = []
    expected = []
    original = copy.deepcopy(inp)

    result = double_numbers_table(inp)
    assert expected == result, f"expected {expected} for {fn_name}({original}), got {result}"
    assert original == inp, f"{arg_name} was modified in {fn_name}, now contains {inp}"

    # negative numbers, rectangular table
    inp = [[-20, -30, 0], [-21, 1, 2]]
    expected = [[-40, -60, 0], [-42, 2, 4]]
    original = copy.deepcopy(inp)

    result = double_numbers_table(inp)
    assert expected == result, f"expected {expected} for {fn_name}({original}), got {result}"
    assert original == inp, f"{arg_name} was modified in {fn_name}, now contains {inp}"

    print(f"tests for {fn_name} passed")


def test_negate():
    """
    Test cases for negate
    """
    fn_name = "negate"
    arg_name = "lst"

    # basic case
    result = [1, 2, 3, 4, 5]
    expected = [-1, -2, -3, -4, -5]
    original = copy.deepcopy(result)

    out = negate(result)
    assert (
        expected == result
    ), f"expected {expected} to be stored in {arg_name} after calling {fn_name}({original}), got {result}"
    assert out is None, f"expected {fn_name} to return None, got {out}"

    # empty list
    result = []
    expected = []
    original = copy.deepcopy(result)

    out = negate(result)
    assert (
        expected == result
    ), f"expected {expected} to be stored in {arg_name} after calling {fn_name}({original}), got {result}"
    assert out is None, f"expected {fn_name} to return None, got {out}"

    # negative numbers, zero
    result = [-10, 20, 0]
    expected = [10, -20, 0]
    original = copy.deepcopy(result)

    out = negate(result)
    assert (
        expected == result
    ), f"expected {expected} to be stored in {arg_name} after calling {fn_name}({original}), got {result}"
    assert out is None, f"expected {fn_name} to return None, got {out}"

    print(f"tests for {fn_name} passed")


def test_negate_table():
    """
    Test cases for negate table
    """
    fn_name = "negate_table"
    arg_name = "table"

    # square table
    result = [[1, 2], [3, 4]]
    expected = [[-1, -2], [-3, -4]]
    original = copy.deepcopy(result)

    out = negate_table(result)
    assert (
        expected == result
    ), f"expected {expected} to be stored in {arg_name} after calling {fn_name}({original}), got {result}"
    assert out is None, f"expected {fn_name} to return None, got {out}"

    # empty table
    result = []
    expected = []
    original = copy.deepcopy(result)

    out = negate_table(result)
    assert (
        expected == result
    ), f"expected {expected} to be stored in {arg_name} after calling {fn_name}({original}), got {result}"
    assert out is None, f"expected {fn_name} to return None, got {out}"

    # negative numbers, rectangular table
    result = [[5, -5], [-4, 4], [-1, 0]]
    expected = [[-5, 5], [4, -4], [1, 0]]
    original = copy.deepcopy(result)

    out = negate_table(result)
    assert (
        expected == result
    ), f"expected {expected} to be stored in {arg_name} after calling {fn_name}({original}), got {result}"
    assert out is None, f"expected {fn_name} to return None, got {out}"

    print(f"tests for {fn_name} passed")

def test_get_lowercase():
    """
    Test cases for get_lowercase
    """
    fn_name = "get_lowercase"
    arg_name = "lst"

    # all lowercase and all uppercase
    inp = ["abcd", "ABCD"]
    expected = "abcd"
    original = copy.deepcopy(inp)

    result = get_lowercase(inp)
    assert expected == result, f"expected {expected} for {fn_name}({original}), got {result}"
    assert original == inp, f"{arg_name} was modified in {fn_name}, now contains {inp}"

    # only lowercase across mutiple strings, empty string
    inp = ["hello", "world", "", "test"]
    expected = "helloworldtest"
    original = copy.deepcopy(inp)

    result = get_lowercase(inp)
    assert expected == result, f"expected {expected} for {fn_name}({original}), got {result}"
    assert original == inp, f"{arg_name} was modified in {fn_name}, now contains {inp}"

    # mix of uppercase and lowercase
    inp = ["tEsTing", "ANOther"]
    expected = "tsingther"
    original = copy.deepcopy(inp)

    result = get_lowercase(inp)
    assert expected == result, f"expected {expected} for {fn_name}({original}), got {result}"
    assert original == inp, f"{arg_name} was modified in {fn_name}, now contains {inp}"

    # numbers and whitespace
    inp = ["th\tis is", "123a tePst"]
    expected = "thisisatest"
    original = copy.deepcopy(inp)

    result = get_lowercase(inp)
    assert expected == result, f"expected {expected} for {fn_name}({original}), got {result}"
    assert original == inp, f"{arg_name} was modified in {fn_name}, now contains {inp}"

    print(f"tests for {fn_name} passed")
    
def test_make_lower():
    """
    Test cases for make_lower
    """
    fn_name = "make_lower"
    arg_name = "lst"

    # both upper and lower case
    inp = ["abcd", "DEFG"]
    expected = ["abcd", "defg"]
    original = copy.deepcopy(inp)

    out = make_lower(inp)
    assert expected == out, f"expected {expected} for {fn_name}({original}), got {out}"
    assert original == inp, f"{arg_name} was modified in {fn_name}, now contains {inp}"

    # mix of upper and lower in one string
    inp = ["tEsTing"]
    expected = ["testing"]
    original = copy.deepcopy(inp)

    out = make_lower(inp)
    assert expected == out, f"expected {expected} for {fn_name}({original}), got {out}"
    assert original == inp, f"{arg_name} was modified in {fn_name}, now contains {inp}"

    # empty string, non-letters
    inp = ["", "123ABC", "!@#"]
    expected = ["", "123abc", "!@#"]
    original = copy.deepcopy(inp)

    out = make_lower(inp)
    assert expected == out, f"expected {expected} for {fn_name}({original}), got {out}"
    assert original == inp, f"{arg_name} was modified in {fn_name}, now contains {inp}"

    print(f"tests for {fn_name} passed")


def test_sum_rows():
    """
    Test cases for sum_rows
    """
    fn_name = "sum_rows"
    arg_name = "table"

    # basic case
    inp = [[1, 2, 3], [4, 5, 6]]
    expected = [6, 15]
    original = copy.deepcopy(inp)

    result = sum_rows(inp)
    assert expected == result, f"expected {expected} for {fn_name}({original}), got {result}"
    assert original == inp, f"{arg_name} was modified in {fn_name}, now contains {inp}"

    # empty list
    inp = []
    expected = []
    original = copy.deepcopy(inp)

    result = sum_rows(inp)
    assert expected == result, f"expected {expected} for {fn_name}({original}), got {result}"
    assert original == inp, f"{arg_name} was modified in {fn_name}, now contains {inp}"

    # empty inner lists
    inp = [[], []]
    expected = [0, 0]
    original = copy.deepcopy(inp)

    result = sum_rows(inp)
    assert expected == result, f"expected {expected} for {fn_name}({original}), got {result}"
    assert original == inp, f"{arg_name} was modified in {fn_name}, now contains {inp}"

    # negatives
    inp = [[-1, 2], [-4, -5]]
    expected = [1, -9]
    original = copy.deepcopy(inp)

    result = sum_rows(inp)
    assert expected == result, f"expected {expected} for {fn_name}({original}), got {result}"
    assert original == inp, f"{arg_name} was modified in {fn_name}, now contains {inp}"

    print(f"tests for {fn_name} passed")


def test_add_row_sum():
    """
    Test cases for add_row_sum
    """
    fn_name = "add_row_sum"
    arg_name = "table"

    # basic case
    result = [[1, 2, 3], [4, 5, 6]]
    expected = [[7, 8, 9], [19, 20, 21]]
    original = copy.deepcopy(result)

    out = add_row_sum(result)
    assert (
        expected == result
    ), f"expected {expected} to be stored in {arg_name} after calling {fn_name}({original}), got {result}"
    assert out is None, f"expected {fn_name} to return None, got {out}"

    # empty table
    result = []
    expected = []
    original = copy.deepcopy(result)

    out = add_row_sum(result)
    assert (
        expected == result
    ), f"expected {expected} to be stored in {arg_name} after calling {fn_name}({original}), got {result}"
    assert out is None, f"expected {fn_name} to return None, got {out}"

    # empty inner lists
    result = [[], []]
    expected = [[], []]
    original = copy.deepcopy(result)

    out = add_row_sum(result)
    assert (
        expected == result
    ), f"expected {expected} to be stored in {arg_name} after calling {fn_name}({original}), got {result}"
    assert out is None, f"expected {fn_name} to return None, got {out}"

    # negatives
    result = [[-1, 2], [-4, -5]]
    expected = [[0, 3], [-13, -14]]
    original = copy.deepcopy(result)

    out = add_row_sum(result)
    assert (
        expected == result
    ), f"expected {expected} to be stored in {arg_name} after calling {fn_name}({original}), got {result}"
    assert out is None, f"expected {fn_name} to return None, got {out}"

    print(f"tests for {fn_name} passed")


def test_all():
    # run all of our tests
    test_double_numbers()
    test_double_numbers_table()
    test_negate()
    test_negate_table()
    test_get_lowercase()
    test_make_lower()
    test_sum_rows()
    test_add_row_sum()
    print("All tests passed!")


if __name__ == "__main__":
    test_all()

