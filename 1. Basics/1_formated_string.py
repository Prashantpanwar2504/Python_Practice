print("Demo program")
name = "Prashant Panwar" #string
age = "25" #string
salary = 67000.561 #strinh

print(f"my name is {name}, my age is {age}, my salary is {salary}")
print(type(age))
print(type(name))
print(type(salary))

# this will give you error, because type() can not take more than one argument
# print(type(name, age, salary))
print(type(age), type(name), type(salary))


#function to find the length of the string.
string_test = "Hello, this is prashant panwar, how you doing."
print(string_test.find('e'), string_test.find('g'), string_test.find('q'))
# when you try to fins a char which  is not present
# in the string then you will get -1 as return val


#length of the string
