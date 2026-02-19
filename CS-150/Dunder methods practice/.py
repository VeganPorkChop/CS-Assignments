from sys import *
class Fraction:
    def __init__(self, n, d):
      if d == 0:
         print("Invalid Denominator!")
         exit()
      else:
         self.numerator = n
         self.denominator = d

    def __str__(self):
      return str(self.numerator) + "/" + str(self.denominator)

    def __add__(self, other):
        newDenominator = self.denominator*other.denominator
        newNumerator = self.numerator*other.denominator + self.denominator*other.numerator
        return Fraction(newNumerator, newDenominator)   
    def __eq__ (self, other):
        return self.numerator * other.denominator == self.denominator * other.numerator

def test_fraction():
    # Test initialization and string representation
    frac1 = Fraction(1, 2)
    frac2 = Fraction(3, 4)
    
    assert str(frac1) == "1/2", "Fraction string representation test failed for 1/2"
    assert str(frac2) == "3/4", "Fraction string representation test failed for 3/4"
    
    # Test addition of fractions
    frac3 = frac1 + frac2  # (1/2) + (3/4) should give (10/8)
    assert frac3.numerator == 10, "Addition numerator test failed"
    assert frac3.denominator == 8, "Addition denominator test failed"
    assert str(frac3) == "10/8", "Fraction string representation test failed for 10/8"
    
    assert Fraction(1, 2) == Fraction(2, 4), "Equality test failed for equal fractions"
    assert not (frac1 == frac2), "Equality test failed for different fractions"
    # Test invalid denominator case
    try:
        invalid_frac = Fraction(1, 0)
        assert False, "Creation of fraction with zero denominator did not raise an error"
    except SystemExit:
        assert True  # Expected behavior, should exit

# Run the tests
test_fraction()