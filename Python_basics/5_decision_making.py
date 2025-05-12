"""
Indentation refers to the spaces at the beginning of a code line.
In Python ':' and 'indentation' are used to create block. Inside the same block all the statement must have the same 'indentation'

#Simple if
if condition:
    statement1
    statement2
statement_outside_if
"""

#Write a program to check whether a given number is Positive or Non Positive!
"""
number = int(input("Enter a number: "))
if number > 0:
    print("Positive")
if number <= 0:
    print("Non Positive")
"""


"""
#if else
if condition:
    statement_inside_if
    statement_inside_if
else:
    statement_inside_else
    statement_inside_else
"""

#Write a program to check whether a given number is Positive or Non Positive!
"""
number = int(input("Enter a number: "))
if number > 0:
    print("Positive Number")
else:
    print("Non Positive")
"""


"""
if elif else -> if else ladder
if condition1:
    statement1
    statement2

elif condition2:
    statement3
    statement4

elif condition3:
    statement5

else:
    statement6
"""

"""
Write a program to print grade obtained in a test. Take marks obtained form user and display the grade.
90 < marks <=100 -> A
80 < marks <=90  -> B
70 < marks <=80  -> C
60 < marks <=70  -> D
50 < marks <=60  -> E
below < 50 -> F
"""

"""
marks = int(input("Enter your marks: "))
if 90 < marks <=100:
    print("Grade -> A")

elif 80 < marks <=90:
    print("Grade -> B")

elif 70 < marks <=80:
    print("Grade -> C")

elif 60 < marks <=70:
    print("Grade -> D")

elif 50 <= marks <=60:
    print("Grade -> E")

else:
    print("Grade -> F")
"""


"""
Single line if else
code1 if conditon else code2
or
x = code1 if conditon else code2
-> if the condition is true code1 will run else code2 will run.
"""

#Write a program to check wheather a given number is even or odd.
number = int(input("Enter a number: "))
result = "Even" if number%2==0 else "Odd"
print(result)

#OR
number = int(input("Enter a number: "))
print("Even") if number%2==0 else print("Odd")

#OR
print("Even" if int(input("Enter a number: "))%2==0 else "Odd")


#There is no conditional operator (? :)  in pyhton.


# Switch statement in python. The bellow code runs only in python 3.10 or above versions
"""
def number_to_string(argument):
    match argument:
        case 0:
            return "zero"
        case 1:
            return "one"
        case 2:
            return "two"
        case default: # OR case _:
            return "something"
 
head = number_to_string(2)
print(head)
"""