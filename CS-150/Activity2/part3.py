def count_lowercase(s):
    """Calculates the number of lowercase letters in a string

    Args:
        s (str): the string to search

    Returns:
        int: the number of lowercase letters
    """
    # Implement me!
    return False


def test_count_lowercase():
    # Implement me!
    pass


def are_all_evens(lst):
    """Returns whether all integers in a list are even

    Args:
        lst (list[int]): the list to search

    Returns:
        bool: True if all integers in the list are even and False otherwise
    """
    # Implement me!
    return False


def test_are_all_evens():
    # Implement me!
    pass


def is_perfect_square(x):
    """Returns whether x is a perfect square

    For example, 4 is a perfect square, and 5 is not

    Args:
        x (int): the number we check is a perfect square

    Returns:
        bool: True if x is a perfect square and False otherwise
    """
    return False


def test_is_perfect_square():
    # implement me!
    pass


def sum_negatives(lst):
    """Calculates the sum of all negative numbers in a list

    Positive numbers are ignored entirely in this calculation

    Args:
        lst (list[int]): the list to search

    Returns:
        int: the sum of all negative numbers in the list
    """
    return 0


def test_sum_negatives():
    # implement me!
    pass


def is_prime(num):
    """Returns whether or not num is prime

    A prime number is any number that is only divided by 1 and itself

    For this function, negative numbers and 0 are not prime
    Additionally, 1 is considered a prime number

    Args:
        x (int): the number we check to be prime

    Returns:
        bool: True if x is a prime and False otherwise
    """
    return False


def test_is_prime():
    # implement me!
    pass


def count_vowels(lst):
    """Calculates the number of vowels in all strings in a list

    Assumes that all strings in lst must consist only of lowercase letters

    A vowel is any letter a, e, i, o, or u
    Additionally, y is considered a vowel so long as it's not the first letter of a string

    Args:
        lst (list[str]): the list to search

    Returns:
        int: the number of vowels in all strings of lst
    """
    return 0


def test_count_vowels():
    # implement me!
    pass


# we'll explain what this __name__ == "__main__" means in lecture
# the short of it is that it says to only run this code when we run this file directly
if __name__ == "__main__":
    # run all of our tests (one at a time)
    test_count_lowercase()
    test_are_all_evens()
    test_is_perfect_square()
    test_sum_negatives()
    test_is_prime()
    test_count_vowels()
    print('All tests passed!')
