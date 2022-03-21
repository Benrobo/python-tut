"""
    Python Conditions and If statements

    Python supports the usual logical conditions from mathematics:

    Equals: a == b
    Not Equals: a != b
    Less than: a < b
    Less than or equal to: a <= b
    Greater than: a > b
    Greater than or equal to: a >= b
    These conditions can be used in several ways, most commonly in "if statements" and loops.

    An "if statement" is written by using the if keyword.
"""

a = 33
b = 200
if b > a:
  print("b is greater than a")
  
  
"""
    Elif
    The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".
"""

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
  
"""
    Else
    The else keyword catches anything which isn't caught by the preceding conditions.
"""

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  
  
"""
    Short Hand If
    If you have only one statement to execute, you can put it on the same line as the if statement.
"""

if a > b: print("a is greater than b")

"""
    Short Hand If ... Else
    If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:
"""

a = 2
b = 330
print("A") if a > b else print("B")

"""
    This technique is known as Ternary Operators, or Conditional Expressions.
"""