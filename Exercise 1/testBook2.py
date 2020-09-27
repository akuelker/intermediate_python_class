import Book2
mag1 = Book2.Magazine('Kim Casey', 'Monthly Computer', 
	2017, 'Business', 'June', True)
print("\n Show the library's magazine")
mag1.displayInfo()
mag1.getPubDate()

print("\nCheck out the magazine\n")
mag1.checkOut();
print("Show the magazine's check in status")
mag1.displayInfo()

