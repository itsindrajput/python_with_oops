#In this case the python is only Considering the last method. 
#Method Overloading is not possible in Python
"""
class Addition:
    def add(self):
        print("No Arguments Passed!")
    def add(self, a):
        self.a = a
        print("Single Argument Passed! ", a)
    def add(self, a, b):
        self.a = a
        self.b = b
        print("Two arguments Passed! i.e ",a, b)

t1 = Addition()
t1.add(1,2) 
t1.add(1,4)
t1.add(1,2)
"""




#Constructor Overloading is not possible in Python
#In this case the python is only Considering the last constructor. 
class Addition:
    def __init__(self):
        print("No Arguments Passed!")
    def __init__(self, a):
        self.a = a
        print("Single Argument Passed! ", a)
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print("Two arguments Passed! i.e ",a, b)

t1 = Addition(1,3)