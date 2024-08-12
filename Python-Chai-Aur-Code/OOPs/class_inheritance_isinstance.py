class Car:
    # constructor 
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @property
    def full_name(self):
        return f"{self.brand} {self.model}"

    def fuel_type(self):
        return "Petrol or Diesel"
    
    # decorator 
    @staticmethod
    def general_description():
        return 'Cars are amazing'

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"

my_tesla = ElectricCar("Tesla", "Model 5", "85Kwh")
print(my_tesla.model)
print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, ElectricCar))
