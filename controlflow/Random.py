from random import shuffle
from random import randint

# Using random library. Shuffle is an inplace function. Shuffles values of list in place.
numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
shuffle(numlist)
print(numlist)

print("\n")

# Using randint function to create a list of randon integers
randlist = []
for item in range(10):
    randlist.append(randint(20, 50))
print(randlist)


# Using input to take values from user at runtime. Input accepts all values as string only.
# Cast values as int(input_value) to convert the value into int. Same goes for other data types too
name = input("Say my name!!!")
print(f'Name is {name}')
