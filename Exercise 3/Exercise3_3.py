import os
fpath = os.getcwd() + "/dream.txt"
lines = list()

with open(fpath, 'r') as open_file:
	line = open_file.readline()
	while(line):
		lines.append(line.rstrip())
		line = open_file.readline()

#print(lines)
for line in lines:
	print(line)

