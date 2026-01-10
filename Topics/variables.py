#let's learn about variables

#first, we will learn about strings
#Strings are set of characters that forms words and then sentences
#below are some of the examples

name = "Breezy"
food = "Momo"
email = "Breezy23@gmail.com"

print(f"Hello {name}")
print(f"Do you like {food}?")
print(f"I think your email is {email}")

#now we have Integers
#whole numbers
#Integer should not be inside quote cause that makes it a string

age = 1000
quantity = 50
rating = 10

print(f"The seminar had {quantity} students whose total age combined would reach the age of {age} (I know sounds weird)."
      f" \nThey all gave the seminar rating of {rating}.")

#here comes Float
#float is kinda same as integer but it consists of decimal portion
#the quote rule for float is same as integer

Price = 9.99
black_friday = 24.99

print(f"There was a black friday sale which offered discount of {black_friday},"
      f"and we got stuff just for {Price}.")


#then comes boolean
#it just have two condition (true or False)
#booleans are really useful in decision making

isStudent = True
issale =  False

print(f"Are you a student?: {isStudent}")

if issale : 
    print(f"{food} is not for sale")
    
else: 
    print(f"{food} is on sale")

