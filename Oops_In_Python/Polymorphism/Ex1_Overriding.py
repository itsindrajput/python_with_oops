# Basic Implementation Of Method Overriding
"""
class Parent:
    def property(self):
        print("Gold + Land + Cash + Power")

    def marry(self):
        print("Marry Priya")
    
class Child(Parent):
    def marry(self):
        print("Marry Roshni")
    
c = Child()
c.property()
c.marry()
"""




# Assessing Parent Class methods using super() from child class
"""
class Parent:
    def property(self):
        print("Gold + Land + Cash + Power")

    def marry(self):
        print("Marry Priya")
    
class Child(Parent):
    def marry(self):
        super().marry()
        print("Marry Roshni")
    
c = Child()
c.property()
c.marry()
"""




# Basic Implementation Of Constructor Overriding
"""
class P:
    def __init__(self):
        print("Parent Class Constructor")

class C(P):
    def __init__(self):
        super().__init__()
        print("Child Class Constructor")

c = C()
"""


