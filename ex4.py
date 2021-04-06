#!/usr/bin/env python3.6

filename = input("Enter file name\n")

try:
    with open(filename) as f:
        print(f"Opening file {filename}\n")
except:
    print(f"File {filename} can't by opened\n")

try:
    line = input("Enter the line number you would like to read\n")
    for x in range (0, int(line)):
        f.readline()

    myline = f.readline()

except:
    print(f"Couldn't read line number {line}\n")

if myline:
    print(f"Below is line number {line} from {filename}\n")
    print(myline)

