#program to check usernames availablity

print("Program written to find out the username availability")

usernames_not = ["Ujjwal", "Saurabh", "Aakash", "Bhadra", "bahun"]

while True:
      name = input("Enter your name: ").capitalize()
      if len(name) < 6 or len(name) > 15:
            print("name can't be less than 6 character and more than 15")
      elif any(char.isdigit() for char in name):
            print("digit is not allowed in name")
      elif name.isspace():
            print("Space is not allowed") 
      elif not name[0].isalpha():
            print("name must begin with a letter")
      elif name in usernames_not:
            print("Name is already taken, get another one")
      else:
            print(f"Welcome {name}")
            break
      
      
print("You are set up")