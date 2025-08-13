print("Demo program")
name = "Prashant Panwar"  # string
age = "25"  # string
salary = 67000.561  # strinh

print(f"my name is {name}, my age is {age}, my salary is {salary}")
print(type(age))
print(type(name))
print(type(salary))

# this will give you error, because type() can not take more than one argument
# print(type(name, age, salary))
print(type(age), type(name), type(salary))

# function to find the length of the string.
string_test = "Hello, this is prashant panwar, how you doing."
print(string_test.find('e'), string_test.find('g'), string_test.find('q'))
# when you try to fins a char which  is not present
# in the string then you will get -1 as return val

# Replacement function for string
course = "python for beginner"
print(course.replace('beginner', 'absolute beginner'))
course = course.replace('beginner', 'advance')
print(course)

# In operation : to check whether string present in the string or not.
str_cs = "hello, this is python for beginner but not for advance, so invest yourself accordingly"
print('invests' in str_cs)
# major difference b/w find and in operator is,
# find function return the index of the substring,
# but in operator return boolean value True/False


# length of the string
str = "hello world, this is python for beginner."
print(len(str))