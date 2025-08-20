for i in range(10):
    print(i) # 1 2 3 4 5 6 7 8 9
print("==============")
for i in range(1, 10):
        print(i) # o/p 1 2 3 4 5 6 7 8 9
print("==============")
for i in range(1, 10, 3):
        print(i) # o/p : 1 4 7
print("==============")
for i in range(10, 1, -3):
        print(i) # o/p : 10 7 4
print("==============")
str = "Prashant Panwar"
for i in str:
    print(i)

## while loop
count=0
while count<5:
    print(count)
    count=count+1

#Loop with else
#to check  if the loop completes normally (not broken by break)
for i in range(5):
    print(i)
else:
    print("Loop finished!")

# In this example break will stop the execution of the program and else statement will not run
# so that we can understand that loop broken by break, but not on it's own.
for i in range(5):
    if i == 4:
        break
    print(i)
else:
    print("Loop finished!")
print("=================================")

# Control in loops:
# break, continue and pass
for i in range(10):
    if i == 5:
        break # break control statement to break the loop and come out of it on a particular condition
    print(i)

print("=====================================")

for i in range(10):
    if i == 5:
        continue # control statement to skip the loop's interation for particular condition and continue it's iteration
    print(i)
print("=====================================")
for i in range(10):
    if i == 5:
        pass # The pass statement in Python is basically a do-nothing placeholder.
    print(i)



## Example- Prime numbers between 1 and 100

for num in range(1,101):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)