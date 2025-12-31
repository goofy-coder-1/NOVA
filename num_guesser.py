#Random number guesser
import math
import random

print("The program to let you guess random number")
actual = random.randint(1, 100)

while True:
      response = input("Do you want to continue? (q to quit): ")
      if response.lower() == "q":
            print("Have a good day!")
            break
      else: 
            guess = int(input("Enter the number: "))
            if guess > 2*actual :
                print("The number guessed is skylining")
            elif guess > actual: 
                print("The number guessed is greater than actual number")
            elif guess == actual-5:
                print("The guessed number is close to actual number")
            elif guess < actual:
                print("The guessed number is less than actual")
            elif guess == actual:
                print(f"BRAVO! {guess} was the right number")
                break
            else:
                print("Invalid response")

    