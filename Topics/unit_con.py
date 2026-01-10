#program for unit conversion

print("Program written for Unit conversion")

response = input("What do you want to convert?\n"
                 f"pounds to kilogram or vice versa -> type A\n"
                  f"kilometer to miles or vice versa -> type B\n"
                   f"Celsius to fahrenheit or vice versa -> type C\n"
                   f"A/B/C?: ")

#function for weight conversion
if response in ("A", "a") :
   weight = float(input("Enter the weight: "))
   intent = input("What do you want to convert given weight into, pounds or kilogram? (P/K): ")
   if intent in ("P", "p"):
      result = weight*2.205
      print(f"The given weight in pounds is : {round(result, 2)} lbs")
   elif intent in ("K", "k"):
      result = weight/2.205
      print(f"The given weight in kilograms is: {round(result, 2)} kgs")
   else: 
      print(f"{intent} is invalid response")

 #function for distance conversion
elif response in ("B", "b"): 
   distance = float(input("Enter the distance: "))
   intent = input("What do you want to convert given distance into, miles or kilometers? (M/K): ")
   if intent in ("K", "k"):
      result = distance*1.609
      print(f"The given distance in kilometers is : {round(result, 2)} km")
   elif intent in ("M", "m"):
      result = distance/1.609
      print(f"The given distance in miles is: {round(result, 2)} miles")
   else: 
      print(f"{intent} is invalid response")

 #Function for temperature conversion
elif response in ("C", "c"):
   temp = int(input("Enter the temperature: "))
   intent = input("What do you want to convert given temperature into, celsius or fahrenheit? (C/F): ")
   if intent in ("C", "c") :
      result = (5/9)*(temp-32)
      print(f"The given temperature in celsius is: {round(result, 2)} °C")
   elif intent in ("F", "f"):
      result = ((9/5)*temp)+32
      print(f"The given temperature in fahrenheit is: {round(result, 2)} °F")
   else: 
      print(f"{intent} is invalid response")

#Prints invalid is the response is not as indicated
else: 
   print(f"{response} is invalid")
