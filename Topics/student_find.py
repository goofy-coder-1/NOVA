print("Welcome to Student Database")

print("This program will help you to find out the student you are searching for.\n")
response = input("Enter the name of student: ").lower()

delta = ["hari", "krisna", "jaya"]
mega = ["bishow", "shankar", "Ryzen"]
omega = ["ujjwal", "shiva", "doraemon"]

if response in delta:
    print(f"the student {response} is found in the database delta")
elif response in mega :
    print(f"the student {response} is found in the database mega")
elif response in omega:
    print(f"the student {response} is found in the database omega")
else: 
    print("The student was not found")