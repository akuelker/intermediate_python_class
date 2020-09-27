import Book

book1 = Book.Book('The Three Princesses', 2019, 'A Kuelker', 'Fantasy', 'In')
book1.displayInfo()

book1.checkOut()
print("I checked out this sweet book!")
book1.displayInfo()

mag1 = Book.Magazine('Bradleigh Boo', 'Zoology Today', 2016, 'Nature',
                     'Out', 'February')
mag1.displayInfo()
mag1.getPubDate()
