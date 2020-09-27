class Employee:
    empCount = 0
    def __init__(self, name, title, salary): #define, initialize
        self.name = name
        self.title = title
        self.salary = salary
        print(self.name, "has been hired.")
        Employee.empCount +=1

    def showEmpInfo(self):
        print("My name is:", self.name,
              "My position is:", self.title)

class Manager(Employee): #create new class using existing class as a base
    def __init__(self, name, title, salary, authority):
        Employee.__init__(self, name, title, salary)
        self.authority = authority
        print(self.name, "is in charge of", self.authority)
    
john = Employee("John Smith", "Procurement", 5)
print(john.name, john.title, john.salary)

john.parkingSpot = 'Next to door'
print('Parking:', john.parkingSpot)
john.showEmpInfo()

taylor = Manager("Taylor", "CEO", 60000, "Coffee") #second employee

print("Number of Employees", Employee.empCount)

#check if attribute exists
print("Parking check", hasattr(john, 'parkingSpot'))
print("Parking check", hasattr(taylor, 'parkingSpot'))

setattr(taylor, 'parkingSpot', 'by tree') #equivalent to taylor.parkingSpot = 'by tree'
print('Taylor parks:', taylor.parkingSpot)
delattr(taylor, 'parkingSpot')
