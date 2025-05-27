# Examples of prior knowledge: 
"""
range, list, str, tuple --> The common thing in all this methods are: 1. indexing (Due to this we can perform slicing operation) 2. iterables 3. Sequence 4. Built-in data types
"""


# Introduction:
"""
💡Different from other iterable present in python.

➤ A set is a class and a built-in data type in python.
✦ Sets are mutable, meaning elements can be added or removed, but the elements themselves must be immutable. 

❖ A set in Python is an unordered collection of unique elements. (Set is not a sequence, we never know the order in which the elements are stored inside the set.)
✦︎ Set does not guarantee to store values in the order of insertion. 


◉ Indexing is not applicable to set objects so, slicing operator is not applicable. 
✦︎ Set is iterable.

→ Sets are defined using curly braces {} or the set() constructor. 
"""


# Creating Set Object:
"""
s1 = {10,9,8}
print(type(s1))                     # <class 'set'>

print(s1)                           # {8, 9, 10}
# ❌ Python sets do not automatically sort elements. ✅ The order you see is based on internal hash mechanisms, not sorting.

s2 = {9,8,9,7,6,8,1}
print(s2)                           # {1, 6, 7, 8, 9}

# Empty Set:
s3 = {}
print(type(s3))                     # <class 'dict'>

s4 = set()
print(type(s4))                     # <class 'set'>


#s5 = set(10,20,30)
#print(type(s5))                    # TypeError: set expected at most 1 argument, got 3

#print(set(10))                     # TypeError: 'int' object is not iterable

print(set("fintech"))               # {'f', 'i', 'h', 'c', 't', 'n', 'e'}
"""


# Write a Python Script to remove duplicate elements from a list.
"""
l1 = [20,10,50,20,30,50,20,10]
result = list(set(l1))
print(result)                       # [10, 20, 50, 30]
"""

# OR

"""
print(list(set([int(i) for i in input("Enter List of Duplicate numbers: ").split(',')])))
"""


# Accessing Set Elements:
"""
s1 = {10,9,8}
for i in s1:
    print(i)               # 8 9 10 
    
l1 = list(s1)
print(l1[0])               # 8
"""


# Built-in methods in set:
"""
s2 = {3,1,9,2,5,7}         # {1, 2, 3, 5, 7, 9} <class 'set'>
print(s2, type(s2))

print(len(s2))             # 6
print(min(s2))             # 1
print(max(s2))             # 9
print(sum(s2))             # 27
print(sorted(s2))          # [1, 2, 3, 5, 7, 9]
"""


# Concatenation and Repetition Operator:
"""
# set + set    -->   Not Supported
s1 = {1,2,3}
s2 = {9,8,7}
print(s1+s2)               # TypeError: unsupported operand type(s) for +: 'set' and 'set'

# set + int    -->   Not Supported
print(s1*2) 
TypeError:                 # unsupported operand type(s) for *: 'set' and 'int
"""


# Comparison Operator: When comparing sets using relational operators like <, <=, >, >=, ==, !=, the comparison is based on subset and superset relationships, not on element values.
""" 
s1 = {1,2,3}
s2 = {9,8,7}
s3 = {3,1,2}
s4 = {9,8,7,6,1,3,2}

print(s2>s1)                # False, They have no common elements, so s1 is not a subset of s2.
print(s1<s4)                # True

print(s1==s2)               # False
print(s1==s3)               # True
# Two set objects are equal if their elements are same, doesn't matter the order of elements.
"""


# Set Object Methods: add(), update(), discard(), remove(), union(), intersection(), clear(), issubset(), issuperset(), pop()
"""
set1 = {11,22}
set1.add(33)
print(set1)                   # {33, 11, 22}

#set1.add(44,55)              # TypeError: set.add() takes exactly one argument (2 given)  

set1.add("Forty-four")         
print(set1)                    # {33, 11, 22, 'Forty-four'}

set1.add((44,55,66))
print(set1)                    # {33, 11, (44, 55, 66), 22, 'Forty-four'}
"""


"""
_______________________________________________________________________________________________________________________________________
add() --> It add iterable or non-iterable object in the set.
update() --> Here we can only pass iterable as an argument. And that iterable object element will become the member of set, along with other set elements.
_______________________________________________________________________________________________________________________________________
"""


"""
set1 = {11,22}
set1.update((33,44,55))
print(set1)                    # {33, 11, 44, 22, 55}
"""


"""
s4 = {9,8,7,6,1,3,2}
s4.remove(9)
print(s4)                      # {1, 2, 3, 6, 7, 8}

s4.discard(8)
print(s4)                      # {1, 2, 3, 6, 7}
"""

"""
s4 = {9,8,7,6,1,3,2}
#s4.remove(10)                   # KeyError: 10
s4.discard(11)                   # Throws No error
print(s4)                        # {1, 2, 3, 6, 7, 8, 9}
"""

"""
s4 = {9,8,7,6,1,3,2}
print(s4.pop())                   # 1, returns the value which will be poped out.
print(s4.pop())                   # 2
print(s4)                         # {3, 6, 7, 8, 9}
"""

"""
s4 = {9,8,7,6,1,3,2}
s4.clear()
print(s4)                         # set(), empty set
"""

"""
s1 = {8,1,5,4,9}
s2 = {10,8,2,9,2}
print(s1.intersection(s2))        # {8, 9}
print(s1.union(s2))               # {1, 2, 4, 5, 8, 9, 10}
"""

"""
s1 = {8,1,9}
s2 = {10,8,2,9,1}
print(s1.issubset(s2))             # True
print(s2.issuperset(s1))           # True
"""


# Set comprehension: s1 = {expression for e in object}
# Example 1: 
"""
numbers = [1, 2, 2, 3, 4, 4, 5]
square = {i**2 for i in numbers}
print(square)                  # {1, 4, 9, 16, 25}
"""

# Example 2:
"""
s = input("Enter a senternce to see how many vowels are there in that: ")
s1 = set()
for i in s:
    if i in "aeiouAEIOU":
        s1.add(i)
print(s1)
"""

# OR

#print({i for i in input("Enter a string: ") if i in "aeiouAEIOU"})