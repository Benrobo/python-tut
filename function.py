"""
    A function is a block of code which only runs when it is called.

    You can pass data, known as parameters, into a function.

    A function can return data as a result.
"""

# In Python a function is defined using the def keyword:

def myname():
    return "benaiah"

print(myname())

"""
    Arguments
    Information can be passed into functions as arguments.

    Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

    The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:
"""

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


"""
    Parameters vs Arguments.
    
    This term is often used quite the same. 
    Parameters is a variable often passed to function definition or when the function is first created.
    
    An argument is the value that is sent to the function when it is called.
"""

def test(name): # parameter
    return name
test("benrobo") # arguments


"""
    Arbitrary Arguments, *args
    If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

    This way the function will receive a tuple of arguments, and can access the items accordingly:
"""

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

"""
    The pass Statement
    function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
"""

def myfunction():
  pass


"""
    Recursion
    Python also accepts function recursion, which means a defined function can call itself.

    Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

    The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.

    In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).

    To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it.
"""

# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion(6)


# LAMBDA FUNCTION

"""
    A lambda function is a small anonymous function.

    A lambda function can take any number of arguments, but can only have one expression.
    
    lambda arguments : expression
"""

# The expression is executed and the result is returned:

x = lambda a : a + 10
print(x(5))

# Lambda functions can take any number of arguments:

x = lambda a, b : a * b
print(x(5, 6))

x2 = lambda arr: [x*2 for x in arr]

print(x2([1,2,3,4,5]))

# Use lambda functions when an anonymous function is required for a short period of time.