#statements help to perform a code or function when specific data matches with the setup data

# name = input("What's your name??: ")

# if name.isdigit():
#     print("Name can't be in digit or capitalized!")
# else: 
#     print(f"Welcome {name}")

# age = int(input("Enter your age: "))

# if age >= 18:
#     print("You are signed up!")
# elif age < 18:
#     print("Parents approval is needed")
# else: 
#     print("Invalid response")

# words = ["vehicle_man", "valve", "yellow"]

# for v in words:
#     print(v, len(v))

#The bottom python code is copied from documentation

users = {"hans": "active", 
         "saurabh": "active",
           "Aakash": "inactive",
             '景太郎': 'active'}

for user, status in users.copy().items():
    if status == "inactive":
        del users[user]

active_users = {}
for user, status in users.items():
    if status == "active":
        active_users[user] = status

print(active_users)