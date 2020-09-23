#-----------------------------------HEADERS-----------------------------------#
from collections import defaultdict
import pandas as pd
import statistics
#-----------------------------------HEADERS-----------------------------------#


#-----------------------------------------------------------------------------#
data2 = pd.read_csv('edge-graph.csv',names=['did','nid'])
dis_neigh_Dict = defaultdict(list) 
for i,row in data2.iterrows():
    dis_neigh_Dict[str(row['did'])].append(str(row['nid']))
#-----------------------------------------------------------------------------#

#--------------------------WEEK DATA FILE-------------------------------------#
id_week_Dict = dict()
data1 = pd.read_csv('cases-week.csv')
for i,row in data1.iterrows():
    id_week_Dict[str(row['districtid'])+'+'+str(row['weekid'])] = row['cases']    
track_stand_deviation = defaultdict(list)
final_id_neigh_mean = dict()
final_id_neigh_mean = defaultdict(lambda:0,final_id_neigh_mean)
for i in dis_neigh_Dict.items():
    dist_to_consider = str(i[0])
    neigh_to_consider = i[1]
    for j in range(1,26):
        entries = 0;
        for k in neigh_to_consider:
            entries += 1
            track_stand_deviation[dist_to_consider+'+'+str(j)].append(id_week_Dict[k+'+'+str(j)])
            final_id_neigh_mean[dist_to_consider+'+'+str(j)] += id_week_Dict[k+'+'+str(j)]
        final_id_neigh_mean[dist_to_consider+'+'+str(j)] /= entries
        final_id_neigh_mean[dist_to_consider+'+'+str(j)] = \
            '{0:.2f}'.format(final_id_neigh_mean[dist_to_consider+'+'+str(j)])
final_id_neigh_staDeviation = dict()
for i in track_stand_deviation.items():
    l = len(i[1])
    if l>1:
        tmpL = [float(x) for x in i[1]]
        final_id_neigh_staDeviation[i[0]] = '{0:.2f}'.format(statistics.stdev(tmpL))
    else:
        final_id_neigh_staDeviation[i[0]] = '{0:.2f}'.format(float(0))

finalWeekList = []
finalWeekList.append(['districtid','weekid','neighbormean','neighborstdev'])
for i in final_id_neigh_staDeviation.items():
    tmpList = []
    firstTwo = i[0].split('+')
    tmpList.append(firstTwo[0])
    tmpList.append(firstTwo[1])
    tmpList.append(final_id_neigh_mean[i[0]])
    tmpList.append(final_id_neigh_staDeviation[i[0]])
    finalWeekList.append(tmpList)

out = pd.DataFrame(finalWeekList)
out.to_csv('neighbor-week.csv',index=False,header=False)
#--------------------------WEEK DATA FILE-------------------------------------#   

#--------------------------MONTH DATA FILE -----------------------------------#   
id_month_Dict = dict()
data1 = pd.read_csv('cases-month.csv')
for i,row in data1.iterrows():
    id_month_Dict[str(row['districtid'])+'+'+str(row['monthid'])] = row['cases']
track_stand_deviation = defaultdict(list)
final_id_neigh_mean = dict()
final_id_neigh_mean = defaultdict(lambda:0,final_id_neigh_mean)
for i in dis_neigh_Dict.items():
    dist_to_consider = str(i[0])
    neigh_to_consider = i[1]
    for j in range(1,8):
        entries = 0;
        for k in neigh_to_consider:
            entries += 1
            track_stand_deviation[dist_to_consider+'+'+str(j)].append(id_month_Dict[k+'+'+str(j)])
            final_id_neigh_mean[dist_to_consider+'+'+str(j)] += id_month_Dict[k+'+'+str(j)]
        final_id_neigh_mean[dist_to_consider+'+'+str(j)] /= entries
        final_id_neigh_mean[dist_to_consider+'+'+str(j)] = \
            '{0:.2f}'.format(final_id_neigh_mean[dist_to_consider+'+'+str(j)])

final_id_neigh_staDeviation = dict()
for i in track_stand_deviation.items():
    l = len(i[1])
    if l>1:
        tmpL = [float(x) for x in i[1]]
        final_id_neigh_staDeviation[i[0]] = '{0:.2f}'.format(statistics.stdev(tmpL))
    else:
        final_id_neigh_staDeviation[i[0]] = '{0:.2f}'.format(float(0))

finalMonthList = []
finalMonthList.append(['districtid','monthid','neighbormean','neighborstdev'])
for i in final_id_neigh_staDeviation.items():
    tmpList = []
    firstTwo = i[0].split('+')
    tmpList.append(firstTwo[0])
    tmpList.append(firstTwo[1])
    tmpList.append(final_id_neigh_mean[i[0]])
    tmpList.append(final_id_neigh_staDeviation[i[0]])
    finalMonthList.append(tmpList)

out = pd.DataFrame(finalMonthList)
out.to_csv('neighbor-month.csv',index=False,header=False)
#--------------------------MONTH DATA FILE -----------------------------------#

#--------------------------OVERALL DATA FILE ---------------------------------#
id_overall_Dict = dict()
data1 = pd.read_csv('cases-overall.csv')
for i,row in data1.iterrows():
    id_overall_Dict[str(row['districtid'])+'+'+str(row['overallid'])] = row['cases']
track_stand_deviation = defaultdict(list)
final_id_neigh_mean = dict()
final_id_neigh_mean = defaultdict(lambda:0,final_id_neigh_mean)
for i in dis_neigh_Dict.items():
    dist_to_consider = str(i[0])
    neigh_to_consider = i[1]
    for j in range(1,2):
        entries = 0;
        for k in neigh_to_consider:
            entries += 1
            track_stand_deviation[dist_to_consider+'+'+str(j)].append(id_overall_Dict[k+'+'+str(j)])
            final_id_neigh_mean[dist_to_consider+'+'+str(j)] += id_overall_Dict[k+'+'+str(j)]
        final_id_neigh_mean[dist_to_consider+'+'+str(j)] /= entries
        final_id_neigh_mean[dist_to_consider+'+'+str(j)] = \
            '{0:.2f}'.format(final_id_neigh_mean[dist_to_consider+'+'+str(j)])

final_id_neigh_staDeviation = dict()
for i in track_stand_deviation.items():
    l = len(i[1])
    if l>1:
        tmpL = [float(x) for x in i[1]]
        final_id_neigh_staDeviation[i[0]] = '{0:.2f}'.format(statistics.stdev(tmpL))
    else:
        final_id_neigh_staDeviation[i[0]] = '{0:.2f}'.format(float(0))

finalOverallList = []
finalOverallList.append(['districtid','overallid','neighbormean','neighborstdev'])
for i in final_id_neigh_staDeviation.items():
    tmpList = []
    firstTwo = i[0].split('+')
    tmpList.append(firstTwo[0])
    tmpList.append(firstTwo[1])
    tmpList.append(final_id_neigh_mean[i[0]])
    tmpList.append(final_id_neigh_staDeviation[i[0]])
    finalOverallList.append(tmpList)

out = pd.DataFrame(finalOverallList)
out.to_csv('neighbor-overall.csv',index=False,header=False)
#--------------------------OVERALL DATA FILE ---------------------------------#