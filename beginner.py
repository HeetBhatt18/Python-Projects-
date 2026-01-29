import random

number = random.randint(1, 10)
guess = None

print("Guess a number between 1 and 10")

while guess != number:
    guess = int(input("Enter your guess: "))

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("🎉 Correct! You guessed the number.")
