import re
emailAddress = input("Enter a valid email address: ")
userName, domain = emailAddress.split('@')
print(userName)
print(domain)