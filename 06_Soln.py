# Class Variable
# Add a class varible to Car that keeps track of th number of Cars created.


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
    



class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)


def fuel_type(self):
        return "Electric charge"

    
#my_tesla = ElectricCar("Tesla", "Model S", "85KWh")
# print(my_tesla.brand)
# print(my_tesla.fuel_type())

safari = Car("Tata", "Safari")
safariThree = Car("Tata", "Nexon")
# print(safari.fuel_type())
# print( safari.total_car)

print(Car.total_car)
