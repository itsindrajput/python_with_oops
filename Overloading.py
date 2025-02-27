"""
Operator and method overloading in Python allows us to use the same operators or methods with different behaviors depending on the operands or the object they're called on.
For every operator Magic Methods are available. To overload any operator we have to override 
that Method in our class. 
"""

"""
print(10*3)
print('Hello'*3)
"""



"""
class Book:
    def __init__(self,pages):
        self.pages = pages

    def __add__(self, other): #Python calls book1.__add__(book2).
        return self.pages + other.pages
 
book1 = Book(100)
book2 = Book(200)
print("Total No. of Books = ", book1 + book2)
"""





"""
class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return Book(self.pages + other.pages) 

book1 = Book(100)
book2 = Book(200)
book3 = Book(300)

print("Total No. of Pages = ", (book1 + book2 + book3).pages)
"""