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




print("===============")