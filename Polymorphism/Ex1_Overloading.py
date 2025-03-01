"""
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __gt__(self,other):
        return self.marks > other.marks

    def __lt__(self,other):
        return self.marks < other.marks
    
s1 = Student("Aman", 200)
s2 = Student("Rishabh", 250)    
print(s1>s2)
print(s1<s2)
"""





class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __mul__(self,other):
        return self.salary * other.days

class EntryRegiser:
    def __init__(self, name, days):
        self.name = name
        self.days = days
    

e1 = Employee("Rishabh", 25, 1000)
er = EntryRegiser("Aryan", 28)

print("The Monthly salray = ",e1*er)