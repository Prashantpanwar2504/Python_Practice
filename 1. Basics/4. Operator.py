# x = 20
# y = 3

# print(x + y)
# print(x * y)  # multiplication
# print(x ** y)  # power
# print(x / y)  # Division
# print(x // y)  # Floor division
# print(x % y)  # Remember


# print("-------------")
# a = 20
# a%=3  #remenber
# a*=3
# a**=3
# a//=3
# a&=20 #bitwise AND assignment operator.
# a|=10 #bitwise OR assignment operator.
# a^=17 #bitwise XOR assignment operator.
# a>>=3 #right shift assignment operator.
# a<<=3 #left shift assignment operator.
# print(a := 3)
# print(a)


print("=========================================")

num1 = float(input("Enter first number:"))
num2 = float(input("Enter Second number:"))

print(""" Press 1 for Addition          5 for Floor Division
                2 for Subtraction       6 for Modulus
                3 for Multiplication    7 for Exponential
                4 for Division""")

opr = int(input("Enter your Choice:"))

add = num1+num2
sub = num1-num2
mul = num1*num2
div = num1/num2
exp = (num1**num2)
f_div = num1//num2
mod_d = num1%num2

if opr == 1:
    print("Addition :", add)
elif opr == 2:
    print("Subtraction :", sub)
elif opr == 3:
    print("Multiplication :", mul)
elif opr == 4:
    print("Division :", div)
elif opr == 5:
    print("Floor Division :", f_div)
elif opr == 7:
    print("Exponential :", exp)
else:
    print("Modulus :", mod_d)



