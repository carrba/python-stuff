#!/usr/bin/python3.6

def divide (numerator, denominator):
    myint = numerator // denominator
    myfraction = numerator % denominator

    if myfraction == 0:
        print("Answer is", myint)
    else:
        print("Answer is", myint, "remainder", myfraction)



num = int(input("Enter the numerator "))
den = int(input("Enter the denominator "))
divide (num, den)