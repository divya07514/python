class Animal():

    def __init__(self, name):
        self.name = name
        print("Animal Created")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")


class Dog(Animal):

    def __init__(self,name):
        Animal.__init__(self, name)
        print("Dog created")

    def eat(self):
        print("Doggy is eating")

    def speak(self):
        print("Doggy is speaking")


dog = Dog("Neela")
dog.speak()


class Cat():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says meow !!!"


class Horse():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says neighh !!! "


def pet_speak(pet):
    print(pet.speak())


pet_speak(Cat("Niko"))
pet_speak(Horse("Ghoda"))
