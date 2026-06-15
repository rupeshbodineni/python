employees = [ 
    {"eid": 1, "ename": "Shah Rukh Khan", "gender": "Male", "age": 59}, 
    {"eid": 2, "ename": "Deepika Padukone", "gender": "Female", "age": 38}, 
    {"eid": 3, "ename": "Amitabh Bachchan", "gender": "Male", "age": 82}, 
    {"eid": 4, "ename": "Priyanka Chopra", "gender": "Female", "age": 42}, 
    {"eid": 5, "ename": "Aamir Khan", "gender": "Male", "age": 59}, 
    {"eid": 6, "ename": "Kareena Kapoor", "gender": "Female", "age": 44}, 
    {"eid": 7, "ename": "Salman Khan", "gender": "Male", "age": 59}, 
    {"eid": 8, "ename": "Katrina Kaif", "gender": "Female", "age": 41}, 
    {"eid": 9, "ename": "Hrithik Roshan", "gender": "Male", "age": 50}, 
    {"eid": 10, "ename": "Alia Bhatt", "gender": "Female", "age": 31}, 
    {"eid": 11, "ename": "Akshay Kumar", "gender": "Male", "age": 57}, 
    {"eid": 12, "ename": "Kangana Ranaut", "gender": "Female", "age": 37}, 
    {"eid": 13, "ename": "Ranbir Kapoor", "gender": "Male", "age": 42}, 
    {"eid": 14, "ename": "Vidya Balan", "gender": "Female", "age": 46}, 
    {"eid": 15, "ename": "Ranveer Singh", "gender": "Male", "age": 39}, 
    {"eid": 16, "ename": "Anushka Sharma", "gender": "Female", "age": 36}, 
    {"eid": 17, "ename": "Rajinikanth", "gender": "Male", "age": 74}, 
    {"eid": 18, "ename": "Aishwarya Rai", "gender": "Female", "age": 51}, 
    {"eid": 19, "ename": "Vijay", "gender": "Male", "age": 50}, 
    {"eid": 20, "ename": "Madhuri Dixit", "gender": "Female", "age": 57} 
]

# for employee in employees:
#     print(employee)

# for employee in employees:
#     if employee["age"]>50:
#         print(employee)

# count=0
# for employee in employees:
#     if employee["gender"]=="Male":
#         count+=1
# print("total number of male employees:",count)



# count=0
# for employee in employees:
#     if employee["gender"]=="Female":
#         count+=1
# print("total number of female employees:",count)

# print(len(employees))

# for employee in employees:
#     if employee["age"]==59:
#         print(employee)

# for employee in employees:
#     if employee ["age"]<40:
#         print(employee["ename"])

# for employee in employees:
#     if  30<=employee["age"]>50:
#         print(employee["ename"])

# for employee in employees:
#     if employee["gender"]=="Female":
#         print(employee["ename"],employee["age"])

# for employee in employees:
#     if employee["gender"]=="Male":
#         print(employee["ename"],employee["age"])

# for employee in employees:
#     if employee["ename"].startswith("A"):
#         print(employee["ename"])


# for employee in employees:
#     if employee["ename"].endswith("r"):
#         print(employee["ename"])


# for employee in employees:
#     if employee["age"]>=60:
#         print(employee["ename"],"-Senior Employee")
#     else:
#         print(employee["ename"],"-Regular Employee")

for employee in employees:
    if employee["age"]<40:
        print(employee["ename"],"-young")
    elif 40<=employee["age"]<59:
        print(employee["ename"],"-Middled aged")
    else:
        print(employee["ename"],"-Senior")