#/usr/bin/env python3
import random

def pickwinner():
    pw =  random.randint(1,3)
    return pw

def pickwindow():
    pick = random.randint(1,3)
    return pick

def showgoat(playerchoice, winner):
    if playerchoice != winner:
        thegoat = 6 - winner - playerchoice
        return thegoat
    else:
        


