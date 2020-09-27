import datetime
d=datetime.datetime.now()
for ival in ['year', 'month', 'day', 'hour', \
	     'minute', 'second', 'microsecond']:
	print(ival, ':', getattr(d, ival))
