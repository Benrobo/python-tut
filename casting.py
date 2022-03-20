
"""
    There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

    Casting in python is therefore done using constructor functions:
       int() :- construct an integer from an interger literall, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
       
       float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
       
       str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals
"""
print("")

# converting to interger

# x = int(1)   # type is now int
# y = int(2.8) # type is now int
# z = int("3") # type is now int

#  converting to string

x = str(1)   # type is now str
y = str(2.8) # type is now str
z = str("3") # type is now str


print(type(x), type(y), type(z), x)