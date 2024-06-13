# Property Decorators
# Use a property decorator in the Car class to make the model attribute read-only.


class Car:

    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model= model
        Car.total_car += 1

    def get_brand(self):
        return self.brand + " !"
    

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    

    @staticmethod # 
    def general_description(): # static methode don't need self connection.
         return "Cars are a means of transport"
    

    @property
    def model(self):
         return self.__model


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)


def fuel_type(self):
        return "Electric charge"

    
my_car = Car("Tata", "Safari")
# my_car.model = "City"
Car("Tata", "Nexon")

print(my_car.model)

