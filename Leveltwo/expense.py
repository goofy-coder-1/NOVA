# Program for expense tracker

print("Program to track your expenses\n")
print("Through this program, we will help you track your expenses\n")

# Items database
items = {
    "apple": {"Price": 200, "Group": "Fruit"},
    "banana": {"Price": 2200, "Group": "Fruit"},
    "matcha": {"Price": 2000, "Group": "Fruit"},
    "date": {"Price": 2500, "Group": "Fruit"},
    "chocolate": {"Price": 100, "Group": "Fruit"},
    "pizza": {"Price": 20000, "Group": "Fruit"},
    "burger": {"Price": 200, "Group": "Fruit"},
    "snacks": {"Price": 1500, "Group": "Fruit"}
}

salaries = []
savings = []

while True:
    response = input("Are you ready? (yes/no): ").strip().lower()
    if response == 'no':
        print("Closing Program")
        break

    # Get salary and savings
    try:
        salary = int(input("Enter your salary: "))
        saving = int(input("Amount you would like to save from your salary: "))
    except ValueError:
        print("Please enter valid numbers!")
        continue

    salaries.append(salary)
    savings.append(saving)

    total_available = salary - saving
    print(f"Money available after saving: {total_available}\n")

    # Record expenses for this entry
    expenses = []  # reset for each run
    while True:
        spent_on = input("Enter an item you spent money on (q to end listing): ").strip().lower()
        if spent_on == 'q':
            break
        expenses.append(spent_on)

    if not expenses:
        print("No expenses recorded.")
        continue

    print("\nYour expenses list:", expenses)

    # Calculate total price of expenses
    total_price = 0
    for item in expenses:
        if item in items:
            price = items[item]["Price"]
            total_price += price
            print(f"{item} costs {price}")
        else:
            print(f"{item} not found in items list")

    print(f"\nTotal price of recorded expenses: {total_price}")

    # Check if expenses exceed available money
    remaining = total_available - total_price
    if remaining < 0:
        print(f"\nYour expenses exceed your available money by {-remaining}, used from your savings")
    else:
        print(f"Your remaining money after expenses: {remaining}")
        print("Your savings are safe")

    # Ask if the user wants to quit
    choice = input("\nDo you want to quit? (y/n): ").strip().lower()
    if choice == 'y':
        print("Bye Bye")
        break
    print("\n--- Next Entry ---\n")
