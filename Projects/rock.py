#Program for rock paper scissor game
import random

while True:
    print("Program for rock paper scissor game\n")

    options = ["rock", "paper", "scissor"]
    choice = input("Enter one among rock, paper, and scissor: ").lower()
    user_choice = choice

    computer_choice = random.choice(options)
    print(f"Computer choose {computer_choice}")

    if user_choice == 'rock' and computer_choice == 'paper':
        print("You lost to a computer")
    elif user_choice == 'rock' and computer_choice == 'scissor':
        print("You won")
    elif user_choice == 'scissor' and computer_choice == 'paper':
        print("You won")
    elif user_choice == 'paper' and computer_choice == 'rock':
        print("You won")
    elif user_choice == 'paper' and computer_choice == 'scissor':
        print("You lost to the computer")
    elif user_choice == 'scissor' and computer_choice == 'rock':
        print("You lost to the computer")
    elif user_choice == computer_choice:
        print("It's a draw")
    else:
        print("Invalid input")

    response = input("do you want to continue?(y/n): ").lower()
    if response == 'y':
        print("Okay")
    else:
        break
