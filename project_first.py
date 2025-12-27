# #This is a basic program to calculate the area of rectangle

print("Welcome\nLet's find out the area of rectangle")

length = float(input("Enter the length of rectangle: "))
width = float(input("Enter the width of rectangle: "))

Area = length * width
print(f"The total Area of rectangle is {Area} cm²")

#Now comes the program for shopping cart

item = input("What would you like to buy?: ")
price = float(input("What is the price of each?: "))
quantity = int(input("How many of these would you like to buy?: "))

total = price * quantity

print(f"You bought {quantity}x{item}/s")
print(f"Your total is : ${total}")

#program written to find out the area of circle

print("Find out the area of circle\n")
pi = 3.14159
radius = int(input("Enter the radius of circle: "))

area = pi * radius
print(f"The total area of circle is {area} cm²")