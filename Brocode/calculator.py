
operator = input("Enter an operator (+ - * /): ")

number_first = int(input("Enter the first number: "))
number_second = int(input("Enter the first number: "))

match operator:
    case '+':
        result = number_first+number_second
        print(f"The sum of two number is {result}")
    case '-':
        result = number_first-number_second
        print(f"The sum of two number is {result}")
    case '*':
        result = number_first*number_second
        print(f"The sum of two number is {result}")
    case '/':
        if number_second == 0:
            print("can't divide by zero")
        else:
           result = number_first/number_second
           print(f"The sum of two number is {result}")
    case _:
        print("Invalid")