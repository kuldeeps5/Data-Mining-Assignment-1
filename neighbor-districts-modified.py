import json
import pandas as pd

myfile = pd.read_csv("mapAllDictToOne.csv")
jsonFile = open("neighbor-districts.json")
jsonDict = json.load(jsonFile)

start = "1234567"
mydict = {}
check = {}
for i,row in myfile.iterrows():
    if (str(row[1])+str(start)) in check:
        mydict[row[0]] = str(row[1])+"/Q"+str(start)
    else:
        start = str(int(start)+1)
        check[str(row[1])+str(start)] = 1
        mydict[row[0]] = str(row[1])+"/Q"+str(start)
######################################################
newDict = {}

for k in (jsonDict):
    val1 = k
    if k in mydict:
        val1 = mydict[k]
    tmpList = []
    for val2 in jsonDict[k]:
        if val2 in mydict:
            if (mydict[val2] != val1):
                tmpList.append(mydict[val2])
        else:
            tmpList.append(val2)
    if val1 in newDict:
        newDict[val1].extend(tmpList)
    else:
        newDict[val1] = tmpList

finalDict = {}
for i in newDict.items():
    s = set(i[1])
    finalDict[i[0]] = list(s)

#####################################################
with open('neighbor-districts-modified.json', 'w') as jsonFile:
    json.dump(finalDict, jsonFile, indent=4)