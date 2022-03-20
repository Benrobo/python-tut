
"""
    Python Operators
    Operators are used to perform operations on variables and values.

    In the example below, we use the + operator to add together two values:
"""

"""
    Python divides the operators in the following groups:

    Arithmetic operators
    Assignment operators
    Comparison operators
    Logical operators
    Identity operators
    Membership operators
    Bitwise operators
"""

# Arithmetic Operators

a = 10
b = 20
c = 27

add = a+b
sub = a-b
mult = a*b
division = b/a
mod = b%a # returns the modulus or remainder when divided
expo = a**2 # returns the Exponentiation 10^2 
floordiv = c//a # floor division. it simply divides the number without decimal place

# print(f" 
#     {add} \n 
#     {sub} \n 
#     {mult} \n 
#     {division} \n 
#     {mod} \n 
#     {expo} \n 
#     {floordiv} 
# ")


# Assignment Operators

a += 10 # or a = a + 10
b = 100
c *= 2 # or c = c * 2
# a **= 2 # or a = a^2
a >>= 1

# print(a)

#  Logical Operators

# Logical operators are used to combine conditional statements:

# AND :- Returns True if both statements are true otherwise returns false

# print( "name" == 23 and "name" == "name" )

# OR :- Returns True if one of the statements is true

# print( "name" == 23 or "name" == "name" )

#  NOT :- Reverse the result, returns False if the result is true

# print(not(10 < 5 and 20 < 10))

# Identity Operators :- Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# IS :- Returns True if both variables are the same object

# print(a is b)  # returns True case int == int

# IS NOT :- Returns True if both variables are not the same object

# print(a is not a) # returns false cause int == int which is true, and the opposite of True is false

# Membership Operators

# IN :- Returns True if a sequence with the specified value is present in the object

# print("ben" in "benrobo") # return True cause "ben" is present

# NOT IN :- Returns True if a sequence with the specified value is not present in the object

print("name" not in "benrobo") # return True cause "name" is not present