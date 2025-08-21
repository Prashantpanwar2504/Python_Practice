# 1. List
# An ordered, mutable, and dynamic collection in Python.
# Can hold elements of mixed data types.
# Most commonly used data structure in Python.

# Key Properties
# Ordered → preserves insertion order.
# Mutable → can change elements.
# Duplicates allowed → same value can appear multiple times.
# Indexing & slicing → supports positive & negative indexing.

my_list = [1 , 2, 4, "Prashant", 2]
print(my_list)
# you can also get list element using for loop
for i in my_list:
    print(i)


print(my_list[0]) # first element
print(my_list[-1]) # last element
print(my_list[1:4]) # slicing
print(my_list[::-1]) # reverse list
print(my_list)
print("=======================")
# | Method             | Description             | Example                   |
# | ------------------ | ----------------------- | ------------------------- |
# | `append(x)`        | Add element to end      | `my_list.append(99)`      |
# | `insert(i, x)`     | Insert at position      | `my_list.insert(2, "AI")` |
# | `extend(iterable)` | Merge another iterable  | `my_list.extend([1,2,3])` |
# | `remove(x)`        | Remove first occurrence | `my_list.remove(20)`      |
# | `pop([i])`         | Remove & return element | `my_list.pop()`           |
# | `index(x)`         | Get index of element    | `my_list.index("Python")` |
# | `count(x)`         | Count occurrences       | `my_list.count(30)`       |
# | `sort()`           | Sort ascending          | `my_list.sort()`          |
# | `reverse()`        | Reverse list            | `my_list.reverse()`       |
# | `copy()`           | Shallow copy            | `new = my_list.copy()`    |
# | `clear()`          | Remove all elements     | `my_list.clear()`         |

my_list.append(45)
# my_list.insert(2, "AI") # other element will shift to the right side.
# my_list.extend(['s', 'e', 'x']) # right merge
print(my_list)
my_list.remove("Prashant")
print(my_list)
print(my_list.sort()) # ONLY WORK SAME TYPE OF DATA
my_list.pop() # pop last element.
print(my_list)

list1 = ["abd", "pra", "sha", "n4t", "ntr", "aaa", "aab", "aca"]
list1.sort()
print(list1)

#sallow copy of list
copy_lst = list1.copy()
print(copy_lst)

#remove duplicates from the lsit

list3 = [1 ,2 ,4 ,8 ,4 ,2 ,7 ,9 ,4 ,2 ,6 ,9 ,5 ,3 ,5 ,8 ,5 ,3 ,6 ,3 ,7 ,3 ,7 ,7 , 8, 6, 3, 3, 7]
unique_list = []
for i in list3:
    if i not in unique_list:
        unique_list.append(i)
print(unique_list)

