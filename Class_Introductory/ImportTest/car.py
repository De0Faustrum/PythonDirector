class Car:

	def __init__(self, brand, colour, price):
		#similar to the constructor in C++, the parameter "self" point to the entity itself.
		#And when we call functions, we don't need to fill the parameter "self".
		self.brand = brand
		self.colour = colour
		self.price = price

	def car_profile(self):
		print(f"My car is a {self.colour} {self.brand}, and I bought it for {self.price} dollars")

class Battery:
	def __init__(self, volume, voltage, current):
		self.volume = volume
		self.voltage = voltage
		self.current = current

	def battery_profile(self):
		print(f"Battery volume:{self.volume}kWh; Rated voltage:{self.voltage}V; Rated current:{self.current}A.")

class ElectricCar(Car):
	def __init__(self, brand, colour, price, volume, voltage, current):
		super().__init__(brand, colour, price)
		self.battery = Battery(volume, voltage, current)

	def car_profile(self):
		super().car_profile()
		self.battery.battery_profile()