class Car:
    def __init__(self, make, model, year, vin, mileage):
        self.make = make
        self.model= model
        self.year = year
        self.vin = vin
        self.mileage = mileage

    def displayInfo(self):
        print('Make: ', self.make, ', Model: ',
              self.model, ', Year: ', self.year, ', Mileage: ', self.mileage)

    def setMileage(self, newMileage):
        self.mileage = newMileage

auto1 = Car('Kia', 'Sorrento', 2016, 'GVHSIE849TH', 70000)
auto1.displayInfo()
auto1.setMileage(72500)
auto1.displayInfo()

