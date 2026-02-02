"""
Author: Graham Gilbert-Schroeer
Reviewed by: Anastasia Kurdia
Last modified: 02/02/2026

Part 1 (List Comprehensions version)

A collection of functions to practice iteration and nested iteration using
list comprehensions where appropriate.

Note: Some in-place problems (like `negate`) are awkward to express cleanly
with list comprehensions, so regular loops are acceptable there.
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


def negate(lst):
    """Negates every number in lst (in-place)

    Args:
        lst (list[int]): the list to negate each number in

    Returns:
        None
    """
    return_list = []
    for pos in range(len(lst)):
        return_list.append(lst[pos]*-1)

    return return_list


def get_lowercase(lst):
    """Creates a single string of all the lowercase letters inside of lst

    lst is not modified

    Args:
        lst (list[str]): the list to search

    Returns:
        str: a string containing all lowercase letters in
             all strings of lst, in the order they appear
    """
    # Hint: as a reminder, islower() can check if a given letter is lowercase
    #   (or if a whole string consists of lowercase letters)
    # https://docs.python.org/3/library/stdtypes.html#str.islower
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
        list[str]: a new list with all uppercase letters converted to lowercase
    """
    # hint: consider using lower()
    # https://docs.python.org/3/library/stdtypes.html#str.lower
    return_list = []
    for char in lst:
        return_list.append(char.lower())
    return return_list

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


def test_all():
    # run all of our tests
    test_double_numbers()
    test_negate()
    test_get_lowercase()
    test_make_lower()
    print("All tests passed!")


if __name__ == "__main__":
    test_all()

