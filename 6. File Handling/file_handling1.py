# File handling is a crucial part of any programming language.
# Python provides built-in functions and methods to read from
# and write to files, both text and binary. This lesson will
# cover the basics of file handling, including reading and
# writing text files and binary files.



# reading whole file in a single command
with open('demo.txt', 'r') as file:
    content = file.read()
    print(content)
    # content2 = file.readline()
    # content3 = file.readlines()

print("===============")


#  reading a file line by line
with open('demo.txt', 'r') as file2:
    for line in file2:
        print(line) # you will get one extra linespace after every print statement
        print("--------------")

    print("After using Strip")
# print(line.strip())  # strip() removes the newline character, if you are not going to use the Strip then
# you will get one extra line after every line you got the console screen.
with open('demo.txt', 'r') as file3:
    for line in file3:
        print(line.strip())
        print("--------------")


# Writing a file with overwriting, old data will be gone

with open('demo.txt', 'w') as file4:
    file4.write('Hello  this is the new data\n')
    # content=file.read()
    # print(content)

with open('demo.txt', 'r') as file5:
    content = file5.read()
    print(content)


#  right now we are not abl;e to understand this concept to we will come on this later and will continue.
#  right now you should focus on that your bus is about to leave soon so please start packing your bag.
# thank & Regard
#  Prashant Panwar
#  A succesful push to git server