#Introduction:
"""
Function is a block of code/statement which when called perform some specific task. And Function has a name for identification.

# Function Definition:
def functionName(args):
    code
    code

# Function Calling:
functionName(parameters)        
"""

# Example:
"""
def greet():
    print("Hello","Rishabh")
    
greet()
""" 


# Local and Global Variable:

# Local Variable: A variable declared inside a function and accessible only within it.
"""
def show():
    x = 10          # local variable
    print(x)

show()              
#print(x)            # Error – x is not accessible outside
"""


# Global Variable: A variable declared outside all functions and accessible everywhere.
"""
x = 100               # global variable
def display():
    print(x)
display()


# If you modify a global variable inside a function, use the global keyword.
x = 50
def update():
    global x
    x = 200
update()
print(x)               # Output: 200
"""


# Ways to define a function:
"""
1. Takes Nothing, Returns Nothing
2. Take Something, Return Nothing
3. Take Nothing, Return Something
4. Take Something, Return Something
"""

# 1. Takes Nothing, Returns Nothing
"""
def add():
    print("Enter two numbers:")
    a = int(input())
    b = int(input())
    print("Sum =",a+b)
    n 
add()
"""


# 2. Take Something, Return Nothing
"""
def multiplication(a,b):            # a & b are formal arguments
    c = a*b
    print("Result =",c)
    
print("Enter Two Numbers:")
multiplication(10, 20)              # 10 & 20 are Actual Arguments
"""


# 3. Take Nothing, Return Something
"""
def volume():
    print("Enter length, width and height to calculate volume of a cuboid: ")
    l = int(input())
    w = int(input())
    h = int(input())
    v = l*w*h
    return v

result = volume()
print("Volume =", result)
"""


# 4. Take Something, Return Something
"""
fact = 1
def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact *= i
    return fact

user_input = int(input("Enter a number to calculate its factorial: "))
result = factorial(user_input)
print("Factorial =",result)
"""