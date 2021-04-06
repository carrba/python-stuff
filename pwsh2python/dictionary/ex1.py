#!/usr/bin/python3

my_dict = {}

grades = {'Ana':'B', 'John':'A+', 'Denise':'A', 'Katy':'A'}

# add an entry
grades.['Sylvan'] = 'A'

# test if key in dictionary
'John' in grades
'Sylvan' in grades
# or
'Ana' in grades.keys()

# test if value in dictionary
'A' in grades.values()