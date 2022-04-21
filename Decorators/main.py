from timer import Timer
from count import CountDown

"""
    Decorators
    
    They dynamically alter the functionality of a function, method, or
    class without having to directly use subclasses or change the source code of the decorated function. 
    When used correctly, decorators can become powerful tools in the development process. This topic covers implementation and
    applications of decorator functions in Python.
    
    By definition, a decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it.
    
    Put simply: decorators wrap a function, modifying its behavior.
"""

# Decorators augment the behavior of other functions or methods. Any function that takes a function as a parameter
# and returns an augmented function can be used as a decorator.

def sayHello(name):
    return name

def greet(greetMe):
    print(greetMe("benrobo"))
    
# greet(sayHello)

"""
    Simple Decorators
    Now that you’ve seen that functions are just like any other object in Python, you’re ready to move on and see the magical beast that is the Python decorator. Let’s start with an example:
"""

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

sayWhee = my_decorator(say_whee)

# sayWhee()
# Something is happening before the function is called.
# Whee!
# Something is happening after the function is called.

"""
    Python allows you to use decorators in a simpler way with the @ symbol, sometimes called the “pie” syntax. The following example does the exact same thing as the first decorator example:
"""

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")
    
# say_whee()

# So, @my_decorator is just an easier way of saying say_whee = my_decorator(say_whee). It’s how you apply a decorator to a function.

# Simpler form

def mult(func):
    return func

@mult
def test(a,b):
    print(a*b)

# test(2,2)    

"""
    Sometimes, we would wanna pass an arguments to a function, but when arguments isnt passed, would lead to an error.
"""

def custom_decor(func):
    
    def wrapper():
        func()
    return wrapper

@custom_decor
def greet(name):
    print(f"hello, {name}")
    
# greet() # greet() missing 1 required positional argument: 'name'

"""
    As you can see, the above decorator function throws an error. To fix this, The solution is to use *args and **kwargs
"""

def custom_decor(func):
    
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper

@custom_decor
def greet(name):
    print(f"hello, {name}")
    
# greet("benrobo")

"""
    Returning Values From Decorated Functions
    What happens to the return value of decorated functions? Well, that’s up to the decorator to decide. Let’s say you decorate a simple function as follows:
"""

def custom_decor(func):
    
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper

@custom_decor
def greet(name):
    print(f"hello, {name}")
    return f"welcome, {name}"

# greeter = greet("benrobo") # hello, ben

# print(greeter) # None

"""
    As you can see above, we were expecting "welcome, benrobo" to get showned, but why? that because, our decorator function doesnt explicitly return a value, but a function. To fix this, we need to tell our decorator function to return a value
"""

def custom_decor(func):
    
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper

@custom_decor
def greet(name):
    print(f"hello, {name}")
    return f"welcome, {name}"

# greeter = greet("benrobo") # hello, ben

# print(greeter) # welcome, benrobo

# Find how many milliseconds it took a function to run

@Timer
def loop(start):
    for i in range(start):
        pass
        
# loopVal = loop(1)

# print(loopVal)

@CountDown
def counter(num):
    a = 0
    for x in range(num):
        a += 1
        print(a)
        
# val = counter(6)
# print(val)

"""
    Classes as Decorators. 
    
    Recall that the decorator syntax @my_decorator is just an easier way of saying func = my_decorator(func). Therefore, if my_decorator is a class, it needs to take func as an argument in its .__init__() method. Furthermore, the class instance needs to be callable so that it can stand in for the decorated function.

    For a class instance to be callable, you implement the special .__call__() method:
"""


class Decorator:
    
    def __init__(self, func):
        self.func = func
    
    def __call__(self,  *args, **kwargs):
        print("beforfe calling function")
        res = self.func(*args, **kwargs)
        print("after calling function")
        return res
    
    
@Decorator
def test(name):
    print(f"welome {name}")
    
# test("ben")

# This can also be used to idenityfy a loggedIn user


class IsLoggedIn:

    def __init__(self, func):
        self.func = func
        self.currentUser = "benrobo"
    
    def __call__(self, *args, **kwargs):
        userName = "benrobo"
        if userName != self.currentUser:
            return print("user with that name doesnt exists")
        return self.func(*args, **kwargs)
        
@IsLoggedIn
def loginUser(name):
    print(f"welcome {name}")
    
loginUser("ben")