print("Demo program")
name = "Prashant Panwar" #string
age = "25" #strinh
salary = 67000.561 #strinh

print(f"my name is {name}, my age is {age}, my salary is {salary}")
print(type(age))
print(type(name))
print(type(salary))


# this will give you error, because type() can not take more than one argument
# print(type(name, age, salary))
print(type(age), type(name), type(salary))