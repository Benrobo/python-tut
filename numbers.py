from random import randrange, seed
from math import pow, floor, cos


"""
    There are three numeric types in Python:
        int
        float
        long
        complex
        
    They are immutable data types, means that changing the value of a number data type results in a newly allocated object.
"""
print("")

x = 100    # int
y = 2.8  # float
z = 1j   # complex

# use the DEL (del) keyword to delete a variable

del y

# convert variable of one data-type to another using int() float() complex()

# newx = complex(x)

# Mathematical Functions

"""
    abs(x) :- The absolute value of x: the (positive) distance between x and zero.
    ceil(x) :- The ceiling of x: the smallest integer not less than x
    min(a,b) :-  get the minimum numbers between interget a and b
    max(a, b) :- get the maximum numbers between interget a and b
    pow(x, y) :-  Get the power of varaible x or x**y, where y is the raise-to number
"""

newx =  randrange(12) # x**y
 
print(newx)