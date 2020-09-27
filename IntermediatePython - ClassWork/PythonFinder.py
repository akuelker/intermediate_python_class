import re #regular expressions/ regex
def findPython(textInput):
    pythonRegEx = re.compile('Python')
    matchedObject = pythonRegEx.search(textInput)
    if matchedObject:
        print('%s found' %matchedObject.group())
        return matchedObject
    else:
        print('No Match')
        return(None) #not necessary

textWPython = "Classes: Python Wed, R Friday, Tableau Mon"
textWOPython= "Classes: SQL Wed, R Friday, Tableau Mon"

findPython(textWPython)
findPython(textWOPython)
