"""
# Arithmatic Operators: +, -, *, /, //, %, **
a = 5
b = 3
c = 2.5

print(a%c) # And return integer if both are interger, return float if any one is float 
print(a%b) # Give the Reminder
print(a//c) 
print(a//b) # Floor Division similar to C/C++, gives us quotient
# And return integer if both are interger, return float if any one is float 
print(a/b) # Actual Division as of Maths and always return a float value
print(a**b) # Power
print(a*b) # Multiplication
print(a-b) # Substraction
print(a+b) # Addition
"""


"""
#______________________________________________________________________________________________________________
# Relational Operators: <, >, <=, >=, ==, !=
print(4>5) # False 
print(6>0) # True 
print(6>5>4) # True 
print(10>8>6>4>2) # True 
"""


"""
#______________________________________________________________________________________________________________
# Logical Operators: and, or, not
print(not True) # False 
print(3>4) # False 
print(not 3>4) # True
print(4>1 and 3<10) # True, True/False are bool type of result.
print(6<9 or 1>4) # If anyone out of two are True the result will be True.

print("Seeta" or "Geeta") # Seeta, Here Operand are of str type
# When ever logical operator are applied are non boolean expression the result are also non bool type.
# Logic is: non empty string are considered as True and empty string are considered as False.
# So Based on above explaination, 1st will check LHS of 'or' -> will get a non empty str type -> so True, and in case-of 'or' if 1st operand is True result will be True. Therefore we can say that in case of 'or' result depends on 1st operand if it gets True.

print("Ram" and "Shyam") # Shyam
#1st will check LHS of 'and' -> will get a non empty str type -> so True, and in case-of 'and' if 1st operand is True we have to also check for 2nd operand -> which is also True. Therefore we can say that in case of 'and' result depends on 2nd operand.

print(3 and 4) # 4, Non Zero numbers are True, Zero is False.
print(0 and 5) # 0, First Check for Zero and Non Zero, then based on or/and decide result.
print(0 or 5) # 5
"""


#______________________________________________________________________________________________________________
# Bitwise Operators: & (AND), | (OR), ^ (XOR), ~ (NOT), << (LEFT SHIFT), >> (RIGHT SHIFT)
"""
| A | B | A & B (AND) | A \| B (OR) | A ^ B (XOR) |
| - | - | ----------- | ----------- | ----------- |
| 0 | 0 | 0           | 0           | 0           |
| 0 | 1 | 0           | 1           | 1           |
| 1 | 0 | 0           | 1           | 1           |
| 1 | 1 | 1           | 1           | 0           |

"""


#______________________________________________________________________________________________________________
# Assignment Operators: =, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=


#______________________________________________________________________________________________________________
# Identity Operators: is, is not
x = 5
y = 5 # In this case python will not create a new object, instead it will assign the id of 5 in y as a reference and now y will also point to the same object. And now x & y will contain same id.
z = 7

"""
•	Python tracks how many references point to each object using a reference counter.
•	When an object’s reference count drops to zero, Python’s Garbage Collector frees the memory.

"""

"""
print(id(x))
print(id(y)) 

print(x is y) # Prints's True as x and y have same id.
print(x is z) # False
print(x is not z) # True
"""

#______________________________________________________________________________________________________________
# Membership Operators: in, not in
# x in y  y can be iterable/collection of elements
# y cann't be int, float, bool, complex
# y can be list, tuple, set, dict, range, str etc.

a = "Rishabh"
print("Ri" in a) # True

"""
b = 1234
print(1 in b) #TypeError: argument of type 'int' is not iterable
"""