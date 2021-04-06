#!/usr/bin/python3.6

def divide (numerator, denominator):
    myint = numerator // denominator
    myfraction = numerator % denominator
    return (myint, myfraction)

num = int(input("Enter the numerator "))
den = int(input("Enter the denominator "))
(whole, fraction) = divide (num, den)

if fraction == 0:
    print("Answer is", fraction)
else:
    print("Answer is", whole, "remainder", fraction)