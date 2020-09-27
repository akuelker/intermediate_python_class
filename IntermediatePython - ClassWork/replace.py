import re

def replaceVersion(textInput, version):
    return re.sub('Python \d([.]\d)+',
                  version, textInput)

oldVersion1 = "Python 0.9.1"
oldVersion2 = "blah blah Python 2.7" + \
              " more blah Python 2.7"

print(replaceVersion(oldVersion1, "Python 3.6"))
print(replaceVersion(oldVersion2, "Python 3.6"))
