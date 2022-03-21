"""
    Python has two primitive loop commands:

    while loops
    for loops
"""

"""
    The while Loop
    With the while loop we can execute a set of statements as long as a condition is true.
"""

i = 1
while i < 6:
  print(i)
  i += 1
  
"""
    Note: remember to increment i, or else the loop will continue forever.
"""

"""
    The break Statement
    With the break statement we can stop the loop even if the while condition is true:
"""

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
  
"""
    The continue Statement

    With the continue statement we can stop the current iteration, and continue with the next:
"""

# Continue to the next iteration if i is 3:

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
  

"""
    The else Statement
    With the else statement we can run a block of code once when the condition no longer is true:
"""

# Print a message once the condition is false:

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
  
  
"""
    Python For Loops
    A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

    This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

    With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
"""

# Dictionary

ne = {"name": "ben", "age": 20}

for x in ne.items():
    print(x)
    
# Array

fruits = ["apple", "banana", "cherry"]

for x in fruits:
  print(x)
  

"""
    Looping Through a String
    Even strings are iterable objects, they contain a sequence of characters:
"""

for x in "banana":
  print(x)
  

  
"""
    The break Statement
    With the break statement we can stop the loop before it has looped through all the items:
"""

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) # apple, banana
  if x == "banana":
    break

# Exit the loop when x is "banana", but this time the break comes before the print:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x) # "apple"