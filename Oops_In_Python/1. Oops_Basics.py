# Introduction:
"""
## Procedural Programming:
Procedural Programming is a method of organizing your code by dividing it into a set of functions . These functions can call each other to perform various tasks, enhancing code reusability and efficiency.

In Procedural Programming, you start with a main function that calls other functions as needed. Each function performs a specific task and can call other functions to accomplish more complex operations. 

For instance, if you're developing software for a university system with entities like students , faculty , and courses , you would need to pass large amounts of data between functions, leading to complex and hard-to-maintain code.


## Object-Oriented Programming:
Object-Oriented Programming ( OOP ) offers a better way to organize your code, especially for larger and more complex software systems. Instead of dividing your code into functions, OOP breaks it down into a set of entities or objects . Each object represents a real-world entity and contains both data and methods that operate on that data.

For example, in a university system, you can create separate classes for Student , Faculty , and Course . Each class encapsulates all the relevant data and methods related to that entity.

By bundling data and methods together within classes, OOP reduces the need to pass large amounts of data between functions. Objects can interact with each other by calling each other's methods, which simplifies the overall structure of the code.
"""


# Classes and Objects in OOPs:
"""
## Class:
Classes and objects are key parts of OOP in Python. A class is a blueprint for creating objects, defining data types, attributes, and methods for those objects. 

## Object:
An object is created from a class, using memory for its data members, like C1 and C2 from the Complex class.

## Classes vs. Objects
A class is like a blueprint for a house, while an object is an actual house built from that blueprint. The class defines the structure and behavior, and objects are the tangible instances created based on that definition.

## Comparison with Other Languages
In languages like C++ and Java, there are primitive types (e.g., int, float) and class types. Python differs because every type in Python is a class, and even basic variables are instances of classes. This uniformity simplifies the language's design and usage.
"""

# Example: Creating a Class in Python
"""
class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    
    def print(self):
        print(str(self.real) + " + " + str(self.img) + "i")
    
    def add(self, C):
        self.real += C.real
        self.img += C.img
    
c1 = Complex(10,20)
c1.print()              # 10 + 20i

c2 = Complex(20,30)
c1.add(c2)
c1.print()              # 30 + 50i
"""


# Constructors in Python
"""
A constructor is a special method used to initialize objects when they are created. In Python, the __init__ method serves as the constructor. It sets up the initial state of an object by assigning values to its data members.

## The self Reference
self is a special reference used within class methods to refer to the current instance of the class. It allows access to the object's data members and other methods. This is similar to the this keyword in C++ and Java.

self is the special reference used to access the data member of the current class. 
When we write methods inside the class, the first parameter we pass is `self. This indicate that we need to provide reference on which this method will get called. It gives us reference to the object on which we calling the method.
"""


# Using Methods to Manipulate Objects
"""
Methods like print and add perform specific operations on an object's data members. The print method displays the complex number in a readable format, while the add method adds the real and imaginary parts of another Complex object to the current object.

Accessing Members with the Dot Operator
The dot operator (.) is used to access an object's methods and data members. For example, C1.print() calls the print method of the C1 object, and C1.real accesses the real data member of C1.
"""


# Advantages of Object-Oriented Programming
"""
Object-oriented programming (OOP) is a widely used programming paradigm that organizes software design around objects. The main advantages include:

Modularity: Code is organized into separate classes, making it easier to manage and maintain.
Reusability: Classes can be reused across different programs, reducing redundancy.
Scalability: OOP makes it easier to scale software by adding new classes and objects.
Maintainability: Encapsulation ensures that objects manage their own data, leading to fewer bugs and easier updates.
"""


"""
Nouns, also called naming words, are used to name people, places, animals, objects and ideas.
Nouns are of two main types: Proper nouns and common nouns. 
1. Common nouns: Common nouns are those nouns that refer to a generic item, group or place.
Ex: boy, girl, pet, animal, housefly, college, Home, 

2. Proper Nouns: Nouns that are used to name a person, place or thing specifically are called a proper noun. Proper nouns always begin with a capital letter.
Ex: John, The Sun, The Taj Hotel, The White House
"""