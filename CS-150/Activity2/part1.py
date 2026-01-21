import math  # we'll talk about this in lecture soon


def is_palindrome(s):
    """Returns whether a string is a palindrome

    A palindrome is any string that is identical when read forwards or backwards

    Args:
        s (str): the string to check

    Returns:
        bool: True if s is a palindrome and False otherwise
    """

    # Implement me!
    return False


def test_is_palindrome():
    assert is_palindrome('racecar')
    assert is_palindrome('abc  cba')
    assert not is_palindrome('hello')
    assert not is_palindrome('Racecar')
    assert is_palindrome('')


def adjacent_duplicate(lst):
    """Calculates the number of adjacent_duplicates in a list of numbers

    An adjacent duplicate is a number with the same number next to it in the list
    Note that each number with an adjacent duplicate is counted separately

    Args:
        lst (list[int]): the list to search

    Returns:
        int: the number of duplicates
    """

    # Implement me!
    return 0


def test_adjacent_duplicate():
    assert 2 == adjacent_duplicate([4, 4])
    assert 2 == adjacent_duplicate([3, 6, 6, 3, 4, 3])
    assert 5 == adjacent_duplicate([-1, -1, -1, -1, -1])
    assert 0 == adjacent_duplicate([])


def average(lst):
    """Calculates the average of a list of numbers

    If the list is empty, returns 0

    Args:
        lst (list[int]): the list of numbers

    Returns:
        float: the average of these numbers
    """

    # Implement me!
    return 0


def assertNearlyEqual(expected, actual):
    """
    Validates if expected and actual are "nearly equal"
    Necessary for tests involving floats
    """
    # Note this f-string (mentioned in the strings lecture slides)
    # This string requires that we put an "f" in front
    message = f'Expected ~{expected}, got {actual}'
    assert math.isclose(expected, actual), message


def test_average():
    assertNearlyEqual(3.0, average([2, 3, 4]))
    assertNearlyEqual(1.2, average([1, 1, 1, 1, 2]))
    assertNearlyEqual(-2.5, average([-5, 0]))
    assertNearlyEqual(0, average([]))


# we'll explain what this __name__ == "__main__" means in lecture
# the short of it is that it says to only run this code when we run this file directly
if __name__ == "__main__":
    # run all of our tests (one at a time)
    test_is_palindrome()
    test_adjacent_duplicate()
    test_average()
    print('All tests passed!')
