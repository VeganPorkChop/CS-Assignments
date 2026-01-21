def half_roundup(x):
    """Calculates x divided by 2 and rounded up

    For example, half_roundup(5) should produce 3
    Note that negative numbers should be rounded to the next largest integer

    Args:
        x (int): the number to divide

    Returns:
        int
    """
    if x % 2 == 0:
        return x // 2
    return (x + 1) // 2


def test_half_roundup():
    # Implement me!
    pass


def ascending(s):
    """Returns whether the letters of s are in ascending order

    A string is in ascending order if each letter is the same or 
      comes after the previous letter alphabetically
    For example, 'abccd' is ascending, while 'ba' is not

    Args:
        s (str): the string to check

    Returns:
        bool: True if the letters of s are in ascending order, and False otherwise
    """
    for index in range(len(s)-1):
        if s[index] > s[index + 1]:
            return False
    return True


def test_ascending():
    # Implement me!
    pass


def largest_digit(lst):
    """Finds the string with the largest digit in the list of strings lst

    If there are no strings with digits in lst, returns the empty string ''
    All strings in lst must consist only of digits (0-9)

    For example, running largest_digit on ['11', '02'] should return '02'

    If there are multiple strings with the highest digit in lst
      largest_digit will return the first (left-most) of these strings

    Args:
        lst (list[str]): the list of strings to search

    Returns:
        str: the string with the highest digit among all strings in lst
    """
    largest = -1
    result = ''
    for s in lst:
        for letter in s:
            if int(letter) > largest:
                result = s
                largest = int(letter)
    return result


def test_largest_digit():
    # Implement me!
    pass


# we'll explain what this __name__ == "__main__" means in lecture
# the short of it is that it says to only run this code when we run this file directly
if __name__ == "__main__":
    # run all of our tests (one at a time)
    test_half_roundup()
    test_ascending()
    test_largest_digit()
    print('All tests passed!')
