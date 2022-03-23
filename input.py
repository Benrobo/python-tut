import math

"""
    User Input
    Python allows for user input.

    That means we are able to ask the user for input.

    The method is a bit different in Python 3.6 than Python 2.7.

    Python 3.6 uses the input() method.

    Python 2.7 uses the raw_input() method.

    The following example asks for the username, and when you entered the username, it gets printed on the screen:
"""

username = input("Enter username: ")
print(f"Username is: {username}")

# Formatted String Literals
# Formatted string literals (also called f-strings for short) let you include the value of Python expressions inside a string by prefixing the string with f or F and writing expressions as {expression}.

# An optional format specifier can follow the expression. This allows greater control over how the value is formatted. The following example rounds pi to three places after the decimal:



# print(f'The value of pi is approximately {math.pi:.4f}.') # print value of PI in 4decimal places

# Passing an integer after the ':' will cause that field to be a minimum number of characters wide. This is useful for making columns line up.

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}

# Without space between name and phone

for name, phone in table.items():
    print(f"{name} ==> {phone}")
    
# With space


for name, phone in table.items():
    print(f"{name:10} ==> {phone:10}")

