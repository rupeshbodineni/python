import csv
import json
fp1=open('user.csv','r')
csv_reader=csv.reader(fp1)
users=list(csv_reader)
print(len(users))