import random
import sys
print(sys.executable)

fruits = [
    "apple",
    "banana",
    "pineapple",
    "mango",
    "orange",
    "grape",
    "watermelon",
    "papaya",
    "guava",
    "blueberry",
    "blackberry",
    "strawberry",
    "kiwi",
    "pear",
    "peach",
    "plum",
    "pomegranate",
    "coconut",
    "apricot",
    "dragonfruit",
    "lychee",
    "cherry",
    "fig",
    "date",
    "avocado"
]

word = random.choice(fruits)

letters = list(word)
random.shuffle(letters)
scrambled = "".join(letters)

attempts = 5

while attempts > 0:
    print(f"Can you guess what fruit is this?: {scrambled}")
    guess = input(f"Your Guess: ")

    if guess.lower() == word:
        if attempts == 5:
         print(f"{guess} was right")
         print(f"Bravo! guess in first attempt")
        else:
         print(f"{guess} was right")
         print(f"unscrambled it while {attempts} attempts left")
        break
    else:
        attempts -= 1
        print(f"{guess} is not right")
        print(f"{attempts} attempts left")
        
print("--------Result---------")

if attempts == 0:
    print(f"\nGame Over. The word was: {word}")

score = attempts * 20
print(f"Your score is {score}")

print("-----------------------")



