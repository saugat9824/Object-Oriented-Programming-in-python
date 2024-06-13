# Static Methode
# Add a static methode to the Car class that returns a general description of a Car.
"""
a method that belongs to a class rather than an instance of aclass
"""

class Car:

    total_car = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_car += 1

    def get_brand(self):
        return self.brand + " !"
    

    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    

    @staticmethod # 
    def general_description(): # static methode don't need self connection.
         return "Cars are a means of transport"
    



class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)


def fuel_type(self):
        return "Electric charge"

    
#my_tesla = ElectricCar("Tesla", "Model S", "85KWh")
# print(my_tesla.brand)
# print(my_tesla.fuel_type())

my_car = Car("Tata", "Safari")
Car("Tata", "Nexon")
# print(safari.fuel_type())
# print( safari.total_car)

# print(my_car.general_description())
print(Car.general_description())
