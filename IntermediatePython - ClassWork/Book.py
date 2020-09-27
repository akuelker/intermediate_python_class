class Book:
    def __init__(self, title, year, author, genre, status):
        self.title = title
        self.year = year
        self.author = author
        self.genre = genre
        self.status = status

    def displayInfo(self):
        print('Title: ', self.title, ', Year: ', self.year, ' , Author: ',
              self.author, ' , Genre: ', self.genre, ' , Status: ', self.status)
        
    def checkOut(self):
        self.status = 'Out'

    def checkIn(self):
        self.status = 'In'
        
class Magazine(Book):
    def __init__(self, title, year, author, genre, issue, status):
        Book.__init__(self, author, title, year, genre, status)
        self.issue = issue

    def getPubDate(self):
        print('Pub Date: ', self.year, ' , ', self.issue)
