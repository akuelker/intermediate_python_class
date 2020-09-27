import pypyodbc
import os
pypyodbc.lowercase = False
#we are running the program in the same folder as the database
path =  os.getcwd()+"\\"+"datatables.mdb"
print(path)
connection = pypyodbc.connect(
    r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};" +
    r"Dbq="+path+";")
cursor = connection.cursor()
cursor.execute("SELECT partnum, descrip, auto, "+\
               "price FROM mydust")
for row in cursor:
    print(row)
cursor.close()
connection.close()
