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
    "Ujjwal": {"grade": "bachelor", "age": "20"}
}

response = input("What do you like to know about the student?: ").lower()

match response:
    case "grade":
        for hello_key, hello_value in student.items():
            print(f"The student is in {hello_value['grade']}")
    case "age":
        for hello_key, hello_value in student.items():
            print(f"The student is {hello_value['age']}")