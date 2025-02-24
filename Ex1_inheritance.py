"""
Create a class in Python representing a car. Instantiate multiple car objects and perform operations like accelerating, braking, and changing gear on each object. 
"""
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0
        self.gear = 1

    def accelerate(self, increase):
        self.speed += increase
        print(f"{self.make} {self.model} accelerated to {self.speed} km/h.")

    def brake(self, decrease):
        self.speed -= decrease
        if self.speed < 0:
            self.speed = 0
        print(f"{self.make} {self.model} slowed down to {self.speed} km/h.")

    def change_gear(self, new_gear):
        if new_gear in range(1, 6):  
            self.gear = new_gear
            print(f"{self.make} {self.model} changed to gear {self.gear}.")
        else:
            print("Invalid gear selection.")

# Creating multiple car objects
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Civic", 2023)
car3 = Car("Ford", "Mustang", 2021)

# Performing operations on car objects
car1.accelerate(30)
car1.change_gear(3)
car1.brake(10)

car2.accelerate(50)
car2.change_gear(4)
car2.brake(20)

car3.accelerate(70)
car3.change_gear(5)
car3.brake(40)
