#-----------------------------------HEADERS-----------------------------------#
import pandas as pd
#-----------------------------------HEADERS-----------------------------------#

#---------------IMPORT FILES and PREPROCESSING--------------------------------#

cases_week = dict()
data1 = pd.read_csv('cases-week.csv')
for i,row in data1.iterrows():
    cases_week[str(row['districtid'])+'+'+str(row['weekid'])] = row['cases']

cases_month = dict()
data2 = pd.read_csv('cases-month.csv')
for i,row in data2.iterrows():
    cases_month[str(row['districtid'])+'+'+str(row['monthid'])] = row['cases']
    
cases_overall = dict()
data3 = pd.read_csv('cases-overall.csv')
for i,row in data3.iterrows():
    cases_overall[str(row['districtid'])+'+'+str(row['overallid'])] = row['cases']

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
weekNeighSPOT = dict()
weekStateSPOT = dict()

for i in cases_week.items():
    if i[1] > neighbor_week_Mean[i[0]] + neighbor_week_SD[i[0]]:
        weekNeighSPOT[i[0]] = "hot"
    elif i[1] < neighbor_week_Mean[i[0]] - neighbor_week_SD[i[0]]:
        weekNeighSPOT[i[0]] = "cold"
    if i[1] > state_week_Mean[i[0]] + state_week_SD[i[0]]:
        weekStateSPOT[i[0]] = "hot"
    elif i[1] < state_week_Mean[i[0]] - state_week_SD[i[0]]:
        weekStateSPOT[i[0]] = "cold"
        
weekSPOT = []
for i in weekNeighSPOT.items():
    tmpList = []
    split = i[0].split('+')
    tmpList.append(int(split[1]))
    tmpList.append('neighborhood')
    tmpList.append(weekNeighSPOT[i[0]])
    tmpList.append(split[0])
    weekSPOT.append(tmpList)

for i in weekStateSPOT.items():
    tmpList = []
    split = i[0].split('+')
    tmpList.append(int(split[1]))
    tmpList.append('state')
    tmpList.append(weekStateSPOT[i[0]])
    tmpList.append(split[0])
    weekSPOT.append(tmpList)

weekSPOT.sort()
weekSPOT.insert(0,['weekid','method','spot','districtid'])

out = pd.DataFrame(weekSPOT)
out.to_csv('method-spot-week.csv',index=False,header=False)

#-------------------------PROCESSING WEEK DATA--------------------------------#


#-------------------------PROCESSING MONTH DATA-------------------------------#
monthNeighSPOT = dict()
monthStateSPOT = dict()

c3 = 0
c4 = 0
for i in cases_month.items():
    if i[1] > neighbor_month_Mean[i[0]] + neighbor_month_SD[i[0]]:
        monthNeighSPOT[i[0]] = "hot"
    elif i[1] < neighbor_month_Mean[i[0]] - neighbor_month_SD[i[0]]:
        monthNeighSPOT[i[0]] = "cold"
    if i[1] > state_month_Mean[i[0]] + state_month_SD[i[0]]:
        monthStateSPOT[i[0]] = "hot"
    elif i[1] < state_month_Mean[i[0]] - state_month_SD[i[0]]:
        monthStateSPOT[i[0]] = "cold"
        
monthSPOT = []
for i in monthNeighSPOT.items():
    tmpList = []
    split = i[0].split('+')
    tmpList.append(int(split[1]))
    tmpList.append('neighborhood')
    tmpList.append(monthNeighSPOT[i[0]])
    tmpList.append(split[0])
    monthSPOT.append(tmpList)

for i in monthStateSPOT.items():
    tmpList = []
    split = i[0].split('+')
    tmpList.append(int(split[1]))
    tmpList.append('state')
    tmpList.append(monthStateSPOT[i[0]])
    tmpList.append(split[0])
    monthSPOT.append(tmpList)

monthSPOT.sort()
monthSPOT.insert(0,['monthid','method','spot','districtid'])

out = pd.DataFrame(monthSPOT)
out.to_csv('method-spot-month.csv',index=False,header=False)

#-------------------------PROCESSING MONTH DATA-------------------------------#
 

#-------------------------PROCESSING OVERALL DATA-----------------------------#
overallNeighSPOT = dict()
overallStateSPOT = dict()

for i in cases_overall.items():
    if i[1] > neighbor_overall_Mean[i[0]] + neighbor_overall_SD[i[0]]:
        overallNeighSPOT[i[0]] = "hot"
    elif i[1] < neighbor_overall_Mean[i[0]] - neighbor_overall_SD[i[0]]:
        overallNeighSPOT[i[0]] = "cold"
    if i[1] > state_overall_Mean[i[0]] + state_overall_SD[i[0]]:
        overallStateSPOT[i[0]] = "hot"
    elif i[1] < state_overall_Mean[i[0]] - state_overall_SD[i[0]]:
        overallStateSPOT[i[0]] = "cold"
        
overallSPOT = []
for i in overallNeighSPOT.items():
    tmpList = []
    split = i[0].split('+')
    tmpList.append(int(split[1]))
    tmpList.append('neighborhood')
    tmpList.append(overallNeighSPOT[i[0]])
    tmpList.append(split[0])
    overallSPOT.append(tmpList)

for i in overallStateSPOT.items():
    tmpList = []
    split = i[0].split('+')
    tmpList.append(int(split[1]))
    tmpList.append('state')
    tmpList.append(overallStateSPOT[i[0]])
    tmpList.append(split[0])
    overallSPOT.append(tmpList)

overallSPOT.sort()
overallSPOT.insert(0,['overallid','method','spot','districtid'])

out = pd.DataFrame(overallSPOT)
out.to_csv('method-spot-overall.csv',index=False,header=False)

#-------------------------PROCESSING OVERALL DATA-----------------------------#      