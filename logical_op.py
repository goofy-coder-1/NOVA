#logical operators = evaluate multiple conditions (or, and, not)
# or = at least one condition must be true
# and = both condition must be true
# not = inverts the condition (not False, not True)

age = 17
is_adult = True

if age < 18 or age > 25 or is_adult:
    print("The party is cancelled")
else:
    print("Let's hop on the car")

temp = 20
is_sunny = False

if temp >= 25 and not is_sunny: 
    print("we will be going outside")
else: 
    print("We will stay inside today")