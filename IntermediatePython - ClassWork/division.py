try:
    numerator = int(input("Enter number!!!"))
    denom = int(input("Anotha one"))
    print(numerator/denom)
#Division by 0
except ZeroDivisionError as ex:
    print("No zeroes")
    print(ex)
#Did not enter a valid number
except ValueError as ex:
    print("Not a number")
    print(ex)
    raise(IOError) #can raise any exception at any time
