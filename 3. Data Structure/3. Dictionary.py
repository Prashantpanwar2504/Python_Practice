# Dictionary :
# An unordered, mutable, key-value mapping.
# Keys must be unique and hashable (immutable types like string, int, tuple).
# Values can be of any type.

my_dic = {
    'a': "one",
    'b': "two",
    'c': "three",
    'd': "four",
    'e': "five",
    'f': True,
    'g': False,
    'h': None
}
print(my_dic)
# print(my_dic[3]) # Dictionary does not support indexing, unorderes set
# print((my_dic[0:4])) # Dictionary Does not Support Slicing
print("=========================================")
# Dictionary can store a list as a value in it
my_dict = {"name": "Alice", "age": 25, "skills": ["Python", "ML"]}
print(my_dict["skills"])
print("====================================")

# Key Properties
# Mutable → can add, modify, delete.
# Unordered (before Python 3.7) but insertion-ordered from Python 3.7+.
# Fast lookups via hash tables.


# Important Data Scinece interview question, often asked question in the interview.
# Iterating a List inside a Dictionary
data = {
    "fruits": ["apple", "banana", "mango"],
    "numbers": [10, 20, 30, 40],
    "cities": ["Delhi", "Mumbai", "London"]
}
# Iterate over a specific key
for key in data:
    print(f"Items in {key}:")
    for value in data[key]:
        print("  -", value)
# Iterate over all key-value pairs
for key, value in data.items():
    print(f"{key} -> {value}")

print("====================================")

# Handling real-world JSON (API style)
students = {
    "classA": ["Alice", "Bob", "Charlie"],
    "classB": ["David", "Eva"]
}

for classname, students_list in students.items():
    print(f"{classname} has students:")
    for student in students_list:
        print("   ", student)
# When asked about this, always mention that dictionaries
# map keys to values, and if the value is a list,
# you must iterate twice → first over dictionary keys,
# then over list item.

# Important Methods of Dictionary
# | Method            | Description                           | Example                              |
# | ----------------- | ------------------------------------- | ------------------------------------ |
# | `get(key)`        | Safe access (returns None if missing) | `my_dict.get("age")`                 |
# | `keys()`          | All keys                              | `my_dict.keys()`                     |
# | `values()`        | All values                            | `my_dict.values()`                   |
# | `items()`         | Key-value pairs                       | `my_dict.items()`                    |
# | `update({...})`   | Merge dicts                           | `my_dict.update({"city":"Delhi"})`   |
# | `pop(key)`        | Remove & return value                 | `my_dict.pop("age")`                 |
# | `popitem()`       | Remove last item                      | `my_dict.popitem()`                  |
# | `setdefault(k,v)` | If missing, set key                   | `my_dict.setdefault("salary", 5000)` |
# | `clear()`         | Empty dictionary                      | `my_dict.clear()`                    |

print("====================================================")
my_dict4 = {
    "name": "Alice",
    "age": 25,
    "skills": ["Python", "ML"],
    "city": "Delhi"
}
# get(key[, default]) : Safely access value (returns None or default if key is missing).
print(my_dict4.get("name"))
print(my_dict4.get("salary"))
print(my_dict4.get("salary", 23000)) #temp key-value pair
print(my_dict4)

# keys() : Returns all keys.
print(my_dict4.keys()) # it can not take any parameter

# values() : return all the value
print(my_dict4.values())

# items() : Returns all key-value pairs as tuples.
print(my_dict4.items()) # same as print(my_dict4)

# update({key:value}) : Add or modify items.
my_dict4.update({"age": 26, "country": "India"})
print(my_dict4)

# pop(key[, default]) : Remove and return value for the given key.
print(my_dict4.pop("city"))  # Delhi
print(my_dict4)
# popitem() : Removes and returns the last inserted key-value pair.
print(my_dict4.popitem())
# ('country', 'India')
print(my_dict4)
# setdefault(key[, default]) :
# If key exists → return its value.
# If missing → insert with default value.
print(my_dict4.setdefault("age", 30))     # 26 (already exists)
print(my_dict4.setdefault("salary", 5000)) # 5000 (added)
print(my_dict4)
# {'name': 'Alice', 'age': 26, 'skills': ['Python', 'ML'], 'salary': 5000}
print("=======")
# clear() : Removes all items from dictionary.
my_dict4.clear()
print(my_dict4)   # {}



print("==============================================")

students = {
    "101": {"name": "John", "marks": [80, 90, 85]},
    "102": {"name": "Emma", "marks": [78, 88, 92]},
    "103": {"name": "Raj", "marks": [70, 75, 80]}
}

# My solution
for roll, details in students.items():
    print(roll,  sum(details["marks"])/len(details["marks"]))


print("--------------------------------")
# Print each student with average marks
for roll, details in students.items():
    avg = sum(details["marks"]) / len(details["marks"])
    print(f"Roll No: {roll}, Name: {details['name']}, Average: {avg}")


