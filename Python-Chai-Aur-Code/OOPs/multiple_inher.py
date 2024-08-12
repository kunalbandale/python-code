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

class Battery:
    def __init__(self, battery_size):
        self.battery_size = battery_size

    def get_battery_info(self):
        return f"Battery size: {self.battery_size}"

class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type

    def get_engine_info(self):
        return f"Engine type: {self.engine_type}"

class ElectricCarTwo(Car, Battery, Engine):
    def __init__(self, brand, model, battery_size, engine_type):
        Car.__init__(self, brand, model)
        Battery.__init__(self, battery_size)
        Engine.__init__(self, engine_type)

    def fuel_type(self):
        return "Electric Charge"

# Testing the multiple inheritance
my_new_tesla = ElectricCarTwo("Tesla", "Model S", "100Kwh", "Electric")
print(my_new_tesla.full_name)             # Outputs: Tesla Model S
print(my_new_tesla.get_battery_info())    # Outputs: Battery size: 100Kwh
print(my_new_tesla.get_engine_info())     # Outputs: Engine type: Electric
print(my_new_tesla.fuel_type())           # Outputs: Electric Charge
