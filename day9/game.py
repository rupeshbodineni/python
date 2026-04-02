import random

number = random.randint(1, 50)

while True:
    guess = int(input("Enter your guess (1-50): "))

    if guess > number:
        print("Too High")
    elif guess < number:
        print("Too Low")
    else:
        print("Correct! You guessed the number.")
        break