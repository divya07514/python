print(" Hi I am Divya Thakur")
print(len("Divya"))
# String var declaration
myString = "Divya Thakur"
# String indexing
print(myString[4])
print(myString[-2])
# String slicing (getting substring from given index till end of the string)
print(myString[2:])
# String slicing (getting substring from given starting  index till end the given index. stop index is exclusive)
print(myString[:7])
# String slicing (getting substring between twp given indexes)
print(myString[0:4])
# String slicing (getting substring from start till end in given step size. Default step size is 1)
print(myString[::2])
print(myString[1:9:2])
# String reverse using step size . Just a nice to know trick
print(myString[::-1])

# String are immutable in python just like they are in java
name = "Sam"
name_lastLetters = name[1:]
newName = "P" + name_lastLetters
print(newName)
# making multiple copies of a string at a time
alpha = "a"
print(alpha * 10)

# Available Strings functions
newName = "mridul thakur"
print(newName.upper())
print(newName.split(" "))
print("This is a nice String".split("i"))

# String formatting
print("Hello {}".format("World"))
print("The {2} {1} {0} ".format("fox","brown","quick"))
# F string formatting
name = "World"
print(f"Hello {name}")



