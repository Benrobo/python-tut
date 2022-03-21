"""
    A variable is only available from inside the region it is created. This is called scope.

    Local Scope
    A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
"""

# A variable created inside a function is available inside that function:

def func():
    x = 100
    print(x) # 100

func()

# print(x) # name 'x' is not defined

"""
    Function Inside Function
    As explained in the example above, the variable x is not available outside the function, but it is available for any function inside the function:
"""

# The local variable can be accessed from a function within the function:

def func1():
    x = 200
    def func2():
        print(x)
    func2()
func1()    


"""
    Global Scope
    A variable created in the main body of the Python code is a global variable and belongs to the global scope.

    Global variables are available from within any scope, global and local.
"""

# A variable created outside of a function is global and can be used by anyone:

x = 300

def myfunc():
  print(x) # 300

myfunc()

print(x) # 300

"""
    Naming Variables
    If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function):
"""

x = 300

def myfunc():
  x = 200
  print(x) # 200

myfunc()

print(x) # 300

"""
    Global Keyword
    If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.

    The global keyword makes the variable global.
"""

# If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global name
  name = "benaiah"

myfunc()

print(name)


# To change the value of a global variable inside a function, refer to the variable by using the global keyword:

age = 45

def myfunc():
  global age
  age = 1000

myfunc()

print(age)
