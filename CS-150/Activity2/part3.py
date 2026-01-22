def count_lowercase(s):
    """Calculates the number of lowercase letters in a string

    Args:
        s (str): the string to search

    Returns:
        int: the number of lowercase letters
    """
    count = 0
    for letter in s:
        if letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
            count+=1
        """I know this seems inefficient, but i cant use isascii(), i cant use isalpha(), i cant hardcheck all numbers (because what if its an emoji), so to cut out the most possibilities at once I used the alphabet meathod :("""
    return count


def test_count_lowercase():
    assert 5 == count_lowercase("This meSSAGE CONTAINS 5 LOWERCASE LETTERS")
    assert 0 == count_lowercase("😎1CCII(99=0-0234""}{{|}})")
    assert 0 == count_lowercase("")
    pass


def are_all_evens(lst):
    """Returns whether all integers in a list are even

    Args:
        lst (list[int]): the list to search

    Returns:
        bool: True if all integers in the list are even and False otherwise
    """
    if lst == []:
        return False
    for num in lst:
        if num%2 != 0:
            return False
    return True


def test_are_all_evens():
    assert True == are_all_evens([2, 4, 6, 8, 88888888882])
    assert False == are_all_evens([2, 4, 6, 888888888881])
    assert True == are_all_evens([9999992, 1002, 202020202020])
    assert False == are_all_evens([0])
    assert False == are_all_evens([])
    pass


def is_perfect_square(x):
    """Returns whether x is a perfect square

    For example, 4 is a perfect square, and 5 is not

    Args:
        x (int): the number we check is a perfect square

    Returns:
        bool: True if x is a perfect square and False otherwise
    """
    guess = 1
    if x <= 0:
        return False

    while abs(x - pow(guess, 2)) > 0.00001:
        guess = (x/guess + guess)/2

    if pow(int(guess), 2) == x:
        return True
    return False
    """
    This is the neutonian method for finding square roots, 
    I used it to find the square root of x, then I squared the integer 
    (we know the guess is a slight over estimation, so i imposed it over an integer)
    version of that guess to see if it equaled x
    """

def test_is_perfect_square():
    assert True == is_perfect_square(4)
    assert False == is_perfect_square(5)
    assert True == is_perfect_square(1)
    assert True == is_perfect_square(25)
    assert False == is_perfect_square(999999)
    assert False == is_perfect_square(-4)
    assert True == is_perfect_square(2500)

    pass


def sum_negatives(lst):
    """Calculates the sum of all negative numbers in a list

    Positive numbers are ignored entirely in this calculation

    Args:
        lst (list[int]): the list to search

    Returns:
        int: the sum of all negative numbers in the list
    """
    return_sum = 0
    for num in lst:
        if num < 0:
            return_sum += num
    return return_sum


def test_sum_negatives():
    assert -15 == sum_negatives([5, -3, 2, -8, 0, 4, -4])
    assert 0 == sum_negatives([1, 2, 3, 4, 5])
    assert -1 == sum_negatives([-1, 0, 1])
    assert 0 == sum_negatives([])
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
    number = 1
    list_of_divisors = [1, 2]
    while num >= number:
        number +=2
        prime = True
        temp = None
        for temp in list_of_divisors[1:]:
            if number%temp == 0:
                prime = False
        if prime:
            list_of_divisors.append(number)
    
    return num in list_of_divisors


def test_is_prime():
    assert True == is_prime(1)
    assert True == is_prime(2)
    assert True == is_prime(13)
    assert False == is_prime(4)
    assert False == is_prime(0)
    assert False == is_prime(-7)
    assert True == is_prime(7919)
    assert True == is_prime(100003)
    assert False == is_prime(100002)  
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
    count = 0
    for string in lst:
        for itteration in range(len(string)):
            char = string[itteration]
            print(char)
            if char in ['a', 'e', 'i', 'o', 'u'] or (char == 'y' and itteration != 0):
                count += 1
            print(count)
            print(string.index(char))
    return count

def test_count_vowels():
    assert 7 == count_vowels(['hello', 'world', 'this', 'is', 'a', 'test'])
    assert 5 == count_vowels(['rhythm', 'my', 'by', 'you'])
    assert 5 == count_vowels(['a', 'e', 'i', 'o', 'u'])
    assert 25 == count_vowels(['yayayayay', 'eieioioio', 'ouououou'])
    assert 0 == count_vowels([])
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
