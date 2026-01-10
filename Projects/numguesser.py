#code to generate a number and let user guess it
import random
import math
import time

print("Program for number guessing")
actual = random.randint(1, 10)

while True:
    guess = input("Enter your guess: ")
     
    if not guess.isdigit():
        print("Input must be digit")
        continue

    if len(guess) > 2:
        print("Input can't be greater than two")
        continue

    guess = int(guess)

    if guess == actual :
        print("Analyzing number")
        time.sleep(1.5)
        print("Additional confirmation")
        time.sleep(1.5)
        print("backend verification")
        time.sleep(1.5)
        print(f"BRAVO! {guess} is the right number")
        break
    elif guess > actual:
        print("The guess is greater than actual")
    elif guess < actual:
        print("The guess is less than actual")
    else:
        "Invalid Input"