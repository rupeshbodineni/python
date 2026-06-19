import csv
import json
fp1=open('user.csv','r')
csv_reader=csv.reader(fp1)
users=list(csv_reader)
print(len(users))
emp_data=[]
for emp in emp_data:
    emp_data.append({"id":users[0],
                     "name":users[1],
                     "gender":users[2]
                          })
fp2=open('emp.json','w')
json.dump