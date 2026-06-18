import json
import csv
fp1=open('emp.json','r')
employees=json.load(fp1)
print(type(employees))
female_employees=[]
for emp in employees:
    