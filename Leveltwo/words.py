import random
fruits = ["apple", "banana", "pineapple", "guava", "blueberry", "blackberry", "orange", "coconut", "peanut"]

word = random.choice(fruits)

letters = list(word)
random.shuffle(letters)
scrambled = "".join(letters)

print(f"what might be this fruit?: {scrambled}")

user_guess = []
total = 0

correct = []
incorrect = []

choice = int(input("How many guesses you want to enter?: "))

for guess in range(choice):
    name = input("Enter the name of fruit: ").lower()
    user_guess.append(name)

for items in user_guess:
   if items in fruits:
       print(f"{items} is correct")
       total += 1
       correct.append(items)
   else:
       print(f"{items} is incorrect")
       incorrect.append(items)

print(f"You found {total} correct items")
print("----------correct----------")
for j in correct:
    print(j)
print("----------incorrect----------")
for k in incorrect:
    print(k)