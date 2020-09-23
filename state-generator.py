#-----------------------------------HEADERS-----------------------------------#
from collections import defaultdict
import pandas as pd
import statistics
#-----------------------------------HEADERS-----------------------------------#

#---------------IMPORT FILES and PREPROCESSING--------------------------------#
districtToState = pd.read_csv("districtTOstate.csv") # district to state
districtToID = pd.read_csv("neighbor-districts-modified.csv")   # district to id

dict_ID_to_STATE = dict()
dict_STATE_to_listIDs = defaultdict(list) 

dict_DISTRICT_to_ID  = dict()
for j,col in districtToID.iterrows():
        dict_DISTRICT_to_ID[ col['district']] = str(col['id'])

for i,row in districtToState.iterrows():
    dict_ID_to_STATE[dict_DISTRICT_to_ID[row['district']]] = row['state']

for i in dict_ID_to_STATE.items():
    dict_STATE_to_listIDs[i[1]].append(i[0])

colName = ['did','nid']
districtIDtoNeighbourID = pd.read_csv("edge-graph.csv",names=colName,header=None)
dictListDIDtoNID = defaultdict(list) 
for i,row in districtIDtoNeighbourID.iterrows():
    dictListDIDtoNID[str(row['did'])].append(str(row['nid']))
#weekData = pd.read_csv("cases-week.csv")
#monthData = pd.read_csv("cases-week.csv")
#overallData = pd.read_csv("cases-week.csv")

#---------------IMPORT FILES and PREPROCESSING--------------------------------#

#----------------------WEEK PROCESSING----------------------------------------#
id_week_Dict = dict()
data1 = pd.read_csv('cases-week.csv')
for i,row in data1.iterrows():
    id_week_Dict[str(row['districtid'])+'+'+str(row['weekid'])] = row['cases']

track_stand_deviation = defaultdict(list)
final_id_disState_mean = dict()
final_id_disState_mean = defaultdict(lambda:0,final_id_disState_mean)

for i in dictListDIDtoNID.items():
    if i[0]!= '516':
        curr_state = dict_ID_to_STATE[i[0]]
        curr_district_list = dict_STATE_to_listIDs[curr_state]
        for j in range(1,26):
            entries = 0
            for k in curr_district_list:
                if k != i[0]:
                    entries += 1
                    track_stand_deviation[i[0]+'+'+str(j)].append(id_week_Dict[k+'+'+str(j)])
                    final_id_disState_mean[i[0]+'+'+str(j)] += id_week_Dict[k+'+'+str(j)]
            if entries != 0:
                final_id_disState_mean[i[0]+'+'+str(j)] /= entries
                final_id_disState_mean[i[0]+'+'+str(j)] = \
                    '{0:.2f}'.format(final_id_disState_mean[i[0]+'+'+str(j)])
            else:
                final_id_disState_mean[i[0]+'+'+str(j)] = '{0:.2f}'.format(float(0))
                track_stand_deviation[i[0]+'+'+str(j)].append(0)
    else:
        for j in range(1,26):
            final_id_disState_mean[i[0]+'+'+str(j)] = '{0:.2f}'.format(float(0))
            track_stand_deviation[i[0]+'+'+str(j)].append(0)
               
final_id_disState_staDeviation = dict()
for i in track_stand_deviation.items():
    l = len(i[1])
    if l>1:
        tmpL = [float(x) for x in i[1]]
        final_id_disState_staDeviation[i[0]] = '{0:.2f}'.format(statistics.stdev(tmpL))
    else:
        final_id_disState_staDeviation[i[0]] = '{0:.2f}'.format(float(0))
        
finalWeekList = []
finalWeekList.append(['districtid','weekid','statemean','statestdev'])
for i in final_id_disState_staDeviation.items():
    tmpList = []
    firstTwo = i[0].split('+')
    tmpList.append(firstTwo[0])
    tmpList.append(firstTwo[1])
    tmpList.append(final_id_disState_mean[i[0]])
    tmpList.append(final_id_disState_staDeviation[i[0]])
    finalWeekList.append(tmpList)

out = pd.DataFrame(finalWeekList)
out.to_csv('state-week.csv',index=False,header=False)
#----------------------WEEK PROCESSING----------------------------------------#

#---------------------MONTH PROCESSING----------------------------------------#
id_month_Dict = dict()
data1 = pd.read_csv('cases-month.csv')
for i,row in data1.iterrows():
    id_month_Dict[str(row['districtid'])+'+'+str(row['monthid'])] = row['cases']

track_stand_deviation = defaultdict(list)
final_id_disState_mean = dict()
final_id_disState_mean = defaultdict(lambda:0,final_id_disState_mean)

for i in dictListDIDtoNID.items():
    if i[0]!= '516':
        curr_state = dict_ID_to_STATE[i[0]]
        curr_district_list = dict_STATE_to_listIDs[curr_state]
        for j in range(1,8):
            entries = 0
            for k in curr_district_list:
                if k != i[0]:
                    entries += 1
                    track_stand_deviation[i[0]+'+'+str(j)].append(id_month_Dict[k+'+'+str(j)])
                    final_id_disState_mean[i[0]+'+'+str(j)] += id_month_Dict[k+'+'+str(j)]
            if entries != 0:
                final_id_disState_mean[i[0]+'+'+str(j)] /= entries
                final_id_disState_mean[i[0]+'+'+str(j)] = \
                    '{0:.2f}'.format(final_id_disState_mean[i[0]+'+'+str(j)])
            else:
                final_id_disState_mean[i[0]+'+'+str(j)] = '{0:.2f}'.format(float(0))
                track_stand_deviation[i[0]+'+'+str(j)].append(0)
    else:
        for j in range(1,8):
            final_id_disState_mean[i[0]+'+'+str(j)] = '{0:.2f}'.format(float(0))
            track_stand_deviation[i[0]+'+'+str(j)].append(0)
               
final_id_disState_staDeviation = dict()
for i in track_stand_deviation.items():
    l = len(i[1])
    if l>1:
        tmpL = [float(x) for x in i[1]]
        final_id_disState_staDeviation[i[0]] = '{0:.2f}'.format(statistics.stdev(tmpL))
    else:
        final_id_disState_staDeviation[i[0]] = '{0:.2f}'.format(float(0))
        
finalMonthList = []
finalMonthList.append(['districtid','monthid','statemean','statestdev'])
for i in final_id_disState_staDeviation.items():
    tmpList = []
    firstTwo = i[0].split('+')
    tmpList.append(firstTwo[0])
    tmpList.append(firstTwo[1])
    tmpList.append(final_id_disState_mean[i[0]])
    tmpList.append(final_id_disState_staDeviation[i[0]])
    finalMonthList.append(tmpList)

out = pd.DataFrame(finalMonthList)
out.to_csv('state-month.csv',index=False,header=False)
#---------------------MONTH PROCESSING----------------------------------------#
        
#--------------------OVERALL PROCESSING---------------------------------------#
id_overall_Dict = dict()
data1 = pd.read_csv('cases-overall.csv')
for i,row in data1.iterrows():
    id_overall_Dict[str(row['districtid'])+'+'+str(row['overallid'])] = row['cases']

track_stand_deviation = defaultdict(list)
final_id_disState_mean = dict()
final_id_disState_mean = defaultdict(lambda:0,final_id_disState_mean)

for i in dictListDIDtoNID.items():
    if i[0]!= '516':
        curr_state = dict_ID_to_STATE[i[0]]
        curr_district_list = dict_STATE_to_listIDs[curr_state]
        for j in range(1,2):
            entries = 0
            for k in curr_district_list:
                if k != i[0]:
                    entries += 1
                    track_stand_deviation[i[0]+'+'+str(j)].append(id_overall_Dict[k+'+'+str(j)])
                    final_id_disState_mean[i[0]+'+'+str(j)] += id_overall_Dict[k+'+'+str(j)]
            if entries != 0:
                final_id_disState_mean[i[0]+'+'+str(j)] /= entries
                final_id_disState_mean[i[0]+'+'+str(j)] = \
                    '{0:.2f}'.format(final_id_disState_mean[i[0]+'+'+str(j)])
            else:
                final_id_disState_mean[i[0]+'+'+str(j)] = '{0:.2f}'.format(float(0))
                track_stand_deviation[i[0]+'+'+str(j)].append(0)
    else:
        for j in range(1,2):
            final_id_disState_mean[i[0]+'+'+str(j)] = '{0:.2f}'.format(float(0))
            track_stand_deviation[i[0]+'+'+str(j)].append(0)
               
final_id_disState_staDeviation = dict()
for i in track_stand_deviation.items():
    l = len(i[1])
    if l>1:
        tmpL = [float(x) for x in i[1]]
        final_id_disState_staDeviation[i[0]] = '{0:.2f}'.format(statistics.stdev(tmpL))
    else:
        final_id_disState_staDeviation[i[0]] = '{0:.2f}'.format(float(0))
        
finalOverallList = []
finalOverallList.append(['districtid','overallid','statemean','statestdev'])
for i in final_id_disState_staDeviation.items():
    tmpList = []
    firstTwo = i[0].split('+')
    tmpList.append(firstTwo[0])
    tmpList.append(firstTwo[1])
    tmpList.append(final_id_disState_mean[i[0]])
    tmpList.append(final_id_disState_staDeviation[i[0]])
    finalOverallList.append(tmpList)

out = pd.DataFrame(finalOverallList)
out.to_csv('state-overall.csv',index=False,header=False)
#--------------------OVERALL PROCESSING---------------------------------------#