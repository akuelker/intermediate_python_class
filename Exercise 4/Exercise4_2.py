try:
	#ValueError 
	num = float(input("Enter a numerator: " ))
	denom = float(input("Enter a denominator: " ))	
	#ZeroDivisionError
	print("%s / %s = %s" % (num, denom, num /denom))
except ValueError as ex:
	print("You didn't enter a valid number", ex)
except  ZeroDivisionError as ex:
	print("Error caught: ", ex)	