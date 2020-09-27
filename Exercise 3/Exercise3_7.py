import pickle
class Employee:
#Class representing employees
	#Class variable - all employees will get 
	#the same empCount returned to them
	empCount=0

	#constructor
	def __init__(self, name, title,salary):
		self.name = name
		self.title = \
			title
		self.salary = salary
		Employee.empCount += 1

	#Displays the total number of employees
	def displayCount(self):
		print ("Total Employee %d" % Employee.empCount)

	def displayEmployee(self):
		print ("Name: ", self.name, ", Title: ", 
			self.title, ", Salary: ", self.salary)
			
oldEmp1 = Employee("Biff Arfuss", "Manager", 5000)
fileName = "EmployeeList"
#open the file to pickle the objects
#Note - it is a binary write
fileObject = open(fileName, 'wb')

print("Storing Python Objects into a file: Serialization")
pickle.dump(oldEmp1, fileObject)
#file closed
fileObject.close()

print("Time has passed...")

#opening file and reading in the objects
#Note - it is a binary read
fileObject = open(fileName, 'rb')
print("Reconstituting the Employee - deserialization")
newEmpl1 = pickle.load(fileObject)
fileObject.close()

newEmpl1.displayEmployee()
newEmpl1.displayCount()
