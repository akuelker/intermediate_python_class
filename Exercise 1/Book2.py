''' 3. Create a class that represents a library book. 
The book has attributes, author, title, year, genre, and check-in status.  
Write methods that allow the books information to be displayed, and checkout in and out of the library.
'''
class Book:

	def __init__(self, author, title, year, genre, inLibrary):
		self.author = author
		self.title = title
		self.year = year
		self.genre = genre
		self.inLibrary = inLibrary

	def displayInfo(self):
		print ('Author: ', self.author)
		print ('Title: ', self.title)
		print ('Year: ', self.year)
		print ('Genre: ', self.genre)
		print ('In Library: ', self.inLibrary)

	def checkOut(self):
		self.inLibrary = False
		
	def checkIn(self):
		self.inLibrary = True
		
class Magazine(Book):

	def __init__(self, author, title, year, genre, issue, inLibrary):
		Book.__init__(self, author, title, year, genre, inLibrary)
		self.issue = issue
		
	def getPubDate(self):
		print('Publication Date: %s, %s' % (self.year, self.issue))
	

  
  