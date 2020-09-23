import csv
import pandas as pd

'''with open("cases-overall.csv", "rb") as f:
    csvreader = csv.reader(f, delimiter=",")
    c = 0
    for row in csvreader:
        if "0" in row[2]:
            c = c+1
print(c)'''

with open("districts.csv", "rb") as f:
    data = pd.read_csv("districts.csv")
    c = 0
    for i,row in data.iterrows():
        c = c + row['Confirmed']
print(c)
