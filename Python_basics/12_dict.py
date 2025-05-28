# Introduction:
"""
➤ In Python, a dictionary, or dict, is a built-in data type that stores data in key-value pairs. 

✦ Dictionaries are mutable, ordered (since Python 3.7), and do not allow duplicate keys.

❖ Dictionaries are iterable. And Dictionaries are not in a sequence (means elements should store in a systemic order i.e indexing concept).

◉ Indexing is not applicable to dict object. So we cann't perform slicing operation as well.

→ Keys must be immutable types, such as strings, numbers, or tuples, while values can be of any data type. 

💡Dictionaries are created using curly braces {} or the dict() constructor.
"""


#Set vs Dict in python:
"""
s1 = {10,20,30}            # The Elements present inside this set is called as keys and they cann't be duplicate.
print(type(s1))            # <class 'set'>

d1 ={
    1: "Rahul",            # Element 1, where 1 is key and Rahul is value. Key must be unique.
    2: "Aman",             # Element 2
    3: "Tarun",            # Element 3
    4: "Vinit"             # Element 4
    }
print(type(d1))            # <class 'dict'>
"""


# How to create Dictionary/dict object ?
"""
d1 = {101: "Delhi", 102: "Mumbai", 103: "Agra", 104: "Rajkot"}
print(d1)

d2 = {}                    # Empty Dictionaries
print(type(d2))            # <class 'dict'>

d3 = dict()                # Empty Dictionaries
print(type(d3))            # <class 'dict'>

d4 = dict(a="Ram",b="Sita")
print(d4)                  # {'a': 'Ram', 'b': 'Sita'}

#d5 = dict(1="Ram",2="Lakhan")
#print(d5)                  # SyntaxError

employees = {701: "Amit Sharma", 701: "Amit Sharma", 701: "Amit Sharma", 701: "Amit Sharma"}
print(employees)            # {701: 'Amit Sharma'}
"""


# How to access Dictionary/dict object? 

products = {401: "Laptop", 402: "Smartphone", 403: "Headphones", 404: "Smartwatch"}

print(products)                 # 1st Option

print(products[402])            # Smartphone        #2nd Option
print(products[404])            # Smartwatch

for K in products:              # 3rd Option
    print(K, products[K])


# How to edit dict element?
"""
Editing dictionary element means we want to change data-value of the element with NewDataValue and not the key-value.

dictObject[key-value] = NewDataValue
              ⬇️
          ↙️     ↘️
Key exist?       Doesn't exist, then with that key a new element will be create and NewDataValue will be assigned inside the dict.
If Yes, Good, data-value to that specifice key will change with NewDataValue.
"""

"""
courses = {601: "Data Structures", 602: "Web Development", 603: "Machine Learning", 604: "Cyber Security"}

courses[601] = "Data Science"
print(courses)              # {601: 'Data Science', 602: 'Web Development', 603: 'Machine Learning', 604: 'Cyber Security'}

courses[605] = "Operating System"
print(courses)              # {601: 'Data Science', 602: 'Web Development', 603: 'Machine Learning', 604: 'Cyber Security', 605: 'Operating System'}

del courses[603]
print(courses)              # {601: 'Data Science', 602: 'Web Development', 604: 'Cyber Security', 605: 'Operating System'}
"""


# How to add new element in the dictionary?: dictObject[new-key] = data-value
"""
employees = {701: "Amit Sharma", 702: "Riya Verma", 703: "Nikhil Rao", 704: "Sneha Das"}
employees[705] = "Rishabh Singh"
print(employees)
"""


# Methods present in dictionary are: 
"""
items()  -> Collection of dict elements, 
keys() -->  Collection of keys only of the elements,
values()  -->  Collection of data-values only of the dict elements.
All these methods are dict class attributes.
"""

"""
days = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday"}

print(days.items())
# dict_items([(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday')])

for i in days.items():
    print(i)
"""
"""
Output:
(1, 'Monday')
(2, 'Tuesday')
(3, 'Wednesday')
(4, 'Thursday')
(5, 'Friday')
"""
"""
for i in days.items():
    print(i[0],i[1])                # Accessing key and value separately:
"""
"""
1 Monday
2 Tuesday
3 Wednesday
4 Thursday
5 Friday
"""
"""
for i in days.items():
    key,value = i
    print(key,value)

for key, value in days.items():
    print(key, value) 
"""

"""
days = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday"}

print(days.keys())              
# dict_keys([1, 2, 3, 4, 5])

print(days.values())
# dict_values(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']) 
"""


#Built-in methods: len(), min(), max(), sum(), sorted()
"""
items = {1: "Milk", 2: "Bread", 3: "Eggs", 4: "Butter"}
print(len(items))                    # 4, Returns the number of key-value pairs in the dictionary.
print(min(items))                    # 1, Returns the smallest key (because these functions operate on the keys by default).
print(max(items))                    # 4, Returns the largest key.
print(sum(items))                    # 10, Adds up all the keys.
print(sorted(items))                 # [1, 2, 3, 4], Returns a sorted list of the keys.


#💡 If you want to operate on values instead:
print(len(items.values()))           # 4
print(sorted(items.values()))        # ['Bread', 'Butter', 'Eggs', 'Milk']
"""


# Concatenation (+) and Repetition (*) — Not Allowed Directly on Dicts ❌ 
"""
a = {1: 'a'}
b = {2: 'b'}
print(a + b)                          # ❌ TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
print(a * 2)                          # ❌ TypeError: unsupported operand type(s) for *: 'dict' and 'int'
"""

# Python 3.9 introduced the | (pipe) operator to merge dictionaries (similar to concatenation):
"""
a = {1: 'a'}
b = {2: 'b'}
c = a | b
print(c)                                # Output: {1: 'a', 2: 'b'}
"""


# Comparison operators: 
"""
❖ Only == and != can be used with dictionaries.  Other Comparison Operators (<, >, <=, >=) Not Supported.

◉ Dictionaries are equal only if both the keys and the values are the same, regardless of insertion order.
"""

# Example:
"""
a = {1: 'apple', 2: 'banana'}
b = {2: 'banana', 1: 'apple'}
c = {1: 'apple', 2: 'orange'}

print(a == b)                         # ✅ True (both key-value pairs match)    
print(a != c)                         # ✅ True (value for key 2 differs)
"""


# Dict object methods: pop(key), popitem(), clear()
"""
items = {1: "Milk", 2: "Bread", 3: "Eggs", 4: "Butter"}
print(items.pop(1))
print(items)                          # {2: 'Bread', 3: 'Eggs', 4: 'Butter'}

print(items.popitem())                # (4, 'Butter')

items.clear()
print(items)                          # {}
"""


# Dict Comprehension: Syntax: d1 = {key-expression:data-expression for k in seq}
print({k:k**2 for k in range(1,8,1)})