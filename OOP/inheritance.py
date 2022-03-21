"""
    Python Inheritance

    Inheritance allows us to define a class that inherits all the methods and properties from another class.

    Parent class is the class being inherited from, also called 
    "base" class.

    Child class is the class that inherits from another class, also called "derived" class.
"""

# Parent class aka Base Class
# Child class aka Derived Class

# Parent class

class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printname(self):
        return print(self.name)
    
    def getaddr(self):
        return print("address is me")

    

p1 = Person("benaiah", 20)

# p1.printname()

# Creating child class
# To inherit all methods from parent class, simply add the parent class name within the child class name.



class Students(Person):
    pass

stu = Students("michael", 20)

stu.printname()


"""
    Use the super() Function
    Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
    
    By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.
"""

class Students(Person):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__(name, age)
        self.gradYear = 2021
    
    def courses(self):
        courses = {
            "name": "CE / CS"
        }
        return print(courses)
    
    def gYear(self):
        return print(f"Student would graduate on {self.gradYear}")


stu = Students("michael", 20)

stu.getaddr()
stu.courses()
stu.gYear()
