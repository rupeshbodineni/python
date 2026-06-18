import csv
employees = [
    [1, "Moises", "mbarabisch0@so-net.ne.jp", "Male"],
    [2, "Angelika", "amearing1@discovery.com", "Female"],
    [3, "Perice", "pbindin2@pcworld.com", "Male"]
    
]
fp = open('user.csv', 'w', newline='')
csv_writer = csv.writer(fp)
csv_writer.writerow(["eid", "ename", "email", "gender"])
csv_writer.writerows(employees)
print("Employee file created successfully")