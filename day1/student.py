marks = []

for i in range(5):
    marks.append(float(input(f"Enter marks {i+1}: ")))

total = sum(marks)
percentage = total / 5

print("Percentage:", percentage)

if percentage >= 90:
    print("Grade A")
elif percentage >= 75:
    print("Grade B")
elif percentage >= 50:
    print("Grade C")
else:
    print("Fail")