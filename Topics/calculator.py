#calculator program based on python 

print("Use this to do arithmetic operations")

number_first = float(input("Enter your first number: "))
number_second = float(input("Enter your second number: "))
sign = input("What would you like to do with these numbers? (+, -, /, *): ")

#for addition
if sign == "+" :
    result = number_first+number_second
    print(f"The total sum of these numbers is: {round(result, 4)}")
elif sign == "-":
    result= number_first-number_second
    print(f"The difference between these number is: {round(result, 4)}")
elif sign == "*":
    result = number_first*number_second
    print(f"The product of these two numbers is: {round(result, 4)}")
elif sign == "/":
    if number_second==0:
        print("The result is undefined")
    else: 
         result = number_first/number_second
         print(f"The first num divided by second is: {round(result, 2)}")

else: 
    print(f"{sign} sign is invalid")