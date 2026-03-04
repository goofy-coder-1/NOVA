
student_list = []

print("--- Student GPA Entry System ---")

while True:
    # Get the name from the user
    name = input("Enter Student Name: ")
    
    # Get the GPA and handle potential errors (like typing letters instead of numbers)
    try:
        gpa_input = input(f"Enter GPA for {name}: ")
        gpa = float(gpa_input) # Converts the string input to a decimal number
        
        
        student_list.append({"name": name, "gpa": gpa})
        print(f"Successfully added {name}.\n")
        
    except ValueError:
        print("Error: Please enter a valid number for the GPA (e.g., 3.5).\n")

    choice = input("Do you want to continue?(y/n): ").lower()
    if choice != 'y':
        print("Bye Bye ")
        break

# Display the final results
print("\n--- Final Student List ---")
for student in student_list:
    print(f"Student: {student['name']} | GPA: {student['gpa']}")
