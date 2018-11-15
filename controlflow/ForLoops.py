mylist = [1, 3, 5, 6, 8, 10]
for item in mylist:
    print(item)

print("\n")

# Printing only even numbers
listsum = 0
for item in mylist:
    if item % 2 == 0:
        print(f'Even number {item}')
    else:
        print(f'Odd Number {item}')
    listsum = listsum + item
print(f'Sum of items in the list is {listsum}')
print("\n")

name = "DivyaThakur"
for char in name:
    print(char)
print("\n")

# Tuple unpacking
typlelist = [(1, 2), (3, 4), (5, 6)]
for (a, b) in typlelist:
    print(a)
    print(b)
print("\n")

# Iterating over dictionaries By default you only iterate over keys
mydict = {"k1": 1, "k2": 2}
for (key, value) in mydict.items():
    print(f'Key is {key} and value is {value}')
