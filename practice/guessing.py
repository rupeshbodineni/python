import random
secret=random.randint(1,100)
guess=int(input("Enter a number:"))
if guess>secret:
    print("high")
elif guess<secret:
    print("low")
else:
    print("correct number guessed")
  