
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

# Capitalize :- Return a copy of the string with its first character capitalized and the rest lowercased.

a = "string methods   "

b = a.capitalize()

# print(b)

# Uppar :- change the string to an uppecrcase

b = a.upper()

# print(b)

# LOWERCASE :- change the string to lowercase

b = a.lower()

# STRIP :- remove white space

b = a.strip()

# print(f"'{b}'")

# REPLACE :- replaces a string with another string:

b = a.replace("string", "ben")

# print(b)


# SPLIT :- convert a string to a list or an array using the split("seperator")

b = "welcome, ben".split(',')

# print(b)

# ENCODE :- Return an encoded version of the string as a bytes object

b = "benrobo".encode(encoding="utf-8")

# print(b)

# Title :- returns all title case of the string

b = "welcome to python".title()

# print(b) 


# ESCAPE CHARACTER

# To insert characters that are illegal in a string, use an escape character.

# An escape character is a backslash \ followed by the character you want to insert.

# An example of an illegal character is a double quote inside a string that is surrounded by double quotes:


sent = "We are the so-called \"Vikings\" from the north."

# print(sent)


#  VALIDATE STRINGS
    
# isdigit() :- check if a string is an interger
# islower() :- check if a string is lowercase

b = a.isdigit() # False or True
c = a.islower() # False or True

# print(c)

# JOIN :- Return a string which is the concatenation of the strings in iterable

b = "welcome ben".join("-")

print(b)


# Get how many times a word appear within a string using the count() string method

sentense = "I love programming, I love computing"

count = sentense.count("love")

print(count)