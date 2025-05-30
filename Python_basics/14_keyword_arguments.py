#Introduction:
"""
Actual parameters are the values or variables that are passed to a function or method when it's called, 
While formal parameters are the variables defined within the function's signature to receive those values. 

Also

Argument is data being passed to a function through function call. 
Parameter is data being received by a function in function header. 
Because both belongs to same function, Arguments appear in function call statement and Parameter appears 
in function header, so we can say these terms are related.
"""


# Default Arguments:
"""
def f1(a,b):
    result = a+b
    print("Sum =",result)                # 8
f1(3,5)         
#f1(3,5,8)                               # TypeError: f1() takes 2 positional arguments but 3 were given


def f2(a,b,c):
    result = a+b+c
    print("Sum =",result)                # 15       
f2(3,5,7)                 
#f2(3,5)                                 # TypeError: f2() missing 1 required positional argument: 'c'


def f3(a,b,c=0):
    result = a+b+c
    print("Sum =",result)                # 28      
f3(13,15)   
"""

"""
def f4(a,b=0,c):                         # Non default arguments (i.e. 'c') can't come after default arguments (i.e. 'b')
    result = a+b+c
    print("Sum =",result)                # 28      
f4(13,15)                                # SyntaxError: parameter without a default follows parameter with a default
"""

"""
➤ Default Arguments:
Default value indicate that the function argument will take that valve if no argument value is passed during the function call. 

◉ The default value is assigned by using the assignment (=) Operator.   

💡 We Cannot have non default arguments after default argument.
"""

"""
def f5(a=0,b=0,c=0):			# Default Arguments:
    result = a+b+c
    print("Sum =",result)                
f5()					        # 0
f5(5)					        # 5
f5(6,7)					        # 13
f5(9,8,4)  				        # 21
"""


# Adding Students to a List (Safely)
"""
def add_student(name, student_list=None):
    if student_list is None:
        student_list = []           # Create a new list if one isn’t passed
    student_list.append(name)
    return student_list

students_group_1 = add_student("Alice")
print("Group 1:", students_group_1)  # ➤ ['Alice']

custom_list = ["Eve"]
updated_list = add_student("Charlie", custom_list)
print("Custom List:", updated_list)  # ➤ ['Eve', 'Charlie']
"""


# Positional Vs Keyword Arguments:
"""
❖ Positional arguments are those passed to a function based on their order or position in the function call. The function assigns these arguments to the corresponding parameters in the function definition, according to their order.
"""
"""
def f1(a,b):
    print("a =",a,"b =",b)
f1(2,3)                         # a = 2 b = 3
f1(3,2)                         # a = 3 b = 2
"""


"""Keyword-only arguments mean whenever we pass the arguments(or value) by their parameter names at the time of calling the function in Python in which if you change the position of arguments then there will be no change in the output.
"""
"""
def f1(a,b):
    print("a =",a,"b =",b)
f1(b=2,a=3)                     # a = 3 b = 2


# After Positional Argument Keyword Arguments can come untill multiple values are not going to a single variable.
def f1(a,b):
    print("a =",a,"b =",b)
f1(2,b=3)                       # a = 2 b = 3


def f1(a,b):
    print("a =",a,"b =",b)
#f1(2,a=3)                       # TypeError: f1() got multiple values for argument 'a'


# We cann't have positional arguments after keyword Arguments.
def f1(a,b):
    print("a =",a,"b =",b)
#f1(a=2,3)                        # SyntaxError: positional argument follows keyword argument
"""
