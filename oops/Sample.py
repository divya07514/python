class Dog:
    # Class Object Attribute
    # Same for any instance of a class

    species = "Mammal"

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    # Methods are functions defined inside the bode of the class and they utilize class attributes.
    def bark(self):
        return f'{self.name} is barking'


my_dog = Dog("Doggy", "LKA")
print(my_dog.breed)
print(my_dog.name)
print(my_dog.species)
print(my_dog.bark())
