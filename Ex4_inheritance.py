""""
Develop a Python program that models a vehicle hierarchy. Implement classes for vehicles such as car, bike, and 
truck, inheriting common features from a parent class.
"""
#Hint: Vehicle have brand, model, year

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_info(self):
        return f"{self.year} {self.brand} {self.model}"
    
    def start_engine(self):
        return "Engine started. Ready to go!"

class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors
    
    def display_info(self):
        return f"{super().display_info()} - {self.doors} doors"

class Bike(Vehicle):
    def __init__(self, brand, model, year, type_of_bike):
        super().__init__(brand, model, year)
        self.type_of_bike = type_of_bike
    
    def display_info(self):
        return f"{super().display_info()} - {self.type_of_bike} bike"

class Truck(Vehicle):
    def __init__(self, brand, model, year, capacity):
        super().__init__(brand, model, year)
        self.capacity = capacity  # in tons
    
    def display_info(self):
        return f"{super().display_info()} - {self.capacity} ton capacity"

car = Car("Toyota", "Camry", 2022, 4)
bike = Bike("Honda", "CBR500R", 2023, "Sports")
truck = Truck("Ford", "F-150", 2021, 5)

print(car.display_info())
print(car.start_engine())
print(bike.display_info())
print(truck.display_info())

        