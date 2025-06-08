# Introduction:
"""              
lambda is a keyword, using this we can write function in a single line.
lambda expression are syntactically restricted to a single expression.

lambda input:expression
lambda a,b : a+b

no need of def keyword, no need of return keyword
"""

"""
def add(a,b):
    return a+b
s= add(3,4)
print(s)                        # 7

y = add
print(y)                        # <function add at 0x0000020B759D1440>

print(id(add))                  # 1532913325120
print(id(y))                    # 1532913325120

print(y is add)                 # True, bez both are referencing to same object.

print(add(5,6))                 # 11
print(y(5,6))                   # 11
"""



# Now as we were calling y(), similarly we can consider `lambda a,b: a+b` as one expression. And can pass arguments directly.
"""
print((lambda a,b:a+b)(3,5))     # 8, but this can done only once

print((lambda a,b:a+b)(3,4))     # 7

f1 = lambda a,b : a+b            # Reusabiltiy
print(f1(10,20))                 # 30
"""



# Recursion Using Lambda: Calculate factorial of a number using recursive lambda expression.
"""
def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
print(factorial(5))                # 120


f = lambda n: 1 if n==0 or n==1 else n*f(n-1)
print(f(5))                        # 120
print(f(100))
"""

"""
factorial = (lambda f: lambda n: 1 if n <= 1 else n * f(f)(n-1))(lambda f: lambda n: 1 if n <= 1 else n * f(f)(n-1))
print(factorial(5))  # 120
"""



# lambda with the built-in functions: map(), filter(), and reduce()
# 1. map() applies a function to every item in an iterable.
"""
numbers = [1,2,3,4]
sq = list(map(lambda x: x**2, numbers))
print(sq)                           # [1, 4, 9, 16]
"""


# 2. filter() returns only the items that satisfy a condition (i.e., where the lambda returns True).
""""
data = [1,4,5,6,7,8,10]
evendata = list(filter(lambda y:y%2==0,data))
print(evendata)
"""


# 3. reduce() applies a function cumulatively to the elements of a sequence.
"""
from functools import reduce
numbers = [1,2,3,4]
listmul = reduce(lambda x,y : x*y, numbers)
print(listmul)                        # 24
"""


"""
Final Tip for Mastery
Use lambda when:
•	The function is short and used temporarily.
•	You want a clean, concise alternative to def.
•	Inside higher-order functions like map, filter, sorted, reduce.
Avoid it when:
•	Logic is complex.
•	Readability is crucial.
•	You need multi-line functionality or docstrings.

"""