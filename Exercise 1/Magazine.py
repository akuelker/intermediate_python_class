''' 
3. (Extra) Create a magazine class that inherits from the book class and adds a publication date and issue properties.
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

	def __init__(self, author, title, year, genre, inLibrary, issue):
		Book.__init__(self, author, title, year, genre, inLibrary)
		self.issue = issue
		
	def getPubDate(self):
		print('Publication Date: %s, %s' % (self.year, self.issue))
	

  
  