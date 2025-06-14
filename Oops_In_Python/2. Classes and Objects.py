# Defining Class:
"""
Syntax:                     Example:
class ClassName:            class Student:
    variables                   name = "Abhi"
    functions                   def display(self):
                                    print(self.name)
"""


# Creating Object:
"""
class Student:
    name = "Abhi"
    def display(self):
        print(self.name)
s1 = Student()              # Object 1
s2 = Student()              # Object 2
s1.display()
"""


# Instance Object & Class Object:
"""
class Student:
    name = "Abhi"       # class object variables.
    def display(self):
        print(self.name)
        
If we create a class in Python, which means we have created Class Object. And there will be only one class object of a class. Variables inside the class objects are called class object variables.


s1 = Student()          # Instance Object 1
s2 = Student()          # Instance Object 2
In Python object are generally called instance object. Instance objects are empty objects at the time of creation.
Here, Student() will create an instance object and s1 and s2 are refering to that instance object. And if any variables are created inside the instance object are called instance object variable.
"""


# Type Of Variables:
"""
1. Global Variable
2. Local Variable
3. Class Object Variables.
4. Instance Object Variable
"""


# __init__() method:
"""
class Test:
    x = 5
    y = 6
    def __init__(self,a):
        self.a = a

t1 = Test(6)            # __init__(t1,6)
t2 = Test(8)            # __init__(t2,8)
"""


# Encapsulation:
"""
Act of combining properties and methods related to the same entity (An entity is something that exists separately from other things and has a clear identity of its own).

Example: Student -> Common Noun -> class
properties: rollno, name, std, section
methods: change_section(), promote_class(), enrollStudent()

attributes = properties + methods (if it is inside a class)
"""