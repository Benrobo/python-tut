# Decorators

They dynamically alter the functionality of a function, method, or
class without having to directly use subclasses or change the source code of the decorated function. 
When used correctly, decorators can become powerful tools in the development process. This topic covers implementation and
applications of decorator functions in Python.

By definition, a decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it.

## Put simply: decorators wrap a function, modifying its behavior.

```py

    def Decorator(func):

        def wrapper():
            print("before calling function")
            res = func()
            print("after functional call")
            return res
        return wrapper
    
    @Decorator
    def test():
        print("Function called")
    
    test() 

    # Same way as
    def Decorator(func):

        def wrapper():
            print("before calling function")
            res = func()
            print("after functional call")
            return res
        return wrapper
    
    def test():
        print("function call")
    
    test = Decorator(test)

    test()

```