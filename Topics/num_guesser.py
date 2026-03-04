import random

print("The program to let you guess random number")
actual = random.randint(1, 100)

while True:
    try:
        guess = int(input("Enter the number: "))
    except ValueError:
        print("Enter a valid number")
        continue

    if guess == actual:
        print(f"BRAVO! {guess} was the right number")
        break
    elif guess > actual:
        print("The number guessed is greater than actual number")
    elif abs(guess - actual) <= 5:
        print("The guessed number is close to actual number")
    else:
        print("The guessed number is less than actual")

    