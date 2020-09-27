def fileIOTest(filename):
    try:
        f1=open(filename, "r")
        print(f1.read())
    except FileNotFoundError as ex:
        print("Error - file %s not found!" %filename)
        print("Details:\n %s" %ex)

    
#have file
fileIOTest("dream.txt")
#don't have
fileIOTest("nightmare.txt")
