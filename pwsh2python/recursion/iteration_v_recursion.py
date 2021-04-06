#!/usr/bin/python3.6

# To "dot source" these functions: "python -i iteration_v_recursion.py"

def factorial_iter(n):
    prod = 1
    for i in range(1,n+1):
        prod *= i
    return prod

def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)