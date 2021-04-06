#!/usr/bin/python3

class coordinate (object):
    def __init__ (self, x, y):
        self.x = x
        self.y = y

    def distance (self, other):
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5

    # The __str__ defines what will be ruturned when you print
    # an object instance
    def __str__ (self):
        return "<"+str(self.x) + "," + str(self.y) + ">"

    # There are lots of other special operators that you can define,
    # such as __add__, __sub__, __eq__, __lt__, __len__

# Create an object of type coordinate
# myobj = corrdinate(3,4)