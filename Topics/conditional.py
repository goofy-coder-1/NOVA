# Conditional expression  = A one line shortcut for the if-else statement (teranary operator)
# Print or assign one of the two values based on a condition
# X if (condition) ele Y

age = int(input("Enter your age: "))
print("You are a minor" if age < 18 else "You are signed up!")

num = float(input("Enter your number: "))
print("The number is even" if num % 2 ==0 else "the number is odd")

role = input("Enter your role: ")
print("Full Access" if role in ("Admin", "admin", "ADMIN") else "limited access")