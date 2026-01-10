# price1 = 3.14159
# price2 = -987.555
# price3 = 12.3444

# # print(f"Price 1 is ${price1:10}")
# # print(f"Price 2 is ${price2: 0.2f}")
# # print(f"Price 3 is ${price3: 0.3f}")

# amount = float(input("Enter the amount: "))
# print(f"the transaction of ${amount: ,.2f} is done.\n The amount ${amount: 0.2f} will be deducted from your account")

count = 0
even = 0
odd = 0

while True:
    num = int(input("Enter a number (0 to stop): "))

    if num == 0:
        break

    count += 1

    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Total numbers:", count)
print("Even numbers:", even)
print("Odd numbers:", odd)
