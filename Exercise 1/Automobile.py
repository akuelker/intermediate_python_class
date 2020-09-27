#Filename: Automobile.py
''' Create a class that represents an automobile. 
An automobile has five attributes: make, model, year, VIN, and mileage. 
The class should have a constructor: one for a new automobile.
The class should have two methods: one to update mileage and one to display automobile information. 
 '''

class Automobile:

	def __init__(self, make, model, year, vin, mileage):
		self.make = make
		self.model = model
		self.year = year
		self.vin = vin
		self.mileage = mileage

	def displayInfo(self):
		print ('Make : ', self.make,  ', Model: ', self.model,  ', Year: ', self.year,  ', Mileage: ', self.mileage)

	def setMileage(self, newMileage):
		self.mileage = newMileage
		
