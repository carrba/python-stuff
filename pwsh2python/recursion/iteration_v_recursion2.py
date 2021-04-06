#!/usr/bin/python3.6

# To "dot source" these functions: "python -i iteration_v_recursion.py"

def mult_iter(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result

def mult(a, b):
    if b == 1:
        return a
    else:
        return a + mult(a, b-1)