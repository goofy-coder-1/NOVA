#Login format code

print("--------------------")
print("-----Login Page-----")
print("--------------------")


while True:
    name = input("Enter your username: ")

    if name.isdigit():
        print("username can't be digit only")
    elif name.isspace():
        print("Name must not be empty")
    elif not name[0].upper():
        print("first letter must be capital")
    elif len(name) > 12:
        print("username can't be longer than 12 characters.")
    elif len(name) < 6:
        print("username can't be less than 6 characters.")
    else : 
        print("Username stored!")
        break

while True:
    password = input("Enter your password: ")
    if password.isdigit():
        print("password can't be digit only")
    elif password.isspace():
        print("Password must not be empty")
    else : 
        print("Password stored!")
        break

while True:
    PIN = input("Enter OTP: ")
    if not PIN.isdigit():
        print("PIN must be digit only")
    elif not len(PIN) == 4:
        print("PIN contains only four number")
    else: 
        print("PIN stored")
        break

