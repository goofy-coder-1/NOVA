
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
while True:
    print("------Student Search----------")
    student_name = input("Enter the name of the student: ")

    found = False

    for student_value in student_list:
        if student_value["name"].lower() == student_name.lower():
            print(f"Student found: {student_value['name']} | GPA: {student_value['gpa']}")
            found = True
            break

    if not found:
        print("Student not found")

    choice = input("Do you want to continue? (y/n): ").lower()
    if choice != 'y':
        print("Bye Bye")
        break

delete = input("Enter the name of the student you want to delete: ")

found = False

for student in student_list:
    if student["name"].lower() == delete.lower():
        student_list.remove(student)
        print(f"{delete} has been removed.")
        found = True
        break

if not found:
    print("Student not found.")

print(student_list)