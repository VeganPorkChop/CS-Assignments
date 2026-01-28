"""
Author(s): Graham Gilbert-Schroeer
Creation Date: 1/26/26

Initial creation by Dietrich Geisler on 10/12/2025
Reviewed by Anastasia Kurdia on 1/22/2026

An implementation of the evaluate function
"""

def evaluate(s):
    """
    Returns the result of evaluating s as an arithmetic expression
    Order of operations is preserved, but no parentheses are allowed
    s can only consist of positive integers, +, and -
    """

    result = 0
    operation = '+'      # keep track of which operation is next to apply
    next_number = ''    # keep track of the next number to work with

    for char in s:
        # when we see another operation, apply what we currently have
        if char == '+' or char == '-':
            result = apply_operation(result, operation, next_number)
            # Set the next operation and reset the next number
            operation = char
            next_number = ''
        else:
            next_number = next_number + char
            
    result = apply_operation(result, operation, next_number)

    return result


def apply_operation(result, operation, next_number):
    """
    A helper function for "evaluate" to apply the current evaluation
    """
    # Turn our next number string into an integer
    number = int(next_number)
    # Check which operation to apply
    if operation == '+':
        return result + number
    elif operation == '-':
        return result - number
    else:  # there's no operation to apply, just return result
        return number


def test_evaluate():
    # Test cases for evaluate
    # These may be useful when debugging!

    expected = 5
    result = evaluate('4+3-2')
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = 42
    result = evaluate('42')
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = 12
    result = evaluate('8+3+1')
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message

    expected = 96
    result = evaluate('100-4')
    error_message = f'expected {expected}, got {result}'
    assert expected == result, error_message


if __name__ == "__main__":
    test_evaluate()
    print('All tests passed!')
