#!/usr/bin/python3

# To "dot source" these functions: "python -i iteration_v_recursion.py"
# Running through the code can be visualised at http://pythontutor.com/ex

def fib_efficient(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans

n = int(input("Enter fibonacci number "))
d = {1:1, 2:2}
print(fib_efficient(n, d))