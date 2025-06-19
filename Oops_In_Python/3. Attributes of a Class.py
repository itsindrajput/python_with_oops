# Type Of Variables:
"""
1. Instance Object Variable [IOV]:
Defined using self.<var> inside methods.
Specific to each object (instance) of the class.
Example: self.a = a → t1.a, t2.a are IOVs.


2. Class Object Variables [COV] (Or Static Variables)
And there is no static keyword in python.
Defined inside class but outside all methods.
Shared by all instances of the class.
Example: x = 10 → x is a COV.


3. Local Variable [LC]:
Defined inside a method and not using self.
Scope is limited to the function/method where declared.
Examples: m1 = 4, a (the parameter in __init__), and self (function parameter).


4. Global Variable [GC]:
Defined outside any class or function.
Accessible throughout the module.
""" 

# Example:
"""
class Test:
    x = 10                  
    def f1():
        m1 = 4             
    def __init__(self,a):
        self.a = a          

t1 = Test(5)                
t2 = Test(7)
"""

# All the variables name in the above code:
"""
x, m1, a, t1.a, t2.a, self, t1, t2, Test, f1, __init__

x --> COV
m1 --> LV
a --> LV
t1.a, t2.a --> IOV
self --> LV
t1, t2 --> GV
Test --> GV (since, it represents Class Object)
f1 --> COV (variable to represetnt function object)
__init__ --> COV (variable to represetnt function object)
"""


#Types of functions:
"""
1. Instance method:
- These are regular methods inside a class.
- They always take self as the first parameter.
- self refers to the current object.
- Used to access and modify instance variables (unique to each object).


2. Static method:
- Defined using the @staticmethod decorator.
- Does not take self or cls as the first parameter.
- Cannot access instance (self) or class (cls) data.
- Acts like a regular function, but lives in the class namespace.


3. Class method:
- Defined using the @classmethod decorator.
- Takes cls as the first parameter, referring to the class itself.
- Can access/modify class-level variables (shared across all objects).


4. Non-member function:
- Functions that are outside any class.
- They are not related to any class or object.
"""

"""
class Test1:
    def f1(self):       #This is instance method: and it expect atleast one parameter, __init__(self) is also an instance method therefore it expect atleast one parameter called self.
        self.a = 5
        
    @staticmethod 
    def f2():           # Static method are the function which is not working for any object
        print("Hello")
        
    @classmethod
    def f3(cls):
        cls.x = 5
        
def fun4():
    print("Non member function are the function which are outside the class!")
"""


# Create and Access: 
# 1. Instance object variable   2. Class object variable

# 1. Instance object variable
"""
- Variables unique to each object.
- Created using self inside instance methods or __init__.
- Stored in the object’s __dict__.

Instance object variable can only be accessed via instance 
object.
- through __init__() via self
- through instance method via self
- through instance object
"""

"""
class Test:
    def f1(self):
        self.a = 5  # self.a is IOV
t1 = Test()         # Here t1 is instance object
t1.f1()             # f1(t1), instance object calls instance methods and pass itself as an argument internally.
"""


# 2. Class object variable
"""
- Created inside the class but outside any method.
- Shared among all objects.
- Stored in the class’s __dict__.

- It is created inside the class
- Through class name, i.e Test
And can be assessed using class_object.static variable
"""

"""
class Test:
    x1 = 7              # COV / Static variable
    
    def f1(self):
        self.a = 10
        Test.x2 = 5     # If x2 is there inside the Class then this will change its value to 5 but it is not there then it creates it.
        
    @staticmethod
    def f2():
        Test.x3 = 9
        print("Hello",Test.x3)
        
    @classmethod
    def f3(cls):
        cls.x4 = 22
        Test.x5 = 11
        print(Test.x5,"Hey",cls.x4)

t1 = Test()
Test.x4 = 17
Test.f2()           # f2()
Test.f3()           #f3(Test)
"""