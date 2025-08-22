# Tuple
# An ordered, immutable collection. You can not modifiy or change the element \
# Used for fixed data (e.g., coordinates, config values).
# Can store multiple type of Data type.
# duplicates are allowed

my_tuple = (1, 2, 3, 3, 'p', 'p', 'r', 2, 5)

# index start from 0
print(my_tuple)
print(type(my_tuple))
print(my_tuple.count(1))
print(my_tuple.index('p'))
# print(my_tuple.index(9))
# when you try to get the index of
# the element which is not present in the tuple
# or list then you will get an error : "ValueError: tuple.index(x): x not in tuple"

# Key Properties
# Ordered → elements remain in order.
# Immutable → cannot be changed after creation.
# Duplicates allowed.
# Supports indexing & slicing.
# my_tuple[3] = 0
print(my_tuple[3])
print(my_tuple.index('p'))
#slicing
print(my_tuple[0:10:2])
print("===================================")
t = (10, 20, 30, 40, 50, 60, 70)
print(t)
print(t[1:4])    # (20, 30, 40)
print(t[:3])     # (10, 20, 30)
print(t[3:])     # (40, 50, 60, 70)
print("===================================")
# Using Step
print(t[::2])    # (10, 30, 50, 70)   → every 2nd element
print(t[1::2])   # (20, 40, 60)       → odd index elements
print("===================================")
# Negative indexing
print(t[-3:])    # (50, 60, 70) from Last 3rd to end
print(t[:-2])    # (10, 20, 30, 40, 50) from starting to second last.

