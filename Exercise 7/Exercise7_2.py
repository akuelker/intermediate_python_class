import datetime  

today = datetime.date.today()
# isocalendar returns a tupple 
#with year, week number, weekday
weekNum = today.isocalendar()[1] 

print("Today is week number %s of %s" % \
	(weekNum, format(today, '%Y')))
