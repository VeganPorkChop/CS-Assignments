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
    assert -1 == half_roundup(-3)
    assert 0 == half_roundup(0)
    assert 5 == half_roundup(10)
    assert 101 == half_roundup(201)
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
    assert True == ascending("abcdefghijklmnopqrstuvwxyz")
    assert False == ascending("babcdefghijklmnopqurstuvwxyz")
    assert True == ascending("acegikmoqstvxz")
    assert False == ascending("Graham Gilbert Schroeer is the best at coding in Python")

    """
    assert False == ascending("aaaaaaa")

    This is perhaps an example of the program not working perfectly?
    To fix this, add this if right before the return True

    if s[0] == s[len(s) - 1]:
        print("This string doesnt move at all!! Therefore, it cant be increasing!")
        return False
    """
    
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
    assert '789' == largest_digit(['123', '456', '789'])
    assert '' == largest_digit([''])
    assert '0123456789' == largest_digit(['0123456789', '999', '999', '999', '999999999999999'])
    assert '34567' == largest_digit(['12345', '23456', '34567', '45555', '55555', '123450'])
    pass


# we'll explain what this __name__ == "__main__" means in lecture
# the short of it is that it says to only run this code when we run this file directly
if __name__ == "__main__":
    # run all of our tests (one at a time)
    test_half_roundup()
    test_ascending()
    test_largest_digit()
    print('All tests passed!')
