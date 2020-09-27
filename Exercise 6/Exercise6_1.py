my_list = [1,2,3,4,5,6,7,8,9,10]

evens = list(filter((lambda x: x%2 ==0), my_list))
odds = list(filter((lambda x: x%2 >0), my_list))
print("Even: ", evens)
print("Odd: ", odds)