import random

print("Welcome to the Number Guessing Game!")
secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = input("Guess a number between 1 and 100: ")
    try:
        guess = int(guess)
        attempts += 1
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} tries.")
            break
    except ValueError:
        print("Please enter a valid number.")
    