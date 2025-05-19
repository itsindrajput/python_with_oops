# Practice Question:
# 1️. Write a Python script to calculate the area of a rectangle.
# Hint: Use the formula Area = length × breadth. Take length and breadth as input from the user.
"""
length = float(input("Enter The Length of the Rectangle: "))
breadth = float(input("Enter The Breadth of the Rectangle: "))
print("Area of Rectangle",length*breadth)
#OR
#print("Area of Rectangle = {:.2f}".format(length*breadth))
#OR
#print(f"Area of Rectangle = {length*breadth:.2f}")
"""

"""
length = float(input("Enter The Length of the Rectangle: "))
breadth = float(input("Enter The Breadth of the Rectangle: "))
area = length * breadth
print("Area of Rectangle", area)
print("Area of Rectangle = {:.2f}".format(area))
print(f"Area of Rectangle = {area:.2f}")
"""


# 2️. Write a Python script to calculate simple interest.
# Hint: Use the formula SI = (Principal × Rate × Time) / 100. Take all values as input from the user.
"""
principal = float(input("Enter the Principal: "))
rate = float(input("Enter the Rate: "))
time = float(input("Enter the Time: "))
si = principal*rate*time/100
print(f"Simple Intrest = {si:.2f}")
"""


# 3️. Write a Python script to remove the last digit from a given number.
# Hint: Use integer division //10 to remove the last digit.
"""
number = int(input("Enter a number: "))
last_digit = number % 10
rem = number // 10
print("Removed last digit = ", last_digit)
print("Remaining number = ", rem)
"""


# 4️. Write a Python script to swap the values of two variables.
# Hint: Use a third variable or Python’s swapping feature.
"""
a, b = int(input("Enter 1st Number: ")), int(input("Enter 2nd Number: "))
temp = a 
a = b 
b = temp 
print(f"After Swap \n1st Number: {a} \n2nd Number: {b}")
"""


# 5️. Write a Python script to check whether a given number is divisible by 5 or not.
# Hint: Use the modulus operator % to check if the remainder is 0.
"""
int(input("Enter a number: "))%5==0) else print("Not Divisible By 5")
"""


# 6️. Write a Python script to print two given words in dictionary (alphabetical) order.
"""
Hint: Use if...else to compare the words and print accordingly.
lower() is used to make the comparison case-insensitive (so "Apple" and "banana" are compared fairly).
Alphabetical order means: "apple" comes before "banana".
"""

"""
str1 = input("Enter 1st Word: ")
str2 = input("Enter 2nd Word: ")
if (str1.lower() < str2.lower()):
    print(f"Words in dictionary order: {str1}, {str2}")
else:
    print(f"Words in dictionary order: {str2}, {str1}")
"""


# 7️. Write a Python script to check whether a given number is a three-digit number or not.
# Hint: A number is three-digit if it is between 100 and 999 (both inclusive).
"""
n = int(input("Enter a number to check whether it is a three-digit number or not: "))
if 100 <= abs(n) <= 999:
    print("It is a 3-digit number")
else:
    print("It is not a 3-digit number")
"""


# 8️. Write a Python script to check whether a given year is a leap year or not.
# Hint: A year is a leap year if it's divisible by 4 but not by 100, unless it's also divisible by 400.
"""
n = int(input("Enter a year to check if it is a leap year or not: "))
if (n%4 == 0):
    if (n%400 == 0):
        print("It is a leap year!")
    elif (n%100 == 0):
        print("It is not a leap year!")
    else:
        print("It is a leap year!")    
"""


# 9️ Write a Python script to check whether a given number is positive, negative, or zero.
# Hint: Use if, elif, and else to check the sign of the number.
"""
n = int(input("Enter a number to check whether a given number is positive, negative, or zero: "))
if (n>0):
    print("Positive")
elif (n<0):
    print("Negative")
else:
    print("Zero")
"""


# 10. Write a Python script to take a complex number as input and display whether the real part or the imaginary part is greater.
# Hint: Use complex() to accept input and compare real and imag attributes.
"""
complex_number = complex(input("Enter a complex number: "))
r = complex_number.real
i = complex_number.imag

if (r>i):
    print(r,">",i, "Real Part Is Greater!")
elif (r<i):
    print(r,"<",i,"Imaginary Part Is Greater!")
else:
    print(r,"=",i, "Real and Imaginary Parts Are Equal!")
"""