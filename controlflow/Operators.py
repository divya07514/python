# Using R ange operator to generate numbers in a given range
from builtins import list

for num in range(2, 20, 2):
    print(f'Number generated is {num}')

# Using Enumerate operator to iterate using index values. It returns a tuple of index and value of item at that index.
word = "hello"
for letter in enumerate(word):
    print(letter)

print("\n")

# Using Zip operator in order to combine two separate lists.
# This operator returns a tuple of these values. Zips the values till the shortest list only.
list1 = [1, 2, 3, 5, 6]
list2 = ["a", "b", "c"]
for item in zip(list1, list2):
    print(item)

list3 = list(zip(list1, list2))
print(list3)

print("\n")

# Using IN operator to check is a value is present in a list
val = 2 in list1
print(val)
letter = "D" in "Divya"
print(letter)
d = {"k1": 2}
key = "k1" in d
val = 2 in d.values()
print(key)
print(val)

print("\n")

# Using min and max operators on lists
numlist = [10, 20, 30, 40]
print(min(numlist))
print(max(numlist))