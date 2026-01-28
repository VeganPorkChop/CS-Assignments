"""
Author(s): Graham Gilbert-Schroeer
Creation Date: 1/26/26

Initial creation by Dietrich Geisler on 10/12/2025
Reviewed by Anastasia Kurdia on 1/22/2026

An implementation of the remove_punctuation function
"""

def remove_punctuation(s):
    """
    Returns the string s with punctuation removed
    Only the characters . , ? and ! are considered punctuation for this function
    """

    result = ''
    for char in s:
        # Check if our specific char is one of '.,?!'
        is_punctuation = char in '.,?!'
        if not is_punctuation:
            result = result + char
    return result


def test_remove_punctuation():
    # Test cases for remove_punctuation
    # These may be useful when debugging!

    expected = 'hey there'
    result = remove_punctuation('hey, there')
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = 'so great'
    result = remove_punctuation('so, great!')
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = 'cat'
    result = remove_punctuation('c.,?!a,?t')
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message


if __name__ == "__main__":
    test_remove_punctuation()
    print('All tests passed!')
