# Lists are ordered sequences that hold variety of object types
my_list = [1, 2, 3]
my_list_mixed = ["STRING", 100, 3.14]
print(len(my_list))

# One more way to create lists
altway = [1] * 3
print(altway)

# Index search in a list
print(my_list[1])
# Index based list data manipulation
my_list[0] = 12
print(my_list)

# Adds the element at the end of the list. Its a permanent change in the list structure
my_list.append(4)
print(my_list)

# Removes the element at the end of the list. Its a permanent change in the list structure
popped = my_list.pop()
print(popped)
print(my_list)

# List sorting operations. Sort is an in place operation. It does not return any thing.
char_list = ['a', 'v', 'q', 'o', 'i']
num_list = [5, 8, 7, 3, 1, 6]
char_list.sort()
num_list.reverse()
print(char_list)
print(num_list)

# Slicing a list
print(my_list[:2])
print(my_list[1:])
print(my_list[0:2:1])

# List concatenation
print(my_list + my_list_mixed)

# List comprehensions are a unique  way of quickly creating lists with python
# Traditional way of creating lists.
newlist = []
for letter in "hello":
    newlist.append(letter)
print(newlist)

# In this way, we assume that the only thing we doing on list is appending
mylist = [letter for letter in "hello"]
print(mylist)
mylist = [x for x in range(1, 9)]
print(mylist)
# Operations can be done on the elements being added to the list.
mylist = [x for x in mylist if x % 2 == 0]
print(mylist)