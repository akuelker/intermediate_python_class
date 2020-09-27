even = lambda x: x%2 ==0
evenList = []
for i in range(1, 21):
	if(even(i)):
		evenList.append(i)
print(evenList)

#option 2
numberList = []
for i in range(1,21):
	numberList.append(i)
evens = list(filter(even, numberList))
print(evens)
	