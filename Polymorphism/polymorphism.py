#Polymorphism Example:
"""
class Cat:
    def talk(self):
        print("Mew....Mew...!")

class Dog:
    def talk(self):
        print("Bhow...Bhow....!")

class Goat:
    def talk(self):
        print("Meahh....Meahh..!")

class Duck:
    def talk(self):
        print("Quack...Quack...!")

def fun(obj):
    obj.talk()

I = [Cat(),Dog(),Goat(),Duck()]
for i in I:
    fun(i)
"""





#Problem in above example:
#AttributeError: 'Dog' object has no attribute 'talk'
"""
class Cat:
    def talk(self):
        print("Mew....Mew...!")

class Dog:
    def bark(self):
        print("Bhow...Bhow....!")

class Goat:
    def talk(self):
        print("Meahh....Meahh..!")

class Duck:
    def talk(self):
        print("Quack...Quack...!")

def fun(obj):
    obj.talk()

I = [Cat(),Dog(),Goat(),Duck()]
for i in I:
    fun(i)
"""





#AttributeError Problem in above example Is Solved:
"""
class Cat:
    def talk(self):
        print("Mew....Mew...!")

class Dog:
    def bark(self):
        print("Bhow...Bhow....!")

class Goat:
    def talk(self):
        print("Meahh....Meahh..!")

class Human:
    def speak(self):
        print("Hey...Hello...!")

def fun(obj):
    if hasattr(obj,'talk'):
        obj.talk()
    elif hasattr(obj,"bark"):
        obj.bark()
    elif hasattr(obj,"speak"):
        obj.speak()

I = [Cat(),Dog(),Goat(),Human()]
for i in I:
    fun(i)
"""