# 1. Write a Python script to display the first 10 odd natural numbers.
"""
i = 1
while i<20:
    print(i,end=" ")
    i+=2
"""

#OR

"""
for i in range(1,11):
    print(2*i-1, end=" ")
"""

# OR

"""
n = int(input("How many odd natural numbers do you want to print? "))
i = 1
count = 0
while (count < n):
    print(i, end=" ")
    i+=2
    count+=1
"""


# 2. Write a Python script that takes a number N as input and prints the first N even natural numbers.
"""
N = int(input("Enter a number upto which you want to print even natural numbers: "))
i = 2
count = 0
while count<N:
    print(i, end=" ")
    i+=2
    count+=1
"""


# 3. Write a Python script to print the first 10 odd natural numbers in reverse order.
"""
i = 19
while i>0:
    print(i, end=" ")
    i-=2
"""

# OR

"""
N = int(input("Enter how many odd natural number you want to print in reverse order: "))
i = 2*N-1
while i>0:
    print(i, end=" ")
    i-=2
"""


# 4. Write a Python script to print the squares of the first N natural numbers.
"""
n = int(input("Enter a number upto which you want to print the squares: "))
i=1
while i<=n:
    print(i, "->", i*i)
    i+=1
"""


# 5. Write a Python script to calculate and display the sum of the first N natural numbers.
"""
n = int(input("Enter a number up to which you want to calculate the sum: "))
i = 1
sum = 0
while i<=n:
    sum += i
    i+=1
print(sum)
"""

# OR

"""
n = int(input("Enter a number up to which you want to calculate the sum: "))
print("Sum =", n * (n + 1) // 2)
"""


# 6. Write a Python script to compute the factorial of a given number.
"""
n = int(input("Enter a number of which you want to calculate the factorial: "))
i = 1
fact = 1
while i<=n:
    fact *= i
    i+=1
print(fact)
"""

# OR

"""
n = int(input("Enter a non-negative number: "))
fact = 1
for i in range(1, n+1):
    fact *=i
print(fact)
"""


# 7. Write a Python script to count the number of digits in a given integer.
"""
integer = int(input("Enter an integer to count the number of digits: "))
count = 0
while integer > 0:
    count +=1
    integer = integer // 10
print(count)
"""

# OR

"""
n = int(input("Enter a number to count the digits present: "))
if n == 0:
    count = 1
else:
    n = abs(n)      # Using abs -> absolute value to support negative numbers
    count = 0
    while n>0:
        count +=1
        n = n//10
    print("Number of Digits = ", count)
"""


# 8. Write a Python script to determine whether a given number is a prime number or not.
"""
n = int(input("Enter a number to check whether it's prime or not: "))
if n<=1:
    print(n, "is not a prime number!")
else: 
    i = 2
    result = True
    while i<n:
        if (n%i == 0):
            print(n, "is not a prime number!") 
            result = False
            break
        i+=1
    if result:
        print(n, "is a prime number!") 
    else:
        print(n, "is not a prime number!") 
"""


# Write a Python script to check whether the entered string is a palindrome or not.
"""
string1 = input("Enter a string to check whether it is a palindrome or not: ")
string2 = string1[::-1]
if string1 == string2:
    print("The string is a palindrome!")
else:
    print("The string is not a palindrome.")
"""


# 10. Write a Python script to compute the Least Common Multiple (LCM) of two given numbers.
"""
print("Enter Two Numbers")
a = int(input())
b = int(input())
l = a if (a>b) else b
while l<=a*b:
    if (l%a==0 and l%b==0):
        print("LCM =",l)
        break
    l+=1
"""

# OR

"""
print("Enter Two Numbers:")
a = int(input())
b = int(input())

if a == 0 or b == 0:
    print("LCM is not defined when one of the numbers is 0.")
else:
    a, b = abs(a), abs(b)  # LCM should be positive
    l = max(a, b)
    while True:
        if (l % a == 0 and l % b == 0):
            print("LCM =", l)
            break
        l += 1
"""


"""
Finding the LCM of 4 and 6
To find the Least Common Multiple (LCM) of 4 and 6, we list the multiples of each number:

Multiples of 4: 4, 8, 12, 16, 20, 24, ...

Multiples of 6: 6, 12, 18, 24, 30, 36, ...

Now, identify the common multiples:
12, 24, ...

The smallest common multiple is 12,
so the LCM of 4 and 6 is 12.

✅ Important Insight:
If two numbers are given, say 4 and 6, their LCM:

Cannot be smaller than the larger number (in this case, 6)

Cannot be greater than the product of both numbers (4 × 6 = 24)
So, the LCM will always lie between 6 and 24.
"""