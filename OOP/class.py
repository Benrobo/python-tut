"""
    Python Classes/Objects
    Python is an object oriented programming language.

    Almost everything in Python is an object, with its properties and methods.

    A Class is like an object constructor, or a "blueprint" for creating objects.
"""

# Create a class named MyClass, with a property named x:

class MyClass:
    x = 5
    
# Now we can use the class named MyClass to create objects:

name = MyClass()

# print(name.x)


# The __init__() function
"""
    Every class created in python has a built-in function called __init__()
    this function get called as soon as the class get instantiated/created
    
    Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
    
    If you're farmiliar with constructor() method in javascript, the __init__() function does the same features.
"""

class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("benaiah", 20)

# print(p1)


# Object Methods

# Class can also contain functions known as methods which is meant to fufil certain tasks.

class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # methods
    def info(self):
        return f"Hello, my name is {self.name.upper()} and I am {self.age}yrs old"
    
    
p1 = Person("benaiah", 20)
p1.age = 25

# del p1.age  # delete object properties

print(p1.info())

# Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.




