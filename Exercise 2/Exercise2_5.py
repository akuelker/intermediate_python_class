import re
sentence = input("Enter one or more sentences: ")
words=re.findall(r'the\b',sentence, re.I)
print("'The' Count: " , len(words))
print(words)