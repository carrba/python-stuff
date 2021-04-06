#!/usr/bin/env python3
from os import path
birthdayfile = "birthdays.txt"
if path.exists(birthdayfile):
    print("Welcome to the birthday dictionary. We know the birthday of:")
    # Create empty dictionary object to hold birthdays
    mydict = {}
    with open('birthdays.txt') as birthdays:
        for data in birthdays:
            splitdata = data.split(":")
            name = splitdata[0]
            birthday = splitdata[1]
            mydict[name] = birthday
            print(name)

    val = ""
    while len(val) == 0:
        req = input("Whose birthday do you want to look up? ")
        req = req.title()
        try:
            val = mydict[req]
            print(f"{req}'s birthday is on {val}")
        except:
            print(f"{req} not found in the dictionary")
