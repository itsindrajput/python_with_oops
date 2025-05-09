"""
import My
print(My.x)
"""


#Or
"""
import My as m
print(m.x)
"""


#Or
"""
import sys
sys.path.append('C:/Users/user/Downloads/Marwadi University/M.Sc (Fintech)/05MF0203 Digital Transformation-I/Lecture Material/Notes/Code/oops_basics')
import oops
print(oops.student_1)
"""

"""
sys is a built-in module that provides access to system-specific parameters and functions used or maintained by the Python interpreter.

sys.path	A list of directories that Python searches for modules. You can append custom paths to import modules from other directories.
"""

#_________________________________________________________________________________________________________________________________________


#To print all the keywords available in Python
import keyword
print("There are total", len(keyword.kwlist), "Keywords in Python")
print(keyword.kwlist)