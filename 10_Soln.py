# Multiple Inheritance.
# Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.


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



# my_tesla = ElectricCar("Tesla", "Model S", "85KWh")

# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricCar))



# print(my_tesla.brand)
# print(my_tesla.fuel_type())

    
# my_car = Car("Tata", "Safari")
# # my_car.model = "City"
# Car("Tata", "Nexon")

# print(my_car.model)



class Battery:
    def battery_info (self):
          return "this is battery"


class Engine:
    def engine_info(self):
         return "This is engine"
    
    


class ElectricCar2(Battery, Engine, Car):
     pass



my_new_tesla = ElectricCar2("tesla", "Model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())
