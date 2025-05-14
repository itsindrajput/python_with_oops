"""
#Loops in Python are control flow structures that allow code to be executed repeatedly. 
Python supports two main types of loops: for loops and while loops. 

Python does not have a built-in do-while loop like some other programming languages.
"""

# The functionality of a do-while loop can be emulated using a while loop with a break statement
"""
while True:
    number = int(input("Enter a number between 1 and 10: "))
    try:
        if (1 <= number <= 10):
            print("Valid number entered:", number)
            break  # Exit the loop if the number is valid
        else:
            print("Number is out of range. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")
"""


#---------------------------------------------------------------------------------------------------------------------


"""
While Loops: A while loop executes a block of code as long as a condition is true. 
Syntax:
while condition:
    statement1
    statement2
statement3 # Statement outside while block
"""

#Write a program to print "Python3" five times on the screen.
"""
n = 1
while n<=5:
    print("Pyhton3")
    n += 1
"""

#WAP to print first N natural number.
"""
n = int(input("Enter a number upto which you want to print Natural number: "))
i=1
while (i<=n):
    print(i,end=" ")
    i = i+1
"""

##WAP to calculate the sum of first N natural number.
"""
number = int(input("Enter a number upto which you want to calculate the sum, of Natural Number: "))
i = 1
sum = 0
while (i<=number):
    sum += i
    i+=1
print("Sum = ", sum)
"""


#-----------------------------------------------------------------------------------------------------------------


# Jump statements
"""
Jump statements in Python are control flow tools that alter the sequential execution of code. They transfer control to another part of the program. Python has three main jump statements: break, continue, and return.

1. break: This statement terminates the loop or switch statement and transfers execution to the statement immediately following the loop or switch.

2. continue: It skips the rest of the code inside the current loop iteration and moves to the next iteration of the loop.
3. return: This statement exits the current function and optionally returns a value to the caller.
"""

#WAP to check whether a given number is prime or not.
"""
n = int(input("Enter a number to check whether it is Prime or Not: "))
i=2
while i < n:
    if (n%i == 0):
        break
    i+=1
if (i==n):
    print(n, "Is a Prime Number")
else:
    print(n, "Is Not a Prime Number")
"""


#OR


"""
n = int(input("Enter a number to check whether it is Prime or Not: "))
i=2
while i<n-1:
    if(n%2==0):
        print(n, "Is Not a Prime Number")
        break
    i+=1
else:
    print(n, "Is a Prime Number")
"""


#OR


"""
number = int(input("Enter a number check whether it is Prime or Not! "))
if (number <=1):
    print(number, "Is not a Prime Number")
else:
    i = 2
    count = 0
    while (i < number):
        if (number%i == 0):
            count +=1
        i+=1
    if (count > 0):
        print(number, "Is not a Prime Number")
    else:
        print(number, "Is a Prime Number")
"""


#-----------------------------------------------------------------------------------------------------------------


#For Loops
"""
A for loop iterates over a sequence (like a list, tuple, string, or range) or other iterable object. 

for iterates n times, where n is number of elements in a sequence.

while loop is used to conditionally repeat a block of code.

Syntax:
for variable in iterable-sequence:
    statement1
    statement2
"""

#WAP to print unicode of each character of the string "Rajput".
#ord() – Converts a single character to its corresponding Unicode integer value.

"""
str = "Rajput"
for x in str:
    print(x, "->", ord(x))
"""


#The range() Function
for i in range(0,10,2):
    print(i, end=" ")