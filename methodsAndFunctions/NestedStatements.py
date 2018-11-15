# LEGB rule
# Local : Names assigned in any way within a function and not declared global in that function
# Enclosing function locals - Names in the local scope of any and all enclosing functions from inner to outer
# Global - Names assgined at the top level of a module file, or declared global in a def within a file
# Built In - Names preassigned in the built in names module: open, range etc etc

# Local scope example
lambda num: num % 2 == 0

# Enclosing function locals
name = "Thakur"


def greet():
    name = "Divya"

    def hello():
        print("Hello " + name)

    hello()


greet()
