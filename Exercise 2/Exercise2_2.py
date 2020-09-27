import re 
#matches only letters.  MiXed was allowed, but not per directions
word = input("Enter a word with uppercase then lower case letters: ")

pat = '^[A-Z][a-z]+$'

if (re.search(pat, word)):
	print("good")
else:
	print("bad")

