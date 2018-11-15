# A function is a piece of code that is called by name. It can be passed data to operate on
# (i.e., the parameters) and can optionally return data (the return value).
# All data that is passed to a function is explicitly passed.

def name_function():
    '''
    Info about name function
    :return:
    '''
    print("hello")


def other_name_function(name):
    '''
    Information about other name function
    :param name:
    :return:
    '''
    return f'Hello {name}'


name_function()
var = other_name_function("Divya")
print(var)


# Using *args, arbitrary number of arguments can be given to the methods.
# Args return a tuple

def sum_func(*args):
    return sum(args) * 0.05


var = sum_func(40, 60, 50, 50)
print(var)


# The special syntax **kwargs in function definitions in python is used to pass a keyworded, variable-length argument list.
# A keyword argument is where you provide a name to the variable as you pass it into the function.
# Kwargs return a dictionary

def myfunc(**kwargs):
    print(kwargs)
    if "fruit" in kwargs:
        print(f'My fruit of choice is {kwargs["fruit"]}')
    else:
        print("No fruit found")


myfunc(fruit='apple', veggie="cucumber")


def myfunc(*args):
    lst = []
    for n in args:
        if n % 2 == 0:
            lst.append(n)
    return lst


lst = myfunc(10, 2, 3, 4, 5, 6)
print(lst)


def animal_crackers(text):
    word_list = text.split()
    return word_list[0][0] == word_list[1][0]


print(animal_crackers("Level  Lama"))


def old_macdonald(name):
    first = name[:3]
    second = name[3:]
    return first.capitalize() + second.capitalize()


print(old_macdonald("macdonald"))


def sentence_reverse(text):
    word_list = text.split()
    return " ".join(word_list[::-1])


print(sentence_reverse("Divya Thakur"))


def has_33(nums):
    for i in range(0, len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False


print(has_33([1, 2, 4, 5, 6, 3, 3, 6, 3]))


def paper_doll(text):
    final_text = ""
    for char in text:
        final_text = final_text + char * 3
    return final_text

print(paper_doll("Hello"))


