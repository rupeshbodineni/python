import csv
fp=open('emp.csv','r')
emp_data= list(csv.reader(fp))
employees=list(emp_data)

# for employee in employees[1:]:
#      print(employee[1])


# for employee in employees[1:]:
#     if employee[3]=="Female":
#      print(employee[1])

# for employee in employees:
#     if employee["eid"]=="10":
#         print(employee)

# for employee in employees:
#     print(employee["ename"])


# for employee in employees:
#     if employee["gender"]=="Female":
#      print(employee["ename"]) 

# print(type(employees))

