menu = {
    "chips" : 5.99,
    "nacho" : 5.10,
    "burrito": 4.50,
    "momo" : 10.00,
    "soda": 2.99
}

list = []
total = 0

for key, value in menu.items():
    print(f"{key}: ${value:.2f}")
print("-------------------------")

while True:
    food = input("Enter the food you want to order(q to quit): ").lower().strip()
    if food == "q":
        break
    elif menu.get(food) is not None:
        list.append(food)
print("-------Your Order--------")
for food in list:
    total += menu.get(food)
    print(food, end= " \n")

print()
print(f"Your total is ${total}")