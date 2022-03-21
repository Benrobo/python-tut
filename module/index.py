import fibo # without naming
import fibo as fib # with naming
import platform # built-in modules
from platform import system # with from keyword


"""
    Module
    
    A file containing a set of functions you want to include in your application.
"""

# Without naming
fibo.fib(10)

# With naming
fib.fib(20)

# Naming a module
"""
    Naming a module can be done by making use of the as keyword
    
    import mymodule as my
    
    my.function()
"""

# Built-in Modules

# There are several built-in modules in Python, which you can import whenever you like.

x = platform.system()
print(x)

# Using the dir() Function
# There is a built-in function to list all the function names (or variable names) in a module. The dir() function:

x = dir(platform)
# print(x)

# From module
# you can choose to some part of a defined module using from keyword

sys = system()
print(sys) # windows