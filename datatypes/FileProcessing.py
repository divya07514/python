myfile = open("test")
print(myfile.read())

# To read the file again after reading it once again, you need to set the cursor at the starting point
print(myfile.read())  # This would return an empty string
myfile.seek(0)  # This would reset the cursor to the starting of the file.
print(myfile.read())  # Now full content of file can be read.
myfile.seek(0)
myfile.close()

# Best practice for file opening. No need to explicitly mention close() in this case
with open("test") as testfile:
    contents = testfile.read()
print(contents)

# Writing and reading from a file
with open("test", mode="r") as f:
    print(f.read())

with open("test", mode="a") as f:
    f.write("\nFourth Line")

with open("test", mode="r") as f:
    print(f.read())

