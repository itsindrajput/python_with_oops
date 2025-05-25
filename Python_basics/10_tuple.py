# Introduction
"""
tuple is a class in Python

tuple is immutable (non changable), So we can't call append(), insert(), extend() method. Also we can't call pop(), remove(), clear() and del statement. If we try to call it will throw an Attribute Error.

tuple is iterable and has sequence 
tuple elements are indexed
tuple can store hetrogeneous elements.
"""


# How To Create tuple object?
"""
print(type(tuple()))        # <class 'tuple'>

t1 = (1,2,3,4,5)
print(t1)
print(type(t1))             # <class 'tuple'>

l1 = [1,2,3,4,5]
print(l1)
print(type(l1))             # <class 'list'>

t2 = (10)
print(type(t2))             # <class 'int'>

t3 = (10,)
print(type(t3))             # <class 'tuple'>

#t4 = tuple(10)
#print(type(t4))             # 'int' object is not iterable

t5 = (1,2,3,4,5)
print(type(t5))             # <class 'tuple'>
"""


# Indexing is same as of list, have both positive and negative indexing.
"""
#     0 1 2 3 4
t1 = (1,2,3,4,5)
print(t1[0], t1[2], t1[4])          # 1 3 5

#print(t1[5])                       # IndexError: tuple index out of range
"""


#Accessing Tuple Elements:
"""
t1 = (1,2,3,4,5)
print(t1[3])                         # 4  

i = 0
while (i<len(t1)):
  print(t1[i], end=" ")              # 1 2 3 4 5
  i+=1

print()  
  
for x in t1:
  print(x, end=" ")                  # 1 2 3 4 5
"""


# Built-in Methods:
"""
t2 = (5,1,7,2,4,9)
print(len(t2))                       # 6
print(max(t2))                       # 9
print(min(t2))                       # 1
print(sum(t2))                       # 28
print(sorted(t2))                    # [1, 2, 4, 5, 7, 9]
print(sorted(t2,reverse=True))       # [9, 7, 5, 4, 2, 1]
"""


#Concatenation and Repetition Operator:
"""
t1 = (1,3,5,7)
t2 = (2,4,6,8)
print(t1+t2)                          # (1, 3, 5, 7, 2, 4, 6, 8)

print(t1*3)                           # (1, 3, 5, 7, 1, 3, 5, 7, 1, 3, 5, 7)
"""


# Comparison Operator:
"""
t1 = (1,3,5,7)
t2 = (2,4,6,8)
print(t1<t2)                           # True

t3 = (10,20,30,40)
t4 = (11,33,55)
print(t3>t4)                           # False

print((1, 2, 3) > (1, 2, 2))           # True


t5 = (1,2)
t6 = (1,2)
print(t5==t6)                          # True
"""


# Tuple Object Methods: index() and count()
"""
t3 = (10,20,30,40)
print(t3.index(20))                     # 1

#print(t3.index(7))                      # ValueError: tuple.index(x): x not in tuple

print(t3.count(10))                      # 1
print(t3.count(80))                      # 0
"""


# Slicing Operator: Where ever there is a concept of indexing there we can use slicing operator.
"""
t1 = (9,5,8,2,4,7,1)
print(t1[2:7:2])                         # (8, 4, 1)
print(t1[1:])                            # (5, 8, 2, 4, 7, 1)
print(t1[::1])                           # (9, 5, 8, 2, 4, 7, 1)
print(t1[::-1])                          # (1, 7, 4, 2, 8, 5, 9)
"""


# User Input: #ake inputs from the user, each being a comma-separated string of integers, and convert them into tuples
"""
t1 = tuple([int(i) for i in input("Enter numbers with comma separate: ").split(',')])
print(t1)
"""


# Tuple Packing and Unpacking
"""
# Packing
t = 1, 2, 3
print(t)                    # (1, 2, 3)
print(type(t))        # <class 'tuple'>

# Unpacking
a, b, c = t
print(a, b, c)     	  # 1 2 3
"""


# Swapping Variables
"""
a, b = 10, 20
a, b = b, a
"""


# Edge Cases & Gotchas
"""
# 1. Modifying a tuple element (Not allowed!)
t1 = (1,2,3,4)
t1[2] = 5
print(t1)               # TypeError


#Tuples themselves cannot be changed, but if they contain mutable objects (like lists), those can be changed.
t2 = (1, [2,3,4], [5,6])
print(t2[1][1])           # 3
t2[1][1] =  12
print(t2)                 # (1, [2, 12, 4], [5, 6])
t2[1].append(14)
print(t2)                 # (1, [2, 12, 4, 14], [5, 6])
"""


"""
✅ When to Use Tuples:
•	Return multiple values from a function
•	Store records (e.g., coordinates, database rows)
•	Use as dictionary keys (immutable requirement)
•	Improve performance where data doesn’t need to change
"""