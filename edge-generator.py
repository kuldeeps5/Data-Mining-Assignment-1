import json
import pandas as pd
jsonFile = open("neighbor-districts-modified.json")
jsonDict = json.load(jsonFile)
conFrom101_onward = {}
start = 101
for key in (sorted(jsonDict)):
    conFrom101_onward[key] = start
    start = start+1
finalList = []
for i in jsonDict:
    iTemp = []
    iTemp.append(conFrom101_onward[str(i)])
    tmpList = []
    for j in jsonDict[i]:
        tmpList.append(conFrom101_onward[str(j)])
    iTemp.append(tmpList)
    finalList.append(iTemp)
for i in finalList:
    i[1].sort()
toCSV = []
for i in finalList:
    for j in i[1]:
        tmpList = []
        tmpList.append(i[0])
        tmpList.append(j)
        toCSV.append(tmpList)
toCSV = sorted(toCSV, key=lambda x: x[0])
df = pd.DataFrame(toCSV)
df.to_csv('edge-graph.csv',header=False,index=False)