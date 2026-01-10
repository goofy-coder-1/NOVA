print("Program to validate your password")
password = input("Enter your password: ")

score = 0
failed = 0

is_length = False
has_lower = False
has_digit = False
has_special = False
has_upper = False

# length check (outside loop)
if len(password) >= 10:
    is_length = True

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    else:
        has_special = True

if has_upper:
    score += 1
else:
    failed += 1

if has_digit:
    score += 1
else:
    failed += 1

if has_lower:
    score += 1
else:
    failed += 1

if is_length:
    score += 1
else:
    failed += 1

if has_special:
    score += 1
else:
    failed += 1

if failed == 0:
    print("Password fulfilled all conditions ")
else:
    print(f"Your password didn't match {failed} conditions\n")

print(f"Your total score is {score}")

if score <= 2:
    print("Your password is weak ")
elif score >= 4:
    print("Your password is strong as fuck")
else:
    print("Meh")
