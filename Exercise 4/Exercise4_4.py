import re
class LineNotNumberedItem(Exception):
	pass

def getList(fileName):
	salesItems = {}
	lineItemRegEx = re.compile(r'(\d+)\s+(\w+)')
	try:
		fileObj =  open(fileName, "r")
		line = fileObj.readline()
		while(line):
			matchedItem = lineItemRegEx.search(line.rstrip())
			if matchedItem:
				print(matchedItem.group(1), " ", matchedItem.group(2))
				salesItems[matchedItem.group(1)] = matchedItem.group(2)
			else:
				raise NotASalesList("Not a sales list")
			line = fileObj.readline()
		fileObj.close()
	except NotASalesList as ex:
		print("File had an item that wasn't number item")
		fileObj.close()
	except FileNotFoundError:
		print("File does not exist %s" %fileName)
	else:
		fileObj.close()
	finally:
		return(salesItems)
print("Notexist.txt has %s items for sale " %len(getList("Notexist.txt")))
print("pickled has %s items for sale " %len(getList("pickled")))
print("HasItems.txt has %s items for sale " %len(getList("HasItems.txt")))

