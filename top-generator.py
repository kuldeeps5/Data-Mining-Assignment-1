#-----------------------------------HEADERS-----------------------------------#
import pandas as pd
from collections import defaultdict
#-----------------------------------HEADERS-----------------------------------#

#---------------IMPORT FILES and PREPROCESSING--------------------------------#

zscore_week_neigh = dict()
zscore_week_state = dict() 
zscore_week = pd.read_csv('zscore-week.csv')
for i,row in zscore_week.iterrows():
    zscore_week_neigh[str(int(row['districtid']))+'+'+str(int(row['weekid']))] = row['neighborhoodzscore']
    zscore_week_state[str(int(row['districtid']))+'+'+str(int(row['weekid']))] = row['statezscore']
    
zscore_month_neigh = dict()
zscore_month_state = dict() 
zscore_month = pd.read_csv('zscore-month.csv')
for i,row in zscore_month.iterrows():
    zscore_month_neigh[str(int(row['districtid']))+'+'+str(int(row['monthid']))] = row['neighborhoodzscore']
    zscore_month_state[str(int(row['districtid']))+'+'+str(int(row['monthid']))] = row['statezscore']

zscore_overall_neigh = dict()
zscore_overall_state = dict() 
zscore_overall = pd.read_csv('zscore-overall.csv')
for i,row in zscore_overall.iterrows():
    zscore_overall_neigh[str(int(row['districtid']))+'+'+str(int(row['overallid']))] = row['neighborhoodzscore']
    zscore_overall_state[str(int(row['districtid']))+'+'+str(int(row['overallid']))] = row['statezscore']  
  
dictZSCORE_MSW_neigh = dict()
dictZSCORE_MSW_neigh = defaultdict(lambda:[],dictZSCORE_MSW_neigh)
dictZSCORE_MSW_state = dict()
dictZSCORE_MSW_state = defaultdict(lambda:[],dictZSCORE_MSW_state)
method_spot_week = pd.read_csv('method-spot-week.csv')
for i,row in method_spot_week.iterrows():
    if row['method'] == 'neighborhood':
        dictZSCORE_MSW_neigh[str(row['weekid'])+'+'+str(row['spot'])].append \
            ([zscore_week_neigh[str(row['districtid'])+'+'+str(row['weekid'])],row['districtid']])  
    else:
        dictZSCORE_MSW_state[str(row['weekid'])+'+'+str(row['spot'])].append \
            ([zscore_week_state[str(row['districtid'])+'+'+str(row['weekid'])],row['districtid']])
for i,val in dictZSCORE_MSW_neigh.items():
    if i.split('+')[1] == 'cold':
        dictZSCORE_MSW_neigh[i].sort()
    else:
        dictZSCORE_MSW_neigh[i].sort(reverse=True)
for i,val in dictZSCORE_MSW_state.items():
    if i.split('+')[1] == 'cold':
        dictZSCORE_MSW_state[i].sort()
    else:
        dictZSCORE_MSW_state[i].sort(reverse=True)

       
dictZSCORE_MSM_neigh = dict()
dictZSCORE_MSM_neigh = defaultdict(lambda:[],dictZSCORE_MSM_neigh)
dictZSCORE_MSM_state = dict()
dictZSCORE_MSM_state = defaultdict(lambda:[],dictZSCORE_MSM_state)
method_spot_month = pd.read_csv('method-spot-month.csv')
for i,row in method_spot_month.iterrows():
    if row['method'] == 'neighborhood':
        dictZSCORE_MSM_neigh[str(row['monthid'])+'+'+str(row['spot'])].append \
            ([zscore_month_neigh[str(row['districtid'])+'+'+str(row['monthid'])],row['districtid']])          
    else:
        dictZSCORE_MSM_state[str(row['monthid'])+'+'+str(row['spot'])].append \
            ([zscore_month_state[str(row['districtid'])+'+'+str(row['monthid'])],row['districtid']])
for i,val in dictZSCORE_MSM_neigh.items():
    if i.split('+')[1] == 'cold':
        dictZSCORE_MSM_neigh[i].sort()
    else:
        dictZSCORE_MSM_neigh[i].sort(reverse=True)
for i,val in dictZSCORE_MSM_state.items():
    if i.split('+')[1] == 'cold':
        dictZSCORE_MSM_state[i].sort()
    else:
        dictZSCORE_MSM_state[i].sort(reverse=True)
    
    
dictZSCORE_MSO_neigh = dict()
dictZSCORE_MSO_neigh = defaultdict(lambda:[],dictZSCORE_MSO_neigh)
dictZSCORE_MSO_state = dict()
dictZSCORE_MSO_state = defaultdict(lambda:[],dictZSCORE_MSO_state)
method_spot_overall = pd.read_csv('method-spot-overall.csv')
for i,row in method_spot_overall.iterrows():
    if row['method'] == 'neighborhood':
        dictZSCORE_MSO_neigh[str(row['overallid'])+'+'+str(row['spot'])].append \
            ([zscore_overall_neigh[str(row['districtid'])+'+'+str(row['overallid'])],row['districtid']])          
    else:
        dictZSCORE_MSO_state[str(row['overallid'])+'+'+str(row['spot'])].append \
            ([zscore_overall_state[str(row['districtid'])+'+'+str(row['overallid'])],row['districtid']])
for i,val in dictZSCORE_MSO_neigh.items():
    if i.split('+')[1] == 'cold':
        dictZSCORE_MSO_neigh[i].sort()
    else:
        dictZSCORE_MSO_neigh[i].sort(reverse=True)
for i,val in dictZSCORE_MSO_state.items():
    if i.split('+')[1] == 'cold':
        dictZSCORE_MSO_state[i].sort()
    else:
        dictZSCORE_MSO_state[i].sort(reverse=True)
#---------------IMPORT FILES and PREPROCESSING--------------------------------#
            

#----------------------------PROCESSING WEEK----------------------------------#
weekFinalList = []
for i in dictZSCORE_MSW_neigh.items():
    tmp = []
    split = i[0].split('+')
    tmp.append(int(split[0]))
    tmp.append('neighborhood')
    tmp.append(split[1])
    c = 0
    for j in i[1]:
        c += 1
        tmp.append(j[1])
        if c == 5:
            break
    while c < 5:
        c += 1
        tmp.append('')
    weekFinalList.append(tmp)
for i in dictZSCORE_MSW_state.items():
    tmp = []
    split = i[0].split('+')
    tmp.append(int(split[0]))
    tmp.append('state')
    tmp.append(split[1])
    c = 0
    for j in i[1]:
        c += 1
        tmp.append(j[1])
        if c == 5:
            break
    while c < 5:
        c += 1
        tmp.append('')
    weekFinalList.append(tmp)
    
weekFinalList.sort()
weekFinalList.insert(0,['weekid','method','spot','districtid1', \
                        'districtid2','districtid3','districtid4','districtid5'])
out = pd.DataFrame(weekFinalList)
out.to_csv('top-week.csv',index=False,header=False)

#----------------------------PROCESSING WEEK----------------------------------#
        
        
#----------------------------PROCESSING MONTH---------------------------------#
monthFinalList = []
for i in dictZSCORE_MSM_neigh.items():
    tmp = []
    split = i[0].split('+')
    tmp.append(int(split[0]))
    tmp.append('neighborhood')
    tmp.append(split[1])
    c = 0
    for j in i[1]:
        c += 1
        tmp.append(j[1])
        if c == 5:
            break
    while c < 5:
        c += 1
        tmp.append('')
    monthFinalList.append(tmp)
for i in dictZSCORE_MSM_state.items():
    tmp = []
    split = i[0].split('+')
    tmp.append(int(split[0]))
    tmp.append('state')
    tmp.append(split[1])
    c = 0
    for j in i[1]:
        c += 1
        tmp.append(j[1])
        if c == 5:
            break
    while c < 5:
        c += 1
        tmp.append('')
    monthFinalList.append(tmp)
        
monthFinalList.sort()
monthFinalList.insert(0,['monthid','method','spot','districtid1', \
                        'districtid2','districtid3','districtid4','districtid5'])
out = pd.DataFrame(monthFinalList)
out.to_csv('top-month.csv',index=False,header=False)
#----------------------------PROCESSING MONTH---------------------------------#
        

#--------------------------PROCESSING OVERALL---------------------------------#       
overallFinalList = []
for i in dictZSCORE_MSO_neigh.items():
    tmp = []
    split = i[0].split('+')
    tmp.append(int(split[0]))
    tmp.append('neighborhood')
    tmp.append(split[1])
    c = 0
    for j in i[1]:
        c += 1
        tmp.append(j[1])
        if c == 5:
            break
    while c < 5:
        c += 1
        tmp.append('')
    overallFinalList.append(tmp)
for i in dictZSCORE_MSO_state.items():
    tmp = []
    split = i[0].split('+')
    tmp.append(int(split[0]))
    tmp.append('state')
    tmp.append(split[1])
    c = 0
    for j in i[1]:
        c += 1
        tmp.append(j[1])
        if c == 5:
            break
    while c < 5:
        c += 1
        tmp.append('') 
    overallFinalList.append(tmp)
          
overallFinalList.sort()
overallFinalList.insert(0,['overallid','method','spot','districtid1', \
                        'districtid2','districtid3','districtid4','districtid5'])
out = pd.DataFrame(overallFinalList)
out.to_csv('top-overall.csv',index=False,header=False)           
#--------------------------PROCESSING OVERALL---------------------------------#   