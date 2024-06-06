# Inheritance
# Create a Electric Car class that inherits from the car class and has an additional attribute battery_size.

class Car:
    def __init__(self, brand, model): # ___init__ known as constructor
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"
    

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model) # for access above
        self.batttery_size = battery_size


my_tesla = ElectricCar("Tesla", "Model S", "85kWH")
print(my_tesla.full_name())
