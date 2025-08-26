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
print("========================")

# clear : to clear or empty a set.
s.clear()
print(s) # it will return set()
print("=========================")
s = {"apple", "banana", "cherry"}
# union : combine two set.
print(my_set.union(s))
set1 = {1,2,3, 4, 6}
set2 = {3,4,5, 8,3}
print(set1.union(set2)) # {1, 2, 3, 4, 5, 6, 8}
print(set1.intersection(set2)) # {3, 4}
print(set1.difference(set2)) # {1, 2, 6}
print(set2.difference(set1)) # {8, 5}
# symmetric_difference : Returns a new set with elements that
# are in either set, but not in both
# In math terms → (A∪B)−(A∩B).
print(set1.symmetric_difference(set2))
# example
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print("A: ", A, "B:", B)
result = A.symmetric_difference(B)
print(result)   # {1, 2, 5, 6}
print("=========================")
# issubset : check of b is the subset of a
a = {1,2,3,4,5,6,7,8,9}
b = {3,5,8,1}
print(b.issubset(a)) # b is the subset of a. that's we are getting True.
print(a.issuperset({})) # a is the superset of empty set {}
print(a.issuperset(b)) # a is the superset of b
print(a.issuperset(a)) # is also the superset of a itself.
print("==========================")

# isdisjoint: check if there is not any common elements.
c = {'b'}
print(a.isdisjoint(c)) # will get True because a and c set does not hab=ve anything in common.





