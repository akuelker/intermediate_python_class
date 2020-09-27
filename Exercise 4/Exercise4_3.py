def getMonthName(month):
	monthNames = {
	1 : 'January',
	2 : 'February' ,
	3 : 'March' ,
	4 : 'April',
	5 : 'May',
	6 : 'June',
	7 : 'July',
	8 : 'August',
	9 : 'September',
	10 : 'October',
	11 : 'November',
	12 : 'December'}
    
	try:
		if (month < 1 or month > 12):
			raise ValueError("Month must be between 1 and 12")
		out = monthNames[month]
		return out
			
	except ValueError as ex:
			print(ex)
			return ""

myMonth = getMonthName(int(input("Enter a valid month number(1-12): ")))

if(len(myMonth) > 0):
	print(myMonth)

