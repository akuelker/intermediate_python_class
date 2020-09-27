import re 
#Allows z to be first character and last as long as there is a z in the middle
word = input("Enter a word with a 'z' in it: ")
#[^zZ] means can't be a z
pat = '[^zZ\W\d\s_]+[zZ][^zZ\W\d\s_]+'
#pat = '\Bz\B' # allows numbers and spaces

if (re.search(pat, word)):
	print("found a Z")
else:
	print("bad")