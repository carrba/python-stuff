#!/usr/bin/env python3.6

def make_shirt(size = "large", text = "I love Python"):
    print(f"T-shirt size is {size} with this logo : {text}\n")

mysize = input("Please enter the T-shirt size, or none to exit ")
mytext = input("Please enter T-shirt logo \n")

make_shirt() 
make_shirt(text=mytext)
make_shirt(text=mytext, size=mysize)
