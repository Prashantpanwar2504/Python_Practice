# basic example
# a=b
# print(a)
# you will get an error
# NameError: name 'b' is not defined
# you have to handle the code/

try:
    a = b
except:
    print("Set some value to b, before executing the code")

try:
    c = d
except NameError as ne:
    print(ne)

try:
    r = 19 / 0
except ZeroDivisionError as ze:
    print(ze, "please enter a non zero number in denominator")

print("---------------------------")
try:
    result = 123 / 0
    a = k
except ZeroDivisionError as de:
    print(de)
except Exception as e1:
    print(e1)

# Line 2: result = 123 / 0 → This will raise ZeroDivisionError because division by zero is not allowed.
# Line 3: a = k → This will raise a NameError (caught as Exception) because 'k' is not defined.
# Important:
# After an exception is caught, Python skips the rest of the try block.
# That means the line:
print("---------------------------")
try:
    a = k
    result = 123 / 0  #this line of code will not be caught by the try block
except Exception as e1:
    print(e1)
    print("this block of code will handle all the exception ")


print("--------------------------------------")

try:
    num=int(input("Enter a number"))
    result=10/num
except ValueError:
    print("This is not a valid number") # if you entered string or character then this exception will print
except ZeroDivisionError: # if you will comment this part then still Main Exception will catch the error.
    print("enter denominator greater than 0")   # if you insert 0 then this exception will print
except Exception as ex:
    print(ex)



print("-----------------------")

## try,except,else block
try:
    num = int(input("Enter a number:"))
    result = 10 / num
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
except Exception as ex:
    print(ex)
else:
    print(f"the result is {result}")

print("----------------------------")

## try,except,else and finally
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
except Exception as ex:
    print(ex)
else:
    print(f"The result is {result}")
finally:
    print("Execution complete.")