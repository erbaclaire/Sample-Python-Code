'''
Homework 5 - Problem 2:
Write a class named Fraction that represents a rational number (a number that can
be expressed as the quotient of two integers). 

See HW5 PDF for specifics
'''

# Checked homework with Matt Pozsgai
# I allow my operators to account for floats, as well - with integers, the operator magic methods assume the denominator is 1 so we never need to qualify that.

from math import gcd

class Fraction:

    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ZeroDivisionError("Denominator is 0 - Cannot Compute Fraction")
        else:
            d =  gcd(numerator,denominator)
            self.denominator = int(abs(denominator/d)) # always makes denominator positive and numerator negative if need be (i.e. will not have 5/-3) and have two negatives make a positive
            if (numerator>0 and denominator>0) or (numerator<0 and denominator<0):
                self.numerator = int(abs(numerator/d))
            else:
                self.numerator = -int(abs(numerator/d))
            
    def __add__(self, other):
        try:
            return Fraction(((self.numerator * other.denominator) + (other.numerator * self.denominator)),(self.denominator * other.denominator))
        except TypeError:
            return NotImplemented
        
    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        try:
            return Fraction(((self.numerator * other.denominator) - (other.numerator * self.denominator)),(self.denominator * other.denominator))
        except TypeError:
            return NotImplemented
        
    def __rsub__(self, other):
        return Fraction(other, 1) - self # for subtraction fraction-int is not the same as int-fraction -- cannot simply reverse.

    def __mul__(self, other):
        try:
            return Fraction((self.numerator * other.numerator), (self.denominator * other.denominator))
        except TypeError:
            return NotImplemented
        
    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        try:
            return Fraction((self.numerator * other.denominator), (self.denominator * other.numerator))
        except TypeError:
            return NotImplemented
        
    def __rtruediv__(self, other):
        return Fraction(other, 1) / self # for division fraction/int is not the same as int/fraction -- cannot simply reverse.
    
    def __repr__(self):
        return "Fraction({}, {})".format(self.numerator, self.denominator)

'''    
if __name__ == '__main__':

    frac1 = Fraction(28, 20)
    frac2 = Fraction(-28, -20)
    frac3 = Fraction(28, -20)
    frac4 = Fraction(-28, 20)
    frac5 = Fraction(0, -19)
    frac6 = Fraction(-3, 6)

    print("fraction 1 tests")
    print("{}: Expect Fraction(7, 5)".format(frac1))
    print("{}: Expect Fraction(42, 5)".format(frac1 + 7))
    print("{}: Expect Fraction(42, 5)".format(7 + frac1))
    print("{}: Expect Fraction(9, 10)".format(frac1 + frac6))
    print("{}: Expect Fraction(9, 10)".format(frac6 + frac1))

    print("{}: Expect Fraction(-28, 5)".format(frac1 - 7))
    print("{}: Expect Fraction(28, 5)".format(7 - frac1))
    print("{}: Expect Fraction(19, 10)".format(frac1 - frac6))
    print("{}: Expect Fraction(-19, 10)".format(frac6 - frac1))
    
    print("{}: Expect Fraction(49, 5)".format(frac1 * 7))
    print("{}: Expect Fraction(49, 5)".format(7 * frac1))
    print("{}: Expect Fraction(-7, 10)".format(frac1 * frac6))
    print("{}: Expect Fraction(-7, 10)".format(frac6 * frac1))
    
    print("{}: Expect Fraction(1, 5)".format(frac1 / 7))
    print("{}: Expect Fraction(5, 1)".format(7 / frac1))
    print("{}: Expect Fraction(-14, 5)".format(frac1 / frac6))
    print("{}: Expect Fraction(-5, 14)".format(frac6 / frac1))

    print("more initialization tests")
    print("{}: Expect Fraction(7, 5)".format(frac2))
    print("{}: Expect Fraction(-7, 5)".format(frac3))
    print("{}: Expect Fraction(-7, 5)".format(frac4))
    print("{}: Expect Fraction(0, 1)".format(frac5))
    print("{}: Expect Fraction(-1, 2)".format(frac6))

    print("more tests")
    print("{}: Expect Fraction(42, 5)".format(frac2 + 7))
    print("{}: Expect Fraction(28, 5)".format(7 - frac2))
    print("{}: Expect Fraction(-7, 10)".format(frac2 * frac6))
    print("{}: Expect Fraction(5, 1)".format(7 / frac2))

    print("{}: Expect Fraction(28, 5)".format(frac3 + 7))
    print("{}: Expect Fraction(42, 5)".format(7 - frac3))
    print("{}: Expect Fraction(7, 10)".format(frac3 * frac6))
    print("{}: Expect Fraction(-5, 1)".format(7 / frac3))

    print("{}: Expect Fraction(28, 5)".format(frac4 + 7))
    print("{}: Expect Fraction(42, 5)".format(7 - frac4))
    print("{}: Expect Fraction(7, 10)".format(frac4 * frac6))
    print("{}: Expect Fraction(-5, 1)".format(7 / frac4))

    print("{}: Expect Fraction(7, 1)".format(frac5 + 7))
    print("{}: Expect Fraction(7, 1)".format(7 - frac5))
    print("{}: Expect Fraction(0, 1)".format(frac5 * frac6))

    # error tests
    # print("{}: Expect ZeroDivisionError".format(Fraction(33,0)))
    # print("{}: Expect ZeroDivisionError".format(7 / frac5))
'''
