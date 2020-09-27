my_list = [1,2,3,4,5,6,7,8,9,10]
evens = list(filter((lambda x: x%2 ==0), my_list))
squared_evens = list(map(lambda x: x * x, evens))
print(squared_evens)

#you can also do it all at once
new_squared_evens = list(map(lambda x: x * x, \
	list(filter((lambda x: x%2 ==0), my_list))))
print(new_squared_evens)