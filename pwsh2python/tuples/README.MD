t = ("pink","green")
t2 = t
t = None
t2
('pink', 'green')

When you make a variable equal to an existing tuple, it is a copy that is created,
rather than a pointer. Deleteing the original variable has no impact on the other variable.
This is in contrast to mutable types such as lists, where a new variable is a pointer to the
same obeect in memory.