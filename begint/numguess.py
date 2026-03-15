import random
import time

print("Program to guess number\n")

customize = input("Do you want to customize range?(y/n): ").lower()
if customize == 'y':
    try:
       a = int(input("Enter the first number for range: "))
       b = int(input("Enter the second number for range: "))
       actual = random.randint(a, b)
    except ValueError:
        print("Invalid input")
        exit()
else:
    actual = random.randint(1, 100)

level = int(input("Choose difficulty level(1, 2, 3, 4): \n" \
"1. Easy (guess in 15 attempts)\n2. Intermediate (guess in 10 attempts)\n3. Hard (Guess in 5 attempts)\n4. Insane (Guess in three attempts): "))

if level == 1:
    attempt = 15
elif level == 2:
    attempt = 10
elif level == 3:
    attempt = 5
elif level == 4:
    attempt = 3
else:
    print("Invalid Input")
    exit()

time.sleep(2)
print("Okay the game begins")
time.sleep(1)
print("--------Game---------")

while attempt > 0:
    guess = int(input("Enter the guess number: "))

    if guess == actual:
        print("Bravo! You got it!")
        print("Attempts left:", attempt)
        break

    elif guess < actual:
        print("Number is higher")

    else:
        print("Number is lower")

    attempt -= 1
    print("Attempts left:", attempt)

if attempt == 0:
    print("Game over! The number was:", actual)

