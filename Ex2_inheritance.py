"""
Write a Python program that defines a class representing a student. Include attributes such as name, age, and 
grade. Instantiate student objects and display their information.
"""
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

# Creating student objects
student1 = Student("Alice", 20, "A")
student2 = Student("Bob", 22, "B")
student3 = Student("Charlie", 21, "A+")

# Displaying student information
student1.display_info()
student2.display_info()
student3.display_info()


