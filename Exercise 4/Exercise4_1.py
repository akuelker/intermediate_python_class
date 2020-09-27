import re
#Using string matching
try:
	inAge = input("Enter your age: " )
	if (re.search(r'^[0-9]+$', inAge)):
		print("Good Age")
		if int(inAge) > 122:
			raise NameError("Age must be a whole number greater than 0.")
	else:
		raise NameError("Age must be a whole number greater than 0.")
except  NameError as ex:
	print(ex)

#using typing	
try:
	intAge = int(input("Enter your age"))
	if intAge < 123 and intAge >= 0: #oldest person who ever lived
		print ("Good Age")
	else: 
		raise NameError("Age must be a whole number between 122 than 0.")
except  NameError as ex:
	print(ex)
except ValueError:
	print("You didn't enter a valid number")