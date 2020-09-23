#-----------------------------------HEADERS-----------------------------------#
import pandas as pd
#-----------------------------------HEADERS-----------------------------------#

#---------------IMPORT FILES and PREPROCESSING--------------------------------#
id_week_Dict = dict()
data1 = pd.read_csv('cases-week.csv')
for i,row in data1.iterrows():
    id_week_Dict[str(row['districtid'])+'+'+str(row['weekid'])] = row['cases']

id_month_Dict = dict()
data2 = pd.read_csv('cases-month.csv')
for i,row in data2.iterrows():
    id_month_Dict[str(row['districtid'])+'+'+str(row['monthid'])] = row['cases']
    
id_overall_Dict = dict()
data3 = pd.read_csv('cases-overall.csv')
for i,row in data3.iterrows():
    id_overall_Dict[str(row['districtid'])+'+'+str(row['overallid'])] = row['cases']

neighbor_week_Mean = dict()
neighbor_week_SD = dict()
neighbor_week = pd.read_csv('neighbor-week.csv')
for i,row in neighbor_week.iterrows():
    neighbor_week_Mean[str(int(row['districtid']))+'+'+str(int(row['weekid']))] = row['neighbormean']
    neighbor_week_SD[str(int(row['districtid']))+'+'+str(int(row['weekid']))] = row['neighborstdev']

neighbor_month_Mean = dict()
neighbor_month_SD = dict()
neighbor_month = pd.read_csv('neighbor-month.csv')
for i,row in neighbor_month.iterrows():
    neighbor_month_Mean[str(int(row['districtid']))+'+'+str(int(row['monthid']))] = row['neighbormean']
    neighbor_month_SD[str(int(row['districtid']))+'+'+str(int(row['monthid']))] = row['neighborstdev']

neighbor_overall_Mean = dict()
neighbor_overall_SD = dict()  
neighbor_overall = pd.read_csv('neighbor-overall.csv')
for i,row in neighbor_overall.iterrows():
    neighbor_overall_Mean[str(int(row['districtid']))+'+'+str(int(row['overallid']))] = row['neighbormean']
    neighbor_overall_SD[str(int(row['districtid']))+'+'+str(int(row['overallid']))] = row['neighborstdev']

state_week_Mean = dict()
state_week_SD = dict()  
state_week = pd.read_csv('state-week.csv')
for i,row in state_week.iterrows():
    state_week_Mean[str(int(row['districtid']))+'+'+str(int(row['weekid']))] = row['statemean']
    state_week_SD[str(int(row['districtid']))+'+'+str(int(row['weekid']))] = row['statestdev']

state_month_Mean = dict()
state_month_SD = dict()  
state_month = pd.read_csv('state-month.csv')
for i,row in state_month.iterrows():
    state_month_Mean[str(int(row['districtid']))+'+'+str(int(row['monthid']))] = row['statemean']
    state_month_SD[str(int(row['districtid']))+'+'+str(int(row['monthid']))] = row['statestdev']

state_overall_Mean = dict()
state_overall_SD = dict()  
state_overall = pd.read_csv('state-overall.csv')
for i,row in state_overall.iterrows():
    state_overall_Mean[str(int(row['districtid']))+'+'+str(int(row['overallid']))] = row['statemean']
    state_overall_SD[str(int(row['districtid']))+'+'+str(int(row['overallid']))] = row['statestdev']
#---------------IMPORT FILES and PREPROCESSING--------------------------------#


#-------------------------PROCESSING WEEK DATA--------------------------------#
dictNeighWeekZS = dict()
dictStateWeekZS = dict()
for j in id_week_Dict.items():
    if neighbor_week_SD[j[0]]!= 0:
        dictNeighWeekZS[j[0]] = '{0:.2f}'.format((j[1] - neighbor_week_Mean[j[0]])/neighbor_week_SD[j[0]])
    else:
        dictNeighWeekZS[j[0]] = '{0:.2f}'.format(float(0))
    if state_week_SD[j[0]]!=0:
        dictStateWeekZS[j[0]] = '{0:.2f}'.format((j[1] - state_week_Mean[j[0]])/state_week_SD[j[0]])
    else:
        dictStateWeekZS[j[0]] = '{0:.2f}'.format(float(0))
    
weekZS = []
weekZS.append(['districtid','weekid','neighborhoodzscore','statezscore'])
for i in dictNeighWeekZS.items():
    tmpList = []
    split = i[0].split('+')
    tmpList.append(split[0])
    tmpList.append(split[1])
    tmpList.append(dictNeighWeekZS[i[0]])
    tmpList.append(dictStateWeekZS[i[0]])
    weekZS.append(tmpList)

out = pd.DataFrame(weekZS)
out.to_csv('zscore-week.csv',index=False,header=False)
#-------------------------PROCESSING WEEK DATA--------------------------------#


#-------------------------PROCESSING MONTH DATA-------------------------------#       
dictNeighMonthZS = dict()
dictStateMonthZS = dict()
for j in id_month_Dict.items():
    if neighbor_month_SD[j[0]]!= 0:
        dictNeighMonthZS[j[0]] = '{0:.2f}'.format((j[1] - neighbor_month_Mean[j[0]])/neighbor_month_SD[j[0]])
    else:
        dictNeighMonthZS[j[0]] = '{0:.2f}'.format(float(0))
    if state_month_SD[j[0]]!=0:
        dictStateMonthZS[j[0]] = '{0:.2f}'.format((j[1] - state_month_Mean[j[0]])/state_month_SD[j[0]])
    else:
        dictStateMonthZS[j[0]] = '{0:.2f}'.format(float(0))

monthZS = []
monthZS.append(['districtid','monthid','neighborhoodzscore','statezscore'])
for i in dictNeighMonthZS.items():
    tmpList = []
    split = i[0].split('+')
    tmpList.append(split[0])
    tmpList.append(split[1])
    tmpList.append(dictNeighMonthZS[i[0]])
    tmpList.append(dictStateMonthZS[i[0]])
    monthZS.append(tmpList)

out = pd.DataFrame(monthZS)
out.to_csv('zscore-month.csv',index=False,header=False)        
#-------------------------PROCESSING MONTH DATA-------------------------------# 


#-------------------------PROCESSING OVERALL DATA-----------------------------#         
dictNeighOverallZS = dict()
dictStateOverallZS = dict()
for j in id_overall_Dict.items():
    if neighbor_overall_SD[j[0]]!= 0:
        dictNeighOverallZS[j[0]] = '{0:.2f}'.format((j[1] - neighbor_overall_Mean[j[0]])/neighbor_overall_SD[j[0]])
    else:
        dictNeighOverallZS[j[0]] = '{0:.2f}'.format(float(0))
    if state_overall_SD[j[0]]!=0:
        dictStateOverallZS[j[0]] = '{0:.2f}'.format((j[1] - state_overall_Mean[j[0]])/state_overall_SD[j[0]])
    else:
        dictStateOverallZS[j[0]] = '{0:.2f}'.format(float(0))

overallZS = []
overallZS.append(['districtid','overallid','neighborhoodzscore','statezscore'])
for i in dictNeighOverallZS.items():
    tmpList = []
    split = i[0].split('+')
    tmpList.append(split[0])
    tmpList.append(split[1])
    tmpList.append(dictNeighOverallZS[i[0]])
    tmpList.append(dictStateOverallZS[i[0]])
    overallZS.append(tmpList)

out = pd.DataFrame(overallZS)
out.to_csv('zscore-overall.csv',index=False,header=False)          
#-------------------------PROCESSING OVERALL DATA-----------------------------#     