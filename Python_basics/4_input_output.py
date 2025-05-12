"""
#Program to add two numbers

print("Enter Two Numbers!")
a = input()
b = input()
print("Sum = ", a+b) #concatenate the value in a and b

print("Enter Two Numbers!")
a = int(input())
b = int(input())
print("Sum = ", a+b) #add the value in a and b

# OR

print("Enter Two Number")
a, b = int(input("Enter 1st Number: ")), int(input("Enter 2nd Number: "))
print("Sum = ", a+b)
"""


#Formatted Output
"""
Parameter	Description
sep:	Specifies the string to use as a separator between the objects being printed. The default value is ' '.
end:	It specifies the string to use as a terminator after the objects are printed. The default value is '\n'.
The end parameter allows you to specify a string that will be printed after the output of the print() function. 
"""

print("Namaste1", "India")

print("Namaste2", "India", sep=" ")
print("Namaste3", "India", sep=" Inacademic ")

print("Namaste4", "India", end="\n\n")
print("Namaste5", "India", end=" Inacademic")

print() 

n = int(input("Enter a number upto which you want to print Natural number: "))
i=1
while (i<=n):
    print(i)
    i = i+1

n = int(input("Enter a number upto which you want to print Natural number: "))
i=1
while (i<=n):
    print(i, end=" ")
    i = i+1