def writeHelloWorld(filename):
    file = open(filename, "w") #opens file for writing. "w" is access type
    file.write("Hello World\n")
    file.write("Put into file %s" %filename)
    file.close()

def readFile(filename): #reads whole file at once
    file=open(filename,"r")
    print(file.read())
    file.close()
    if file.closed:
            print("file closed")

def readFileIter(filename):
    for line in open(filename, "r"):
        print(line, end= "Weird Key")
    if file.closed:
            print("file closed")
    print("\n")
    
def readlineFile(filename):
    #with closes file even w exceptions
    with open(filename, 'r') as open_file:
        line = open_file.readline()
        while line:
            print(line.rstrip()) #removes space
            line = open_file.readline()

def showFileAttributes(filename):
     file = open(filename, "r+")
     print(file.name, file.mode, file.encoding)
     print(file.closed, ": file closed")
     file.close()
     print(file.closed, ": file closed")

writeHelloWorld("test.txt")
print("File is ready at")
#readFile("test.txt")

showFileAttributes("test.txt")
