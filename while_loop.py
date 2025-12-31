#while loop = execute some code while some condition remains true

name = input("Enter your name: ")

while name == "":
    print("You did not enter your name!")
    name = input("Enter your name: ")
print(f"Hello {name}")


food = input("Enter the food you like: ")

while not food == "q":
    print(f"{food} is not on our menu, order something else")
    food = input("Enter the food you like: ")

print("Bye sir")
    