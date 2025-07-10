import random

print("Guess the number! You will have 10 chances to guess, please continue!")

low = int(input("Enter lowest number in range:"))
high = int(input("Enter highest number in range:"))

print(f"\nYou have 10 chances to guess the correct number between {low} and {high}. Good luck!")

num = random.randint(low, high)
gu = 10                         #Total number of allowed guesses
gc = 0                          # Guess count

while gc < gu:
    gc += 1
    guess = int(input("What is your guess?: "))

    if guess == num:
        print(f"Congrats! You guessed the correct number {num}! You got this in {gc} attempts!")
        break

    elif gc >= gu and guess != num:
        print(f"Sorry! The number was {num}. Try again!")

    elif guess > num:
        print("Too high!")

    elif guess < num:
        print("Too low!")


