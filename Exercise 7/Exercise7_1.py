import datetime  
today = datetime.date.today()
print("Today is the %s day of %s" % \
	(format(today, '%j'), format(today, '%Y')))
