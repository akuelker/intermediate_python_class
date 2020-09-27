from Ex5_Menu import Menu
from Exercise5_1 import SelectAll
from Exercise5_2 import SortAll
from Exercise5_3 import SearchBy
from Exercise5_4 import InsertInto
from Exercise5_5 import UpdateQty
from Exercise5_6 import DeleteBook

while True:
	option = Menu()
	print("option is %s" %option)
	if (option == 1):
		SelectAll()
	elif (option == 2):
		SortAll()
	elif (option == 3):
		SearchBy()
	elif (option == 4):
		InsertInto()
	elif (option == 5):
		UpdateQty()
	elif(option == 6):
		DeleteBook()
	else:
		break
