import random
number = random.randint(1, 100)
while True:
    guess=int(input("Enter your guess(1-100):"))
    if guess>number:
        print("Too high!")
    elif guess<number:
        print("Too low!")
    else:
        print("Congratulations! You guessed the number.")
        break