import re

##word = input('Enter a word with only letters and numbers:  ')
##
##if (re.search(r'^[\w]*$', word)) and not(re.search(r'_',word)):
##    print('yay')
##else:
##    print('boo')


##word= input('Enter a word with one uppercase then lower case letters:  ')
##pat = '^[A-Z][a-z]+$'
##if (re.search(pat,word)):
##    print('awesome!')
##else:
##    print('terrible!')


word= input('Enter a word with a z in it:  ')
pat = '^[^zZ]\w*[zZ]\w*[^zZ]$'
#\w = letters, numbers, and _
if (re.search(pat, word)):
    print("There's one!")
else:
    print("Missed it.")
    

##email = input("Email Address: ")
##userName, domain = email.split('@')
##print(userName)
##print(domain)

##sentence = input("Give me your sentences. ")
##words = re.findall(r'the\b', sentence, re.I)
##print(len(words))
##print(words)

