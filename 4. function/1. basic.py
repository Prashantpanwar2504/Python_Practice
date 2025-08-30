# A function is a block of code that performs
# a specific task. Functions help in organizing code,
# reusing code, and improving readability.

def function():
    print("you are inside of a function.")


function()
print("----------------------------------")


# Arguments:Information can be passed into functions as arguments.
# --> Arguments are specified after the function name, inside the parentheses.
# --> You can add as many arguments as you want, just separate them with a comma.

def myname(name):
    print("My name is " + name)


myname("Prashant Panwar")


def fullname(fname, lname):
    print(fname + " " + lname)


fullname(lname="Prashant", fname="Panwar")
fullname("Prashant", "Panwar")  # observe the difference
# fullname("prashant") # fullname() missing 1 required positional argument: 'lname'
print("--------------------------------")


# Arbitrary Arguments, *args : If you do not know how many arguments that will be
# passed into your function, add a * before the parameter name in the function definition.

def myfunction2(*args): # positonal arguements
    print("The youngest childrens are :" + args[3])


myfunction2("ram", "prashant", "rahul", "aman")


# Arbitrary Keyword Arguments, **kwargs : If you do not know how many keyword arguments that will be passed into your function,
# add two asterisk: ** before the parameter name in the function definition.
def myfunction3(**kwargs): # keyword arguments
    print("My last name is " + kwargs["lname"])

myfunction3(fname="Prashant", lname="Panwar")
print("-----------------------------------------")

# default parameter
def my_function4(country = "Norway"):
  print("I am from " + country)

my_function4("Sweden") # if you pass the parameter the it function will get it and print it.
my_function4("India")
my_function4() # if you don't pass the parameter then it will pass the default paramter that was asigned while you define the function
my_function4("Brazil")
print("------------------------------------------")

# Passing a List as an Argument
def my_function5(list):
    for i in list:
        print(i)

numbers = [1,2,3,4,5, "d",6,7,8,9]
my_function5(numbers)


print("---------------------------------")

def function6(i):
    i%2 == 0

function6(91)
print(function6(35)) # will return the value of none, if no return given

print("------------------------------------")
# Return Values
def my_function8(x):
  return 5 ** x

print(my_function8(3))
print(my_function8(5))
print(my_function8(9))

print("------------------------------------")
# Positional-Only Arguments : You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
def my_function9(a,b,c,/,d,e):
  print(a)
  print(b)
  print(c)
  print(d)
  print(e)

my_function9( a = 'a', 'b', 'c', 'd', 'e') # SyntaxError: positional argument follows keyword argument