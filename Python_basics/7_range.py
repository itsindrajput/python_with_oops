# Indexing In Range:
r = range(10,15,1)
print(r[0], r[1], r[2],r[3], r[4])              # 10 11 12 13 14
#print(r[5])                                     # IndexError: range object index out of range


#The word Iterable comes from Iteration, which means repetition of a process.
#Example:
"""
r = range(1, 10, 2)
for i in r:
    print(i)
"""


# print(sum(range(1,11,1))) #55


#WAP to print first n natural numbers.
"""
n = int(input("Enter a number upto which you want to print natural numbers: "))
r = range(1,n+1)
for i in r:
    print(i,end=" ")
"""


#WAP to print the square of first n natural numbers.
"""
print("Enter a number upto which you want to print square: ")
n = int(input())
for i in range(1,n+1):
    print(i, "->", i**2)
"""


# Print all odd numbers from 1 to 20.
# print(list(range(1,20,2)))


# Print numbers in reverse from 10 to 1.
# print(list(range(10,0,-1)))


# Print the table of 7 using range.
"""
for i in range(7,77,7):
    print("7 X",i)
"""

#OR

"""
for i in range(1,11):
    print(f"7 X {i} = {7*i}")
"""

#OR
"""
n = int(input("Enter any number to print its table: "))
r = range(1,11)
for i in r:
    print(f"{n} X {i} = {n*i}")
"""


# Count Down Timer Example
"""
import time 
for i in range(5,0,-1):
    print(i)
    time.sleep(1)
print("Time's Up!")
"""