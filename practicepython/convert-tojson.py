#!/usr/bin/env python3
from os import path
import json
thefile = input("Enter file to create json file from ")
thesep = input("Enter row separator ")
if path.exists(thefile):
    # Create output file name based on input
    thejsonfile = (thefile.split("."))[0]
    thejsonfile = thejsonfile + ".json"
    # Create empty dictionary object to hold birthdays
    mydict = {}
    with open(thefile) as birthdays:
        for data in birthdays:
            splitdata = data.split(thesep)
            thekey = splitdata[0]
            theval = splitdata[1]
            mydict[thekey] = theval
        
    with open(thejsonfile, "w") as outfile:
        json.dump(mydict, outfile)