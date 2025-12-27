#statements help to perform a code or function when specific data matches with the setup data

age = int(input("Enter your age: "))

if age > 18:
    print("You are signed up!")
elif age == 18:
    print("You need to sign up parent-child agreement policy ")
elif age<0 :
    print("The given age is kinda similar to your iq")
else: 
    print("You must be 18+ to sign up")

order = input("Would you like to have something? (Y/N): ")

if order in ("Y", "y") :
    print("What would you like to have?")
else : 
    print("Okay sir")