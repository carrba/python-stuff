#!/usr/bin/python3

def pl(mylist):
    for item in mylist:
        print(item)

x = ["apple", "banana", "grapes"]
# print(x[0])

x.append("orange")
#pl(x)

# extend adds another list to the list
x.extend(["pear","melon"])

# delete the last element of a list
x.pop()
#pl(x)    

# delete a specific named item from the list. (Note: Only eremoves the first occurance of "banana" in the list)
x.remove("banana")
pl(x)

# delete a numbered item
del(x(1))

# Can cast a strig to a list
s = "brian"
mylist = list(s)
mylist.pop()
# join converts a list to a string. Using someing othre than "" would add that value between each character
s2 = "".join(mylist)
print(s2)

# Sorted and sort. Sorted doesn't cahnge the list just returns it sorted. sort mutates the list and sorts it
# So if you assign a variable to sorted it will be referencing a new list
mylist2 = sorted(mylist)
mylist.sort()
mylist.reverse() # also mutates the list

# If you do the following you'rejust creating a pointer or refererence or alias to the original list
l2 = mylist
# Doing this will add this element to mylist and l2, as the point to the same list
l2.append("n")
# To make a new list from an existing list you clone the list as follows
l3 = mylist[:]
