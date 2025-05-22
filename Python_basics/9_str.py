# String (str) In Python is a class which is immutable, iterable, hashable, and is sequence (order of characters matters).
"""
s1 = 'technology'
print(s1)
print(type(s1))                 #<class 'str'>

# String is hashable and list in not.
print(hash(s1))                 # -543583308860834285
print(hash(list(range(4))))     #TypeError: unhashable type: 'list'
"""


# How to create str object?
# str1 = "heyhello"
# str2 = 'heyhello'
# str3 = """heyhello"""
# str4 = '''heyhello'''
# print(str1,str2,str3,str4)

# str5 = str()
# str6 = str(123)
# str7 = str(3.142)
# print(str5, str6, str7)

# str8 = str([1,2,3])
# print(str8)


#Indexing
"""
string1 = "rishabh"
print(string1[0], string1[6])
print(string1[-1], string1[-7])
"""


#Accessing str elements
"""
1. str1[index]
    str1 = "Hello"
    print(str1[0])                  # H
    
2. print(str2)
    str2 = 'technology'
    print(str2)

3. for loop
    str3 = "Friendly"
    for i in str3:
      print(i)
    
4. slicing operator
"""


# Built-in Method len(), min(), max(), sorted(), sum()
"""
str1 = 'mindful'
print(len(str1))        # 7
print(min(str1))        # d
print(max(str1))        # u
print(sorted(str1))     # ['d', 'f', 'i', 'l', 'm', 'n', 'u']
print(str1)             # mindful
#print(sum(str1))       # TypeError: unsupported operand type(s) for +: 'int' and 'str'
"""


# Concatenation and Repetition Operator:
""""
  ---> If both the operand before and after the + operator are integer the sum will take place. Ex: 2+4=6, 3.4+5.1=8.5
+
  ---> If both the operand before and after the + operator are list, str or other iterable than concatenation will take place.
  Ex: "abc"+"de" = "abcde"
  
  * ---> And if we multiply any iterable with int type value then Repetition will take place. Ex: "ab"*3 = "ababab"
  """


# Comparison Operator (<, <=, >, >= Inequality Operator) (==,!= Equality Operator)
"""
print("Patna"<"Bhopal")         #False

str1 = "Loyal"
str2 = "Loyality"       
print(str1<str2)                #True as str2 comes after str1 in dictionary order

# In alphabetical order what comes first is smaller. And in ASCII, uppercase letters A through Z are represented by decimal values 65 through 90, and lowercase letters a through z are represented by decimal values 97 through 122. For example, "A" is 65, "B" is 66, "a" is 97, and "b" is 98. 
"""


# Common String Methods: All string methods return a new string — they do not modify the original string because strings in Python are immutable. help(str.index )
"""
s = "Just looking like a wow."
print(len(s))                 # 24
print(s.index('o'))           # 6
print(s.index('like'))        # 13

print(s.upper())            # JUST LOOKING LIKE A WOW.
print(s)                    # Just looking like a wow.
print(s.isupper())          # False

print(s.lower())            # just looking like a wow.
print(s.islower())          # False
print(s.capitalize())       # Just looking like a wow.
#print(s.iscapitalize())    # AttributeError: 'str' object has no attribute 'iscapitalize'.
print(s.title())            # Just Looking Like A Wow.
"""

# strip() removes characters from both the beginning and the end. It does not affect characters in the middle of the string. To only remove from one end: Use lstrip() (left side), Use rstrip() (right side)

"""
text = "   Hello World   "
print(text.strip())         # Hello World

data = "###Python###"
print(data.strip('#'))      # Python

url = "/user/profile/"
print(url.strip("/er"))     # user/profil
"""

"""
text = "Hello World"
print(text.replace("World","Python"))       # Hello Python
print(text.replace("l","q"))                # Heqqo Worqd
print(text.startswith('He'))                # True
print(text.endswith('ld'))                  # True
print(text.find('W'))                       # 6
print(text.count("l"))                      # 3
print(text.count(" "))                      # 1 count number of words in a string based on the space.

sen1 = "abc"
print(sen1.isalpha())                        # True

sen2 = "abc def"
print(sen2.isalpha())                        # False

sen3 = "123"
print(sen3.isdigit())                         # True

sen4 = "abc123"
print(sen4.isalnum())                         # True
"""


# String Formatting
"""
name, age = "Rishabh", 25
print("My name is %s and I am %d years old." %(name, age)) # My name is Rishabh and I am 25 years old.

print("My name is {} and I am {} years old.".format(name,age)) # My name is Rishabh and I am 25 years old.

print(f"My name is {name} and I am {age} years old.") # My name is Rishabh and I am 25 years old.

print("I'm {1} years old. My Name is {0}.".format(name,age))
"""


# split() — Converts string to list
"""
s = "Python is awesome"
words = s.split()
print(words)                # ['Python', 'is', 'awesome']

print(s.split(" "))         # ['Python', 'is', 'awesome']

# join() — Converts list to string
str1 = "-"
joined = str1.join(words)
print(joined)               # Python-is-awesome
"""


# Example:
"""
string = input("Enter some number seperated by commas: ")
res = string.split(",")
print(res)                         # ['1', '2', '3', '4', '5']
result = [int(i) for i in res]
print(result)                      # [1, 2, 3, 4, 5]
"""

#OR

# print([int(i) for i in input("Enter some number seperated by commas: ").split(",")])


# Slicing Operator:
"""
s = "rishabh"

# Syntax: s[start:stop:step]
print(s[0:4])             # rish
print(s[:4])              # rish
print(s[::2])             # rsah
print(s[::-1])            # hbahsir (reversed string)
"""