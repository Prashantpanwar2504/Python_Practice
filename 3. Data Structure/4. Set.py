# Practice of Set
# Definition : An unordered, mutable collection of unique elements.
# Based on hash tables.

my_set = {1, 2, 3, 4, 5, 'd', 5, 6, 7, 8, 9, 10}
print(my_set)
# if you try to store same value multiple time then it will store it only one time
# because in set repetition of the value is not allowed


# Key Properties
# --> No duplicates allowed.
# --> Unordered → no indexing/slicing.
# --> Very fast for membership checks.

# important method of sets
# add() to add element in the set.
my_set.add(19)
print(my_set)
print("====================")
# update(iterable) : Add multiple values in the set
my_set.update([11, 12]) # update() can take multiple iterables at once
print(my_set)
print("====================")
# example
A = {1, 2, 3}
B = {3, 4, 5, 1}
print(B)
A.update(B)
print(A)
print("'===================")

#  remove : to remove an element from the set, if element is not present in the set
# then you will get an error
my_set.remove(4)
print(my_set)
my_set.remove("d")
print(my_set)
print("====================")

# discard : same as remove function but if the element is not present in the set then
# it will not give you an error.
my_set.discard("g")
print(my_set)
print("====================")

# pop : remove random item from the set
# Removes and returns an arbitrary element from the set.
# arbitrary (not random in the mathematical sense, but unpredictable for you).
print(my_set.pop())
print(my_set)
print(my_set.pop())
print(my_set)

# example
s = {"apple", "banana", "cherry"}

while s:
    fruit = s.pop()
    print("Processing:", fruit)

print("Set is now empty:", s)



