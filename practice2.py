# for n in range(2, 20):
#     for x in range(2, n):
#         if n % x == 0:
#             print(f"{n} equals {x} * {n/x}")
#             break

# for n in range(3, 33):
#         if n % 2 == 0:
#             print("found even number")
#             continue
#         else:
#             print("found odd number")

student = {
    "ujjwal": {"grade": "bachelor", "age": "20"},
    "aayush": {"grade": "undergrad", "age": "19"}
}

while True:
    response = input("Which student are you searching for?: ").lower().strip()

    if response in student:
        print("student found here")
        print("----------------")
        print(f"Grade: {student[response]['grade']}")
        print(f"Age: {student[response]['age']}")
        print("----------------")
    else:
        print("Student not found")

    choice = input("You want to do this again?(y/n): ").lower()
    if choice != 'y':
        print("Bye Fam")
        break