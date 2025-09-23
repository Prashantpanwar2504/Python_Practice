# The filter() Function in Python: The filter() function constructs an iterator from elements
# of an iterable for which a function returns true. It is used to filter out items from a list
# (or any other iterable) based on a condition.
#
#
# Filter the array, and return a new array with only the values equal to or above 18:
#

def even(num):
    if num%2 == 0:
        return True

list1 = [23,643,25,6,32,5,673,24,254,8,63,3,6,13,6,38,5,6,53,34]

even_list = list(filter(even, list1))
print(even_list)



#  filter number which are greater than 5
list2 = [1,2,5,6,3,7,3,8,4,453,23,7,4,8,4,56,3]

greater_than_five = list(filter(lambda x : x>5, list2))
print(greater_than_five)


## Filter with a lambda function and multiple conditions
greater_than_five_and_even = list(filter(lambda x : x>5 and x%2==0,  list2))
print(greater_than_five_and_even)



## Filter() to check if the age is greate than 25 in dictionaries
people=[
    {'name':'Krish','age':32},
    {'name':'Jack','age':33},
    {'name':'John','age':25}
]

def age_greater_than_25(person):
    return person['age']>25

age_greater_24 = list(filter(age_greater_than_25,people))
print(age_greater_24)

# The filter() function is a powerful tool for creating iterators
# that filter items out of an iterable based on a function.
# It is commonly used for data cleaning, filtering objects,
# and removing unwanted elements from lists.By mastering filter(),
# you can write more concise and efficient code for processing and manipulating collections in Python.


# for the name of the contribution tothe github profile.
# Don't know what i am doing with my life.
#10 days without any contribution.