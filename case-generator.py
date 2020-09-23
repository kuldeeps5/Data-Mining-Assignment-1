#-----------------------------------HEADERS-----------------------------------#
import json
from collections import defaultdict
from datetime import datetime,timedelta
import pandas as pd
#-----------------------------------HEADERS-----------------------------------#

#------------------------------INITIALIZATION---------------------------------#
mergedDistrict = ["goa", "delhi", "telangana", "assam"]
doubleTime = {"hamirpur/q2086180":"himachal pradesh","hamirpur/q2019757":"uttar pradesh",
              "bilaspur/q100157":"chhattisgarh","bilaspur/q1478939":"himachal pradesh",
              "pratapgarh/q1585433":"rajasthan","pratapgarh/q1473962":"uttar pradesh",
              "balrampur/q16056268":"chhattisgarh","balrampur/q1948380":"uttar pradesh",
              "aurangabad/q43086":"bihar","aurangabad/q592942":"maharashtra"}
sameDistName = ["hamirpur","bilaspur","pratapgarh","balrampur","aurangabad"]
editDistance = {}
colnames = ["local","online"]
editDis = pd.read_csv("FINAL_EDIT_DISTANCE.csv",names=colnames,header=None)
for i,row in editDis.iterrows():
    editDistance[row['online']] = row['local']
#------------------------------INITIALIZATION---------------------------------#
    

#-------------Reading first 2 raw csv files till 25th april-------------------#
finalList = []
ED = datetime.strptime('25042020', '%d%m%Y')
rawFiles = ['raw_Data_csv/raw_data1.csv','raw_Data_csv/raw_data2.csv']  
for filename in rawFiles:
    data = pd.read_csv(filename)
    for i,row in data.iterrows():
        tDate = row['Date Announced'].split('/')
        strTemp = ""
        for i in tDate:
            strTemp += i
        dateTemp = datetime.strptime(strTemp, '%d%m%Y')
        if dateTemp <= ED:
            tmp = []
            tmp.append(row['Date Announced'])
            t  =  ""
            district = str(row['Detected District'])
            if district == "nan":
                district = ""
            for i in district:
                if i!=" " and i!=".":
                    t = t + i.lower() 
            tmp.append(t)
            tmp.append(row['Num Cases'])
            tmp.append(str(row['Detected State']).lower())
            if tmp[1] == 'unknown':
                if tmp[3] in mergedDistrict:
                    finalList.append(tmp)
            elif (tmp[0] !='' and  tmp[1]!=''):
                finalList.append(tmp)
#-------------Reading first 2 raw csv files till 25th april-------------------#                       


#------Reading districts csv file from 26th april to 5th september------------# 
ed = datetime.strptime('05092020', '%d%m%Y')  
finalList_district = []
data = pd.read_csv('raw_Data_csv/districts.csv')
for i,row in data.iterrows():
    td = row['Date'].split('-')
    td.reverse()
    checkdate = ""
    for i in td:
        checkdate = checkdate + i     # 20042020
    ed_Dt = datetime.strptime(checkdate, '%d%m%Y')
    insert_Date = ed_Dt.strftime("%d/%m/%Y")
    if(ed_Dt <= ed):
        tmp = []
        tmp.append(insert_Date)
        t  =  ""
        district = str(row['District'])
        if district == "nan":
            district = ""
        for ch in district:
            if ch!=" " and ch!=".":
                t  = t+ch.lower()
        tmp.append(t)
        tmp.append(row['Confirmed'])
        tmp.append((str(row['State'])).lower())
        if tmp[1] == 'unknown':
            if tmp[3] in mergedDistrict:
                finalList_district.append(tmp)
        elif (tmp[0] !='' and  tmp[1]!=''):
            finalList_district.append(tmp)
#------Reading districts csv file from 26th april to 5th september------------#                      


        
#------------Map each district with id, starting from 101---------------------#
jsonFile = open("neighbor-districts-modified.json")
jsonDict = json.load(jsonFile)
conFrom101_onward = {}   # Dictionary contain mapped value starting from 101
start = 101
for key in (sorted(jsonDict)):
    t = ""
    for i in key:
        if i!="_":
            t = t+i.lower()
    if "district" in t:
        if t != "bijapurdistrict/q1727570":
            t = t.replace("district","")        
    conFrom101_onward[t] = start
    start = start+1
with open('neighbor-districts-modified.csv', 'w') as f:
    for key in conFrom101_onward.keys():
        f.write("%s,%s\n"%(key,conFrom101_onward[key]))
df = pd.read_csv("neighbor-districts-modified.csv", header=None)
df.to_csv("neighbor-districts-modified.csv", header=["district", "id"], index=False)
#------------Map each district with id, starting from 101---------------------#
        
        
#---------Make "district+date+state" key to deal with commulative------#
prevDit = {}

for i in finalList:
    prevDit[str(i[1])+"+"+str(i[3])] = prevDit.get(str(i[1])+"+"+str(i[3]), 0) + i[2]

SD = datetime.strptime('15032020', '%d%m%Y')    
dist_date_count = {}   # key is (districtName+Date)
dist_date_count = defaultdict(lambda:0,dist_date_count)
for i in finalList:
    tmp = ""
    split = i[0].split('/')
    for j in split:
        tmp += j
    tmpDate = datetime.strptime(tmp, '%d%m%Y')
    if tmpDate >= SD:
        dist_date_count[str(i[1])+"+"+str(i[0])+"+"+str(i[3])] += i[2]
  
for i in finalList_district:
    dist_date_count[str(i[1])+"+"+str(i[0])+"+"+str(i[3])] += i[2] - prevDit.get(str(i[1])+"+"+str(i[3]), 0)
    prevDit[str(i[1])+"+"+str(i[3])] = i[2]
count_dist_date_count = 0
for i in dist_date_count:
    count_dist_date_count += dist_date_count[i]
#---------Make "district+date+state" key to deal with commulative------#


#-----More cleaning of data(range in timestamp and present in our district dictionary)---#
outDistrict = []
for i in conFrom101_onward.items():
    tt = i[0].split('/')
    outDistrict.append(tt[0])

final_dist_date_count = {}
final_dist_date_count = defaultdict(lambda:0,final_dist_date_count)
for j in dist_date_count:
    distDateState = j.split('+')
    if distDateState[0] in editDistance:
        final_dist_date_count[j] = dist_date_count[j]
    elif distDateState[0] in outDistrict:
        final_dist_date_count[j] = dist_date_count[j]
    elif distDateState[2] in mergedDistrict:
        changed = distDateState[2]+"+"+distDateState[1]+"+"+distDateState[2]
        final_dist_date_count[changed] += dist_date_count[j]
        

count_final_dist_date_count = 0
for i in final_dist_date_count:
    count_final_dist_date_count += final_dist_date_count[i]
#-----More cleaning of data(range in timestamp and present in our district dictionary)---#
    

#-------------------Convert final_dist_date_count to listList----------------------#
listList = []
for i in final_dist_date_count:
    t1 = list()
    val = i.split('+')
    t1.append(val[0]+"+"+val[2])
    d2= val[1].split('/')
    listToStr = ''.join([str(elem) for elem in d2])
    curr_date = datetime.strptime(listToStr, '%d%m%Y')
    t1.append(curr_date)
    t1.append(final_dist_date_count[i])
    listList.append(t1)
df = pd.DataFrame(listList,columns=['districtState','date','cases'])
df = df.sort_values('date')
#-------------------Convert final_dist_date_count to listList----------------------#


#------------------------------OUTPUT WEEK FILE-------------------------------#
start_date = datetime.strptime('15032020', '%d%m%Y')
outputList = []
header = ['districtid','weekid','cases']
outputList.append(header)
week_no = 1
date_to_week = {}
for index,row in df.iterrows():
    if row['date'] > start_date + timedelta(days=6):
        week_no  = week_no + 1
        date_to_week[row['date']] = week_no
        start_date = start_date + timedelta(days=7)
    else:
        date_to_week[row['date']] = week_no
        
dictDict = {}
for i in conFrom101_onward:
    tmpDict = {}
    for j in range(1, 26):
        tmpDict[j] = 0
    dictDict[i] = tmpDict  
   
for index,row in df.iterrows():
    disName = row['districtState'].split('+')
    currDistrict = disName[0]
    currState = disName[1]
    disToAdd = ""
    if currDistrict in editDistance:
        for i in conFrom101_onward.items():
            if editDistance[currDistrict] == i[0].split('/')[0]:
                disToAdd = i[0]    
    elif currDistrict in outDistrict:
        if currDistrict in sameDistName:
            for i in conFrom101_onward.items():
                if currDistrict == i[0].split('/')[0]:
                    if doubleTime[i[0]] == currState:
                        disToAdd = i[0]
        else:
            for i in conFrom101_onward.items():
                if currDistrict == i[0].split('/')[0]:
                    disToAdd = i[0]
    elif currState in mergedDistrict:
        for i in conFrom101_onward.items():
            if currState == i[0].split('/')[0]:
                disToAdd = i[0]
    else:
        print("NOT FOUND")
        
    if disToAdd != "":
#        if disToAdd == "bid/q814037":
#            print(row['cases'])   
        dictDict[disToAdd][date_to_week[row['date']]] += row['cases']
        
outputWeekData = []
outputWeekData.append(['districtid','weekid','cases'])
for i in dictDict:
    for j in dictDict[i]:
        tmp = []
        tmp.append(conFrom101_onward[i])
        tmp.append(j)
        tmp.append(dictDict[i][j])
        outputWeekData.append(tmp)
out = pd.DataFrame(outputWeekData)
out.to_csv('cases-week.csv',index=False,header=False)

countCasesWeek = 0
checkCases = pd.read_csv('cases-week.csv')
for i,row in checkCases.iterrows():
    countCasesWeek += row['cases']
#print(countCasesWeek)
#------------------------------OUTPUT WEEK FILE-------------------------------#


#------------------------------OUTPUT MONTH FILE-------------------------------#
start_date = datetime.strptime('15032020', '%d%m%Y')
month_no = 1
counter = 1
date_to_month = {}
date_to_month[start_date] = 1
for index,row in df.iterrows():
    if row['date'].month != start_date.month:
        month_no += 1
        start_date = row['date']
    date_to_month[row['date']] = month_no
 

dictDict = {}
for i in conFrom101_onward:
    tmpDict = {}
    for j in range(1, 8):
        tmpDict[j] = 0
    dictDict[i] = tmpDict
   
for index,row in df.iterrows():
    disName = row['districtState'].split('+')
    currDistrict = disName[0]
    currState = disName[1]
    disToAdd = ""
    if currDistrict in editDistance:
        for i in conFrom101_onward.items():
            if editDistance[currDistrict] == i[0].split('/')[0]:
                disToAdd = i[0]    
    elif currDistrict in outDistrict:
        if currDistrict in sameDistName:
            for i in conFrom101_onward.items():
                if currDistrict == i[0].split('/')[0]:
                    if doubleTime[i[0]] == currState:
                        disToAdd = i[0]
        else:
            for i in conFrom101_onward.items():
                if currDistrict == i[0].split('/')[0]:
                    disToAdd = i[0]
    elif currState in mergedDistrict:
        for i in conFrom101_onward.items():
            if currState == i[0].split('/')[0]:
                disToAdd = i[0]
    else:
        print("NOT FOUND")
        
    if disToAdd != "":             
        dictDict[disToAdd][date_to_month[row['date']]] += row['cases']    
    
outputMonthData = []
outputMonthData.append(['districtid','monthid','cases'])
for i in dictDict:
    for j in dictDict[i]:
        tmp = []
        tmp.append(conFrom101_onward[i])
        tmp.append(j)
        tmp.append(dictDict[i][j])
        outputMonthData.append(tmp)
out = pd.DataFrame(outputMonthData)
out.to_csv('cases-month.csv',index=False,header=False)
countCasesMonth = 0
checkCases = pd.read_csv('cases-month.csv')
for i,row in checkCases.iterrows():
    countCasesMonth += row['cases']
#print(countCasesMonth)
#------------------------------OUTPUT MONTH FILE-------------------------------#


#------------------------------OUTPUT OVERALL FILE-----------------------------#
DisAlongQid_to_State = dict()    
    
outputOverallData = []
dictDict = {}
for i in conFrom101_onward:
    dictDict[i] = 0


for index,row in df.iterrows():
    disName = row['districtState'].split('+')
    currDistrict = disName[0]
    currState = disName[1]
    disToAdd = ""
    if currDistrict in editDistance:
        for i in conFrom101_onward.items():
            if editDistance[currDistrict] == i[0].split('/')[0]:
                disToAdd = i[0]    
    elif currDistrict in outDistrict:
        if currDistrict in sameDistName:
            for i in conFrom101_onward.items():
                if currDistrict == i[0].split('/')[0]:
                    if doubleTime[i[0]] == currState:
                        disToAdd = i[0]
        else:
            for i in conFrom101_onward.items():
                if currDistrict == i[0].split('/')[0]:
                    disToAdd = i[0]
    elif currState in mergedDistrict:
        for i in conFrom101_onward.items():
            if currState == i[0].split('/')[0]:
                disToAdd = i[0]
    else:
        print("NOT FOUND")
        
    if disToAdd != "":
        DisAlongQid_to_State[disToAdd] = currState               
        dictDict[disToAdd] += row['cases']  


outputOverallData = []
outputOverallData.append(['districtid','overallid','cases'])
for i in dictDict:
    tmp = []
    tmp.append(conFrom101_onward[i])
    tmp.append(1)
    tmp.append(dictDict[i])
    outputOverallData.append(tmp)
out = pd.DataFrame(outputOverallData)
out.to_csv('cases-overall.csv',index=False,header=False)
countCasesOverall = 0
checkCases = pd.read_csv('cases-overall.csv')
for i,row in checkCases.iterrows():
    countCasesOverall += row['cases']
#print(countCasesOverall)
#------------------------------OUTPUT OVERALL FILE-----------------------------#
    
    
#---------------------------District to State Mapping--------------------------#   
with open('districtTOstate.csv', 'w') as f:
    for key in DisAlongQid_to_State.keys():
        f.write("%s,%s\n"%(key,DisAlongQid_to_State[key]))
df = pd.read_csv("districtTOstate.csv", header=None)
df.to_csv("districtTOstate.csv", header=["district", "state"], index=False)        
#---------------------------District to State Mapping--------------------------#