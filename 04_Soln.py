# Encapsulation 
# Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter methode for it.


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def get_brand(self):
        return self.brand + " !"
    

    def full_name(self):
        return f"{self.brand} {self.model}"
    

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)


my_tesla = ElectricCar("Tesla", "Model S", "85KWh")
print(my_tesla.brand)
print(my_tesla.get_brand())
