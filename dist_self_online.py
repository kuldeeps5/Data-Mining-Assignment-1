import json
import csv
import os
import pandas as pd

#######################################################
jsonFile = open("neighbor-districts-modified.json")
jsonDict = json.load(jsonFile)
listSelf = []
for k in (sorted(jsonDict)):
    key = k.split("/");
    t = ""
    for i in key[0]:
        if i!="_":
            t = t+i.lower()
    listSelf.append(t)
    
listSelf1 = []
for i in listSelf:
    if "district" in i:
        tmp = i.replace("district","")
        listSelf1.append(tmp)
    else:
        listSelf1.append(i)
df = pd.DataFrame(listSelf1)
df.to_csv('SELFDISTRICT.csv',header=False)

listOnline = set()
f = open("raw_Data_csv/districts.csv",'r')
with f:
    data = pd.read_csv("raw_Data_csv/districts.csv")
    reader = csv.reader(f)
    count  = 1
    for i,row in data.iterrows():
        district = str(row['District'])
        tmpstr = ""
        for i in district:
            if i!=" " and i!=".":
                tmpstr = tmpstr + i.lower() 
        listOnline.add(tmpstr)

print(len(listOnline))
listOnline = sorted(listOnline)
listOnline = list(listOnline)
df = pd.DataFrame(listOnline)
df.to_csv('ONLINEDISTRICT.csv',header=False)

MATCHLIST = list(set(listSelf1) & set(listOnline))
print("Matched : ",len(MATCHLIST))
print("Not Matched : ",723 - len(MATCHLIST))
SELFLIST = list(set(listSelf1) - set(MATCHLIST))
SELFONLINE = list(set(listOnline) - set(MATCHLIST))
SELFLIST = sorted(SELFLIST)
SELFONLINE = sorted(SELFONLINE)
df = pd.DataFrame(SELFONLINE)
df.to_csv('ONLINE_not_matched.csv',header=False)
df = pd.DataFrame(SELFLIST)
df.to_csv('SELF_not_matched.csv',header=False)
#######################################################
def editDistDP(str1, str2, m, n): 
    # Create a table to store results of subproblems 
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)] 
  
    # Fill d[][] in bottom up manner 
    for i in range(m + 1): 
        for j in range(n + 1): 
  
            # If first string is empty, only option is to 
            # insert all characters of second string 
            if i == 0: 
                dp[i][j] = j    # Min. operations = j 
  
            # If second string is empty, only option is to 
            # remove all characters of second string 
            elif j == 0: 
                dp[i][j] = i    # Min. operations = i 
  
            # If last characters are same, ignore last char 
            # and recur for remaining string 
            elif str1[i-1] == str2[j-1]: 
                dp[i][j] = dp[i-1][j-1] 
  
            # If last character are different, consider all 
            # possibilities and find minimum 
            else: 
                dp[i][j] = 1 + min(dp[i][j-1],        # Insert 
                                   dp[i-1][j],        # Remove 
                                   dp[i-1][j-1])    # Replace 
  
    return dp[m][n]
    
colnames=['first','second'] 
#user1 = pd.read_csv('dataset/1.csv', names=colnames, header=None)
list1 = pd.read_csv("SELF_not_matched.csv",names=colnames,header=None)
list2 =  pd.read_csv("ONLINE_not_matched.csv",names=colnames,header=None)
dictMatching = {}
for i,row1 in list1.iterrows():
    tmpStr = ""
    l = 100
    for j,row2 in list2.iterrows():
        tempL = editDistDP(row1['second'],row2['second'],
                          len(row1['second']),len(row2['second']))
        if tempL < l:
            l = tempL
            tmpStr = row2['second']
    dictMatching[row1['second']] = tmpStr
 
#print(dictMatching)   
a_file = open("editDistance.csv", "w")
writer = csv.writer(a_file)
for key, value in dictMatching.items():
    writer.writerow([key, value])     






