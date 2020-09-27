import datetime  

year = int(input("Enter your Church Year: " ))
today =  datetime.date(year,1,1)     # January 1st
today += datetime.timedelta(days = 6 - today.weekday())  # First Sunday

while today.year == year:
	print(today)
	today+= datetime.timedelta(days = 7)
  