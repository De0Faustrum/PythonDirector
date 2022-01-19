#Class：
#1.Basic syntax，for example:
class Car:

	def __init__(self, brand, colour, price):
		#similar to the constructor in C++, the parameter "self" point to the entity itself.
		#And when we call functions, we don't need to fill the parameter "self".
		self.brand = brand
		self.colour = colour
		self.price = price

	def car_profile(self):
		print(f"My car is a {self.colour} {self.brand}, and I bought it for {self.price} dollars")

my_car=Car("BMW","blue",120000)
my_car.car_profile()
	
	#(1).We can set default for some of the attributes of a class.

	#(2).To modify the attributes of an entity, we can directly use the statement below:
		#my_car.colour = "green"
	#But for security, calling function (defined in class) to modify is more common:
		#def set_car_colour(self, colour):
			#self.colour = colour
		#......
		#my_car.set_car_colour("green")

#2.Class inheritance:
	#(1).Subclass possess all the attributes and functions of the superclass.
	#(2).When calling functions in superclass, place the prifix "super()."

class ElectricCar(Car):
	#"voltage" is a newly added attribute.
	def __init__(self, brand, colour, price, voltage):
		super().__init__(brand, colour, price)
		#Initialize previous attributes.
		self.voltage = voltage
		#Initialize added attributes.

	def car_profile(self):
		super().car_profile()
		print(f"And its battery is {self.voltage} V.")

my_e_car = ElectricCar("BMW","Black",240000,220)
my_e_car.car_profile()

	#(3).We can also rewrite the super-function in subclass, the pre-version will be neglected.

#3.Entity inclusion:
	#(1).Entity inclusion makes the main class more succinct, for example:
class Battery:
	#Create an independent class to describe one aspect of the main class entity.
	def __init__(self, volume, voltage, current):
		self.volume = volume
		self.voltage = voltage
		self.current = current

	def battery_profile(self):
		print(f"Battery volume:{self.volume}kWh; Rated voltage:{self.voltage}V; Rated current:{self.current}A.")

class NewElecticCar(Car):
	def __init__(self, brand, colour, price, volume, voltage, current):
		super().__init__(brand, colour, price)
		self.battery = Battery(volume, voltage, current)

	def car_profile(self):
		super().car_profile()
		self.battery.battery_profile()

my_new_ecar = NewElecticCar("BMW", "Blue", 120000, 750, 220, 10)
my_new_ecar.car_profile()