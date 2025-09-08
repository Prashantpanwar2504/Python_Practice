# The map() Function in Python
# The map() function applies a given function to all items in an input list
# (or any other iterable) and returns a map object (an iterator).
# This is particularly useful for transforming data in a list comprehensively.
# syntax : map(function, iterables)


#  normal function
def square(x):
    return x*x

square(10)

# now if we have a list of numbers and we want a another
# list which contains a square of those number then we have to use map function
numbers = [1,2,3,4,5,6,7,8,9]
square_list = list(map(square, numbers))
print(square_list)

# we can use map function with the Lambda function
# when we are using the lambda function with map function then
# first we have to pass the arguments and the operation we want to perform
# and the list we want to map with the new list .
square_list2 = list(map(lambda x:x**2,numbers))
print(square_list2)


# Map function with multiple iterables.
num1 = [1,2,3,4,5]
num2 = [1,2,3,4,5]

# first pass arguments : operation : lists
addition_list = list(map(lambda a, b : a+b, num1, num2))
print(addition_list)


# convert a string of the number into int list

str_list = ['1', '2', '3', '4', '5']
int_list = list(map(int, str_list))
print(int_list)

# conver lower case string into upper case string

fruits = ['apple', 'banna', 'mango']
upper_fruits = list(map(str.upper,fruits))
print(upper_fruits)


# get name from the list of dictionary.

def get_name(person):
    return person['name']

people = [
    {'name' : 'Prashant', 'age' : '25'},
    {'name': 'mansi', 'age': '28'},
    {'name': 'Aditi', 'age': '24'},
    {'name': 'ma yank', 'age': '17'},
]
print(list(map(get_name, people)))

# The map() function is a powerful tool for applying transformations
# to iterable data structures. It can be used with regular functions,
# lambda functions, and even multiple iterables, providing a versatile
# approach to data processing in Python. By understanding and utilizing
# map(), you can write more efficient and readable code.