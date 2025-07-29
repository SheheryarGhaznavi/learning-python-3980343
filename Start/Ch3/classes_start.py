# LinkedIn Learning Python course by Joe Marini
# Example file for working with classes
#

class vehicle :


	def __init__(self, body_style):

		self.body_style = body_style


	def drive(self, speed) :

		self.mode = 'driving'
		self.speed = speed
		print("in main function")



class Car(vehicle) :


	def __init__(self, engine_type):

		super().__init__("Car")
		self.engine_type = engine_type
		self.wheels = 4
		self.doors = 4


	def drive(self, speed) :

		super().drive(speed)
		print("in override function")


class Motorcycle(vehicle) :


	def __init__(self, engine_type, has_side_car = False):

		super().__init__("Motorcycle")
		self.engine_type = engine_type

		if has_side_car :
			self.wheels = 3
		else :
			self.wheels = 2

		self.doors = 0



car1 = Car('gas')
car2 = Car('hybrid')

motor1 = Motorcycle('gas')
motor2 = Motorcycle('gas', True)

print(car1.body_style)
print(car1.doors)
print(car1.engine_type)
print(car1.doors)
# print(car1.speed)
print(car1.drive(30))
print(car1.speed)
