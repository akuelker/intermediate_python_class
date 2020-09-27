import re, os
mypath = input("What directory needs their files renamed")
filenames = list()

for filename in os.listdir(mypath):
	if (re.search(r'sample', filename)):
		newname = (re.sub("sam", "sample", filename))
		fullNamePath = mypath+"\\"+filename
		fullNewNamePath = mypath+"\\"+newname
		print(fullNewNamePath)
		os.rename(fullNamePath,fullNewNamePath)
