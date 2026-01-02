# A simple program written to validate username

print("Let's see your username")
print("-----------------------")
print("username must not contain\n" \
     "1. space or be empty\n"
     "2. only digits\n"
     "3. first letter as lowercase")
print('------------------------')


while True:
    username = input("Enter your username: ")
    if username.isdigit():
        print("username can't have digit")
    elif username.isspace():
        print("username must not be empty")
    elif not username[0].isupper():
        print("First letter must be capital")
    elif not username.find(" ") == -1:
        print("username must not have space")
    elif len(username) > 12:
        print("username can't be longer than 12 characters.")
    elif len(username) < 6:
        print("username can't be less than 6 characters.")
    else: 
        print(f"Welcum {username}\n"
              f"You are signed up!")
        break