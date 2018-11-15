def square(num):
    return num ** 2;


mynums = [1, 2, 3, 4, 5, 6]
for x in map(square, mynums):
    print(x)

print(list(map(square, mynums)))
print(list(map(lambda num: num ** 2, mynums)))


def splicer(mystring):
    if len(mystring) % 2 == 0:
        return "Even"
    else:
        return mystring[0]


names = ["Divya", "Komal", "Saurav"]
print(list(map(splicer, names)))


def check_even(num):
    return num % 2 == 0


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(filter(check_even, numbers)))
