
"""
   String are on eof python data-type which are either enclosed with single quotes '' or double quotes " ". Python treats single quote as double quote
"""
print("")

# single line

a = "welcome ben"

# multiline string

b = """
    This is a multiline string
"""

# STRINGS are Arrays

# strings in Python are arrays of bytes representing unicode characters. python does not have a character datatype, each characters within a string has an index position

#  Square brackets can be used to access elements of the string. 

# SLICING STRINGS 


b = "ben"

# print(b[1])

# To access substrings, use the square brackets for slicing along with the index or indices to obtain your substring

b = "welcome to python programming"

# print(f"""
#     b[0]: {b[0]}
#     b[0:7]: {b[2:7]}
#     b[2:]: {b[2:]}
    
# """)

# Update a string by  slicing

b = "hello world"

# print(f"""
#     Updated string: {b[:6] + " python"}       
# """)

# raw string

#  running this code without the r flag, would lead to an error

# a = "C:\user\\benrobo"

# print(a) # error


newstr = r"C:\user\\benrobo"
# print(newstr)

# Looping through a string

# for i in "benaiah":
#     print(i)
    
# String Length

# To get the length of a string, use the len() function.
a = "Hello, World!"
# print(len(a))

# Check String

# checking if a certain character is present withicn a string we can make use of the "in" keyword

a = "benrobo"

# print("c" in a) # Boolean (True or False)

# Check if NOT

# we can make use of the "not in" keyword to check if a certain character isnt present within a string

a = "benrobo is here"

# print("benr" not in a) # Boolean (True or False) 

# Unicode String 
# Normal string are stored internally as 8-bit ASCII while unicode string are 16-bit unicode

a = u"unicode string"

# STRINGS METHODS

# Capitalize

a = "string methods"

b = a.capitalize()

# print(b)

# Uppar :- change the string 

b = a.upper()

print(b)






 