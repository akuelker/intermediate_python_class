import pickle

oldMascot = {"UMSL" :"Triton", "SLU" : "Billiken", "Webster" : "Gorlok",
             "Missouri S&T": "Miner"}

oldDaysInMonthList = [31,28,31,30,31,30]
fileName = "pickled"
with open(fileName, 'wb') as fileObject:
    print("Storing Python Objects into a file: "+\
          "Serialization")
    pickle.dump(oldMascot, fileObject)
    pickle.dump(oldDaysInMonthList, fileObject)
print("Time has passed...")
with open(fileName, 'rb') as fileObject:
    print("Reconstituting the objects - deserialization")
    newMascots = pickle.load(fileObject)
    print("newMascotsDict %s" % newMascots)
    newDays = pickle.load(fileObject)
    print("newDays %s" %newDays)
