fpath = "dream.txt"
lines = list()
with open(fpath, 'r') as open_file:
	line = open_file.readline()
	while(line):
		lines.append(line.rstrip())
		line = open_file.readline()
open_file.close()
print("There are %s lines in '%s'" % (len(lines),fpath))

