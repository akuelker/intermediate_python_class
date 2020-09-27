import pypyodbc
class DBWork:
	#Does all the database details like connections, 
	#printing out the rows, and closing
	def __init__(self, dbname):
		from os import getcwd
		try:
			pypyodbc.lowercase = False
			#we are running the program in the same folder as the database
			path =  getcwd()+"\\"+dbname
			print(path)
			self.connection = pypyodbc.connect(
				r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};" +
				r"Dbq="+path+";")
			self.cur = self.connection.cursor()
		except Exception as ex:
			print("Database Error: %s" %ex)
		
	def printResults(self, sql):
		self.cur.execute(sql)
		for row in self.cur:
			line = ""
			for item in row:
				line+= str(item) + " "
			print(line)
	def close(self):
		if hasattr(self, 'connection'):	#database connection exists
			if hasattr(self, 'cur'):
				self.cur.close()
			if self.connection is not None:
				self.connection.close()

def SelectAll():
	try:
		sql = "select * from books"
		dbConn = DBWork("datatables.mdb")
		dbConn.printResults(sql)
	except Exception as ex:
		print("Database Error: %s" %ex)
		print("****************")
		print(sql)
		print("***************")
	finally:
		if dbConn is not None:
			dbConn.close()

SelectAll()






