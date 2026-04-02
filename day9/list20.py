
import random

numbers=[11,7,8,18,31,1055,232,99,199,101,201,301,401,501,601,701,801,901,1001,757]

print(len(numbers))

selected_numbers = random.choices(numbers, k=5)

print(selected_numbers)