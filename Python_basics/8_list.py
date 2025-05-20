#Example:
"""
l1 = [50,20,80,10,60,40]
print(l1)
"""


#IndexError: list assignment index out of range
"""
l1[6] =  90 
print(l1)
"""


#Modifying a List: insert() and append()
"""
l2 = [2,9,5,7,1]
l2[1] =  10 
print(l2)

l2.append(8)
print(l2)

l2 = [2, 9, 5, 7, 1]
l3 = [10, 20, 40, 50, 60]
l2.extend(l3)  # This will append all elements of l3 to l2
print(l2)      # [2, 9, 5, 7, 1, 10, 20, 40, 50, 60]

l2.insert(2,3)
print(l2)

l2.insert(100,29) #If index > last index then value will start at lastindex+1 and in this case insert will work as append.
print(l2)
print(l2[7])
"""


# Access List Elements
"""
l1 = [50, 20, 80, 10, 60, 40]
print(l1[0])       	     # 50
print(l1[1], l1[2]) 	 # 20 80
print(l1[1:4])           # [20, 80, 10]
print(l1[::-1])          # [40, 60, 10, 80, 20, 50]
"""


# Looping over the elements of the list
"""
l1 = [50, 20, 80, 10, 60, 40]
i=0
while i<len(l1):
    print(l1[i], end=" ")
    i+=1
"""


# Built-in Methods
"""
list1 = [2, 9, 5, 7, 1, 10, 60, 40, 50, 60]
print(len(list1))       # 10
print(min(list1))       # 1
print(max(list1))       # 60
print(sum(list1))       # 244
print(sorted(list1))    # [1, 2, 5, 7, 9, 10, 40, 50, 60, 60]
"""

"""
l = [1, 4.5, 4+5j]
# print(max(l))   # TypeError: '>' not supported between instances of 'complex' and 'float'
# print(sorted(l))  # TypeError: '<' not supported between instances of 'complex' and 'float'
print(len(l))     # 3
print(sum(l))     # (9.5+5j)
"""


"""
l = [3,5,6,7,8,1,9,1]
print(l.index(1))
print(l.count(1))

l = [10, 20, 30, 40]
l.reverse()             # Reverses the elements in place (modifies the original list).
print(l)                # Output: [40, 30, 20, 10]

l = [50, 10, 40, 20]
l.sort()
print(l)  # Output: [10, 20, 40, 50]

l.sort(reverse=True)
print(l)  # Output: [50, 40, 20, 10]
"""


#list() Constructor
"""
print(list(range(3)))       # [0, 1, 2]
print(list())               # []
"""

"""
l = list(1,2,3)
print(l)                    # TypeError: list expected at most 1 argument, got 3

l = list(1)
print(l)                    # TypeError: 'int' object is not iterable
"""


# Comparison Operators on Lists
"""
l1 = [1, 2, 3]
l2 = [2, 3, 1]
l3 = [1, 2, 3, 4, 5]
l4 = [1, 2, 3]

print(l1 == l2)  # False - order matters
print(l1 == l3)  # False - different elements
print(l1 == l4)  # True  - same elements in same order
print(l1>l2)     # False
"""


# Concatenation Operator
"""
l1 = [1, 5, 9]
l2 = [2, 3, 1]
l3 = l1 + l2
print(l3)  # Output: [1, 5, 9, 2, 3, 1]

# Or 

l1 += l2
print(l1)  # Output: [1, 5, 9, 2, 3, 1]
"""


# Repetition Operator
"""
asterisk symbol between two integer value will result in multiplication: 2*3 = 6, 3.4*4.5 = 15.299999999
If one is list and other is interger than this asterisk will work as Repetition Operator. [1,2]*3 = [1,2,1,2,1,2]
"""


# List of Lists (Nested Lists)
"""
l1 = [5, 4.5, True, "rks"]
print(l1)           # [5, 4.5, True, 'rks']

l2 = [5, 4.5, True, [9, 4, 7]]
print(l2)           # [5, 4.5, True, [9, 4, 7]]
print(l2[3][0])     # 9

l3 = [[1,2,3], [4,5,6], [7,8,9]]
print(l3[0])        # [1, 2, 3]
print(l3[1])        # [4, 5, 6]
print(l3[2])        # [7, 8, 9]

print(l3[0][0])     # 1
print(l3[1][0])     # 4
print(l3[2][0])     # 7

print(l3[2][3])     # IndexError: list index out of range
"""


# List Object Attributes & Methods:
"""
# help(list)          # We can get documentation about the built-in list class in Python.

# print(dir(list))

# Every class have variable and function known as attribute.
l1 = [5, 4.5, True, "rks"] # l1 is an object of list class
l1.f1()     # Here l1 object that wants to call f1 function from its list class. And by applying dot . on any list object we can only be able to call the function of that list class only. And in this case there is no f1 function available so it will through and error. And this is a type of AttributeError: which says 'list' object has no attribute 'f1'
"""


l = [3,5,6,7,8,1,9,1]
del l[1]        
# del modifies the original list. del is a statement, not a method.
print(l)        # [3, 6, 7, 8, 1, 9, 1]


# Deletes by value. Removes only the first occurrence. Raises ValueError if value not found
l.remove(1)
print(l)        # [3, 6, 7, 8, 9, 1]


# Deletes by index (default: last item). If Index is not passed delete the last elemetn. Returns the deleted item. Raises IndexError if index is invalid
l.pop()
print(l)        # [3, 6, 7, 8, 9]

print(l.pop(1)) # 6
print(l)        # [3, 7, 8, 9]
