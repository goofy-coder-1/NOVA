#Typecasting is the process of converting one datatype to another
#str(), int(), float(), bool()
#specially useful for user inputs

name = "Ujjwal Rana"
age = 20
price = 2.99
is_Online = True

#function to find out the variable type
print(type(age))


#function to covert one datatype to another
price = float(int(float(price)))
print(price)

age = str(age)
age += "1" #(this works because line 18 has converted int into a string and putting 1 inside quotation also
print(age) # makes it a string, remove quotation and it throws error)

#typecasting string into intger is not possible since compiler throws an error
#name = int(name)
#print(name)  -> This simply throws error because it is simply not possible to convert characters into numbers

#but we can do this with boolean though, which is quite useful to find out if someone left the input empty or not
name = bool(name)
print(name)

bool("")   # False
bool(" ")  # True
bool(0)    # False
bool(42)   # True