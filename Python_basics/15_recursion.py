# Introduction:
"""
Function calling itself is called recursion.
Recursion involves a function calling itself directly or indirectly to solve a problem by breaking it down into simpler and more manageable parts. 


Recursion is widely used for tasks that can be divided into identical subtasks.

Recursive function is defined like any other function, but it includes a call to itself. The syntax and structure of a recursive function follow the typical function definition, with the addition of one or more conditions that lead to the function calling itself.


Example:
def f1():
    print("Hi")
    f1()            # Recursive Case
    print("Bye")    # No Base Case -> Infinite Loop
f1()
"""


# Basic Example of Recursion: Sum of natural numbers from 1 to n.
"""
def f1(n):
    if n==1:
        return 1
    s = n + f1(n-1)
    return s
x = f1(4)
print(x)             # 10
"""


# Factorial using recursion:
"""
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
"""


"""
In recursion, problem is solved in terms of problem itself.

Each time recursive function call to itself for little simpler version of the original problem.
i.e.
     ↗ n + f1(n-1)      n>1    (Recursive Case)
f(n)=↘ 1                n==1    (Base Case)

Ex: f1(100) = 100 + f1(99)
    f1(n) = n + f1(n-1)
"""


# How to approach recursive function?
"""
Total there will be 3 steps:
    Step 1: Suppose the function is allready built, that we want to make.
            def sum(n):     # What it will do is to add the numbers upto n i.e. 1+2+3+...+n
                
    Step 2: Recursive case: Means we have to call to the function that we have assumed but for the little simpler version of problem.
            sum(n-1)        # 1+2+3+...+n-1 -> Now this will be solution for the above problem in step 1.
            n + sum(n-1)    # And if we will add the above result then we will get to solution.
            
    Step 3: Base case: In what case we didn't want to run the step 2.
            when n == 1 because in that case we can't divide furter. And the sume of 1 is 1.
        
Now, how to write steps in this order: 1, 3, 2
"""


# Write a recursive function to calculate the sum of square of first n natural numbers.
"""
def sum_of_sq(n):                   # Step1: 1^2 + 2^2 + 3^2 + ... + n^2
   if n == 1:                       # Step 3
    return 1
   sum = n**2 + sum_of_sq(n-1)      # Step2: 1^2 + 2^2 + 3^2 + ... + n-1^2
   return sum
result = sum_of_sq(4)
print(result)
"""