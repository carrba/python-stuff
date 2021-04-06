#!/usr/bin/python3

class fraction(object):
    """
    A number represented as a fraction
    """
    def __init__(self, num, denom):
        """ num and denom are integers """
        assert type(num) == int and type(denom) == int, "ints not used"
        self.num = num
        self.denom = denom
        def simplify(x, y):
            """ Simplifies a fraction """
            if x % 2 > 0:
                if y % x > 0:
                    # Check Prime
                    prime = check_prime(x, y)
                    if prime == 0:
                        return str(int(x)) + "/" + str(int(y))
                    else:
                        return simplify ((x / prime), (y / prime))
                else:
                    return str(int(x/x)) + "/" + str(int(y/x))
            else:
                return simplify ((x / 2), (y / 2))
        def check_prime(x, y):
            """ Function used by simplify to check prime number division of num and denom """
            pri = (3,5,7,11,13,17,19,23)
            for i in pri:
                if (x % i == 0) and (y % i == 0):
                    return i
            return 0
    def __str__(self):
        """ Retunrs a string representation of self """
        (x, y) = simplify ((self.num), (self.denom))
        return str(x) + "/" + str(y)
    def __add__(self, other):
        """ Returns a new fraction representing the addition """
        top = self.num*other.denom + self.denom*other.num
        bott = self.denom*other.denom
        return fraction(top, bott)
    def __sub__(self, other):
        """ Returns a new fraction representing the subtraction """
        top = self.num*other.denom - self.denom*other.num
        bott = self.denom*other.denom
        return fraction(top, bott)
    def __float__(self):
        """ Returns a float value of the fraction """
        return self.num/self.denom
    def inverse(self):
        """ Returns a new fraction representing 1/self """
        return fraction(self.denom, self.num)