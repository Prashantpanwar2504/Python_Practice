# Dictionary :
# An unordered, mutable, key-value mapping.
# Keys must be unique and hashable (immutable types like string, int, tuple).
# Values can be of any type.

my_dic = {
    'a' : "one",
    'b' : "two",
    'c' : "three",
    'd' : "four",
    'e' : "five",
    'f' : True,
    'g' : False,
    'h' : None
}
print(my_dic)
# print(my_dic[3]) # Dictionary does not support indexing, unorderes set
# print((my_dic[0:4])) # Dictionary Does not Support Slicing
print("=========================================")
# Dictionary can store a list as a value in it
my_dict = {"name": "Alice", "age": 25, "skills": ["Python", "ML"]}
print(my_dict["skills"])
print("====================================")

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
# then over list items.