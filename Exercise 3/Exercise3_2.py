fileName = "dream.txt"
file1 = open(fileName, "a") #This appends the line to the end of the file
file1.write(input("Enter line to add to file: ") + "\n")
file1.close()

file1 = open(fileName, "r")
fileData = file1.read()
print(fileData)
file1.close()

