# We will learn about python function in this file
#A function is a block of code which only runs when it is called
# A function can return data as a result 
# Majorly used to avoid code repetation 

# instead of this
# temp1 = 77
# celsius1 = (temp1 - 32) * 5 / 9
# print(celsius1)

# temp2 = 95
# celsius2 = (temp2 - 32) * 5 / 9
# print(celsius2)

# temp3 = 50
# celsius3 = (temp3 - 32) * 5 / 9
# print(celsius3)

# # we can do this

# def temp_conversion(fahrenheit):
#     return(fahrenheit-32) *5/9

# print(temp_conversion(77))
# print(temp_conversion(95))
# print(temp_conversion(50))

# def get_greetings():
#     print("hello world")

# message = get_greetings()
# print(message)

# def my_name(name = "GivenName", last_name= "Surname"):
#     print(name + " " + last_name)

# my_name("Ujjwal", 'Rana')
# my_name("Aakash", "Thapa")
# my_name("Hari bahadur", "magar")
# my_name()

# def my_function(country = "Nepal"):
#   print("I am from", country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")

# def animal_name(name):
#     print(f"I have a dog and its name is {name}")

# while True:
#  response = input("What is the name of your pet?: ")
#  if response.find(" ") == -1:
#     print("No spaces allowed")
#  elif response.isspace():
#     print("Invalid")
#  else:
#     animal_name(response)
#     break

# def fruit_function():
#     return["Kera", "Suntala", "Anar"]

# fruits = fruit_function()
# print(fruits[3])

# def my_function():
#   return (10, 20)

# x, y = my_function()
# print("x:", x)
# print("y:", y)

# def add_function(x, y):
#   print("The sum of two number is", x+y)

# def sub_function(x, y):
#   print("The difference of two number is", x-y)

# def div_function(x, y):
#   print("The division of two number is", x/y)

# def mul_function(x, y):
#   print("The product of two number is", x*y)

# x = float(input("Enter the first number: "))
# y = float(input("Enter the second number: "))

# while True:
#   response = input("What operation would like to perform?(-, +, *, /): ")
#   if response == "+":
#     add_function(x, y)
#     break
#   elif response == "-":
#     sub_function(x, y)
#     break
#   elif response == "/":
#     div_function(x, y)
#     break
#   elif response == "*":
#     mul_function(x, y)
#     break
#   else:
#     print("Invalid input")

# def my_name(* ,name):
#     print("Hello", name)

# my_name(name = "Ujjwal")

#one thing you should know is that positional arguments and keyword arguments matter a lot
#You can't use function(keyword_argument, positional_argument)
#argument passing must first begin wiht positional argument

# def greeting_function(greeting, *name, age = "18"):
#     for person in name:
#      if isinstance(person, dict):
#        print(greeting, person['name'], "you are", person['age'])
#      else:
#        print(greeting, person, "You are", age)

# greeting_function("Hello", {'name':"ujjwal", "age": "19"}, "saurabh")

# Create an empty list to store the inputs
a = []

# Ask the user for how many items they want to input
b = int(input("How many items do you want to enter? "))

# Loop to collect multiple inputs
for i in range(b):
    val = input(f"Enter item {i + 1}: ")
    a.append(val)


for i in a:
    print(i)