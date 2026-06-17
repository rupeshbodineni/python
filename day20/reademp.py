import json
fp=open('emp.json','r')
employees=json.load(fp)
print(type(employees))
for employee in employees:
    print(employee['ename'])

for employee in employees:
    if employee['gender']=="Male":
        print(employee)

Female_count=0
for employee in employees:
    if employee['gender']=="Female":
        Female_count+=1
print("no of female employees :",Female_count)

