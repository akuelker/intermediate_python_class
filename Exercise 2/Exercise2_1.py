import re 
#spaces not allowed.  Appears to work.  Haven't explained string match
word = input("Enter a word with only letters and numbers: ")

if (re.search(r'^[\w]*$', word)) and not(re.search(r'_', word)):
	print("good")
else:
	print("bad")
