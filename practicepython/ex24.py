#!/usr/bin/python3

boardsize = input("Enter board size, E.g. 8 for chess, 19 for Go etc ")

printsize = int(boardsize)
across = "----"
down = "|   "
rows = 0

while rows < printsize:
    print(printsize * across)
    print((printsize + 1) * down)
    rows += 1
print(printsize * across)