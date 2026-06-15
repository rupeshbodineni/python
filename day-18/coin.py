import random
coin_result = ["head", "tails"]
head_count = 0
tails_count = 0
for i in range(100):
    result = random.choice(coin_result)      
    if result == "head":
        head_count += 1
    else:
        tails_count += 1
print("number of head count =", head_count)
print("number of tail count =", tails_count)