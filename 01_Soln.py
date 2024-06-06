# Basic Class and Object
# Create a Car class with attributes like brand and model. Then create an instance of this class.

class Car:
    def __init__(self, brand, model): # ___init__ known as constructor
        self.brand = brand
        self.model = model


my_car = Car("Toyota", "Corolla") # object 
print(my_car.brand)
print(my_car.model)


# to use another object

my_new_car = Car("Tata", "Safari")
print(my_new_car.model)
print(my_new_car.brand)
