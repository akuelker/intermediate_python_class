import re

class NotASalesList(Exception):
    print("No way.")
    pass

def getList(fileName):
    salesItems = list() #empty list
    try:
        fileObj = open(fileName, "r")
        line = fileObj.readline()
        while(line):
            if not (re.search('^/d', line)):
                raise NotASalesList("Not sales list, no num")

            line = fileObj.readline()
    except FileNotFoundError:
        print("You lost your file %s" %fileName)
    except NotASalesList as ex:
        print(ex.args)
        salesItems = list() #don't return partial fake list
    else:
        fileObj.close()
    finally:
        print("Return!")

getList("HasItems.txt")
getList("IDontExist.txt")
