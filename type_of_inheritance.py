#1. Single Inheritance:
"""
class P:   
    def m1(self):   
        print("Parent Method")   
class C(P):   
    def m2(self):   
        print("Child Method")   
c=C()   
c.m1()   
c.m2()  
"""



#2. Multi Level Inheritance
"""
class P:   
    def m1(self):   
        print("Parent Method")   
class C(P):   
    def m2(self):   
        print("Child Method")   
class CC(C):   
    def m3(self):   
        print("Sub Child Method")   
c=CC()   
c.m1()   
c.m2()   
c.m3()   
"""



#3. Multiple Inheritance:
"""
class P1:   
    def m(self):   
        print("Parent1 Method")   

class P2:   
    def m(self):   
        print("Parent2 Method")   

class C(P1, P2):  
    def m1(self):   
        print("Child2 Method")   

c = C()   
c.m1()  
c.m()   
print(C.__mro__)  # Checking MRO
"""



#4. Hierarchical Inheritance:
"""
class P:   
    def m1(self):   
        print("Parent Method")   
class C1(P):   
    def m2(self):   
        print("Child1 Method")   
class C2(P):   
    def m3(self):   
        print("Child2 Method")   
c1=C1()   
c1.m1()   
c1.m2()   
c2=C2()   
c2.m1()   
c2.m3()   
"""




#5. Hybrid Inheritance:
"""
class A:
    def show(self):
        print("Class A")

class B(A):
    def show_B(self):
        print("Class B")

class C(A):
    def show_C(self):
        print("Class C")

class D(B, C):
    def show_D(self):
        print("Class D")

obj = D()
obj.show()    
obj.show_B()  
obj.show_C()   
obj.show_D()  
"""



#6. Cyclic Inheritance: 
#
# class A(A):pass