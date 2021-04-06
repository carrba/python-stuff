#!/usr/bin/env python3.7
numsafe = 101
mydict = {}
for x in range(numsafe):
    dictname = "dict" + str(x)
    mydict[dictname] = 0

for x in range(numsafe):
    if x > 0:
        for y in range(numsafe):
            if y % x == 0: 
                # Flip bit on dict
                dictname = "dict" + str(y)
                if mydict[dictname] == 0:
                    mydict[dictname] = 1
                else:
                    mydict[dictname] = 0

for x in range(numsafe):
    dictname = "dict" + str(x)
    if mydict[dictname] == 1:
        print(dictname)
