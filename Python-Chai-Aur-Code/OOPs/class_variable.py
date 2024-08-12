class Car:
	total_car = 0
	# constructor 
	def __init__(self,brand,model):
		self.brand = brand
		self.model = model
		Car.total_car += 1

	def full_name(self):
		return f"{self.brand} {self.model}"

	def fuel_type(self):
		return "Petrol or Diesel"

class ElectricCar(Car):
	def __init__(self,brand,model,battery_size):
		super().__init__(brand,model)
		self.battery_size = battery_size

	def fuel_type(self):
		return "Electric Charge"



my_tesla = ElectricCar("Tesla" , "Model 5" , "85Kwh")
print(my_tesla.model)

my_car = Car("Toyota","Corolla")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())


my_new_car = Car('Tata',"Safari")
print(my_new_car.model)

print(Car.total_car)
