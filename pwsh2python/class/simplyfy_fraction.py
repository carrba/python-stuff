#!/usr/bin/python3

#!/usr/bin/python3

def simplify (x, y):
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

def check_prime (x, y):
    pri = (3,5,7,11,13,17,19,23)
    for i in pri:
        if (x % i == 0) and (y % i == 0):
            return i
    return 0