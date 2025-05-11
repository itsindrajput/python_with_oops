"""
#print(7 + "7") # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(str(7) + "7") #77
print(7 + int("7")) #14
print("ABC" + "DEF") # ABCDEF
print("5" + "5") #55
"""


"""
#Important Points
•	Loss of data: float → int truncates the decimal.
•	Conversion errors: Trying to convert an invalid string raises a ValueError.
"""

"""
x = 4.5
y = int(x)
print(y) # 4

s1 = "abc"
s2 = int(s1)
print(s2) # ValueError: invalid literal for int() with base 10: 'abc'

s3 = "123"
s4 = int(s3)
print(s4)  #123


f1 = "3.142"
f2 = int(f1)
print(f2)

f3 = "3.142"
f4 = int(float(f3))
print(f4) #3

c1 = 2.143
c2 = complex(c1)
print(c2)       #2.143+0j

x = 10
print(bool(x))
"""


"""
# Implicit Type Casting
num_int, num_float = 123, 1.23
num_new = num_int + num_float
print("Value of num_new:",num_new) # 124.23
print("Data type of num_new:", type(num_new)) # <class 'float'>
"""


"""
#Explicit Type Casting
string_num = "15"
number = int(string_num)
print("Data type of string_num:", type(string_num)) #<class 'str'>
print("Value of number:",number) # 15
print("Data type of number:", type(number)) #<class 'int'>

print(number + 10) #25
"""


"""
Some Other Conversion Methods:
bin() – Converts an integer to binary (base 2)
oct() – Converts an integer to octal (base 8)
hex() – Converts an integer to hexadecimal (base 16)
ord() – Character → Unicode Code Point [Converts a single character to its corresponding Unicode integer value.]
chr() – Unicode Code Point → Character [Converts a Unicode integer back to the character it represents.]

"""

print(bin(10))  # Output: '0b1010', 0b prefix means binary

print(oct(10))  # Output: '0o12', 0o prefix means octal

print(hex(255))  # Output: '0xff'

print(ord('A'))   # Output: 65
print(ord('a'))   # Output: 97
print(ord('₹'))   # Output: 8377


print(chr(97))      #a
print(chr(122))     #z