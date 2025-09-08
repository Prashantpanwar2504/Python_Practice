# Lambda Functions in Python
# Lambda functions are small anonymous functions defined using the lambda keyword.
# They can have any number of arguments but only one expression.
# They are commonly used for short operations or as arguments to higher-order functions.

#Syntax
# lambda arguments: expression

addition = lambda a, b : a+b
print(type(addition))
a = int(input("Enter a:"))
b = int(input("Enter b:"))
print(addition(a, b))

print("----------------------")

is_even = lambda  a : a%2 == 0
print(is_even(a))
# Output:
# will return True if even, else False

print("----------------------")
## map()- applies a function to all items in a list
numbers = [1,2,3,4,5,6,7,8,9]
print(list(map(lambda x:x**2,numbers)))