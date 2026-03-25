print("Calculator Program")
print("------------------")

def addfunction(number_first, number_second):
    result = number_first + number_second
    print(f"The sum of given two numbers is: {result}")
    return result

def subfunction(number_first, number_second):
    result = number_first - number_second
    print(f"The subtraction of given two numbers is: {result}")
    return result

def mulfunction(number_first, number_second):
    result = number_first * number_second
    print(f"The multiplication of given two numbers is: {result}")
    return result

def divfunction(number_first, number_second):
    if number_second == 0:
        print("Invalid to divide by zero")
        return None
    result = number_first / number_second
    print(f"The division of given two numbers is: {result}")
    return result

while True:
    try:
        number_first = int(input("Enter the first number: "))
        choice = input("Enter the operation (+, -, *, /) or 'q' to quit: ")

        if choice.lower() == 'q':
            print("Exiting calculator...")
            break

        number_second = int(input("Enter the second number: "))

        match choice:
            case '+':
                addfunction(number_first, number_second)
            case '-':
                subfunction(number_first, number_second)
            case '*':
                mulfunction(number_first, number_second)
            case '/':
                divfunction(number_first, number_second)
            case _:
                print("Invalid operation selected")

    except ValueError:
        print("Invalid input! Please enter valid integers.")