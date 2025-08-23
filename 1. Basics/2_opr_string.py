name = "Prashant"
print(name)
print(name.upper())
print(name.lower())
print(name.count("a"))
name = name.upper()
print(name)

print("=================================================")
# Split function split your string into list.
str2 = "This is python basic class, welcome to the class"
str3 = str2.split()
print(str3)
print("=================================================")
# Split by a specific character
text = "apple,banana,orange"
result = text.split(",")
print(result)
print("=================================================")
# Split by multiple spaces
text = "Python   Data   Science"
result = text.split()
print(result)
print("=================================================")
# Using maxsplit
text = "one two three four"
result = text.split(" ", 2)
print(result)
print("=================================================")
# Split by newline
text = "line1\nline2\nline3"
result = text.split("\n")
print(result)
print("=================================================")
# Practical Example – Parsing CSV values
data = "John,25,Data Scientist"
fields = data.split(",")
print(fields)
print("=================================================")
# Related function: rsplit()
text = "a-b-c-d"
print(text.rsplit("-", 2))
