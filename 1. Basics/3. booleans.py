#
# status = 'yes'
# while status == "yes":
#     a = int(input("enter a number:"))
#     b = int(input("Enter second number:"))
#
#     if a > b:
#         print(a)
#         status = input("Wants to continue?")
#     else:
#         print(b)
#         status = input("Wants to continue?")

# Evaluating values and variables

# x = "Hello"
# y = 1
# print(x, bool(x))  # empty string will always return false, Any string is True, except empty strings.
# print(y, bool(y))  # 0 as a number wil return  false, Any number is True, except 0.
# print(bool("abc"))
# print(bool(123))
# print(bool([1,2,3]))
# print(bool([]))  #Any list, tuple, set, and dictionary are True, except empty ones.

# Some Values are False
# print(bool(False))
# print(bool(None))
# print(bool(not False))
# print(bool(not True))
# print(bool(not 0))
# print(bool(not 1))
# print(bool(""))
# print(bool(not ""))
# print(bool(()), type(())) #tuple
# print(bool({}), type({})) #dictionary
# print(bool([]), type([])) #list


# if you class is returning to the object of it's class then it will be false or 0.
class myclass():
    def __len__(self):
        return 0;


my_obj = myclass()
print(my_obj)
print(bool(my_obj))
print(type(my_obj))

# functin can return boolean

def myFunction1():
    return True
print(myFunction1())

def myFunction2() :
  return True

if myFunction2():
  print("YES!")
else:
  print("NO!")

# Python also has many built-in functions that return a boolean value,
# like the isinstance() function, which can be used to determine
# if an object is of a certain data type:
x = 200
print(isinstance(x, float))