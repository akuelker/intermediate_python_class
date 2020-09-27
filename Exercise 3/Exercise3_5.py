import re 
file1 = open("dream.txt", "r+")
fileData = file1.read()

words=re.findall(r'the\b',fileData, re.I)
print("The word 'the' was found %s times" %len(words))

