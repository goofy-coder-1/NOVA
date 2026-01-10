# #shopping cart program

# foods = []
# prices = []
# total = 0

# while True: 
#     food = input("Enter a food to buy (q to quit): ")
#     if food.lower() == "q":
#         break
#     else:
#         price = float(input(f"Enter the price of {food}: $"))
#         foods.append(food)
#         prices.append(price)

# print("----- YOUR CART -----")

# for food in foods: 
#     print(food, end= " ")

# for price in prices:
#    total += price


students = []
grades = []
total = 0

while True:
      student =  input("Enter the name of the students (q to quit): ")
      if student.lower() == "q":
         print("Have a good day!")
         break
      else: 
         grade = float(input("Enter the gpa of student: "))
         students.append(student)
         grades.append(grade)

print("-----The combined average gpa-----")

for student in students:
    print(student)

for grade in grades: 
    total += grade

print(f"The total gpa of students is {total}")