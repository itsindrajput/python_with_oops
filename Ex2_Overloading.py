"""
Write a Python program that demonstrates method overloading by defining a class with multiple methods having the same name but different parameters, and then invoking each method with different arguments.
"""
class Calculator:
    def add(self, a, b=None, c=None):
        if b is not None and c is not None:
            return a + b + c
        elif b is not None:
            return a + b
        else:
            return a

# Create an instance of the Calculator class
calc = Calculator()

# Invoke the add method with different arguments
print(calc.add(5))       # Output: 5
print(calc.add(5, 10))    # Output: 15
print(calc.add(5, 10, 15)) # Output: 30

class StringManipulator:
    def concatenate(self, str1, str2=None, str3=None):
        if str2 is not None and str3 is not None:
            return str1 + str2 + str3
        elif str2 is not None:
            return str1 + str2
        else:
            return str1

string_manipulator = StringManipulator()

print(string_manipulator.concatenate("Hello"))
print(string_manipulator.concatenate("Hello", " World"))
print(string_manipulator.concatenate("Hello", " World", "!"))

def overloaded_function(arg1, arg2=None, arg3=None):
    if arg2 is not None and arg3 is not None:
        print(f"Three arguments: {arg1}, {arg2}, {arg3}")
    elif arg2 is not None:
        print(f"Two arguments: {arg1}, {arg2}")
    else:
        print(f"One argument: {arg1}")

overloaded_function("test")
overloaded_function("test", "data")
overloaded_function("test", "data", "more data")