#program to find out compound interest

while True:

  print("Program written to find out compound interest")

  Principal = float(input("Enter the initial deposit: "))
  Interest = float(input("Enter the rate: "))

  times_compounded = int(input("How many times is it compounded?: "))
  time = int(input("How many years have passed by?: "))

  print(f"the principal is: {Principal}")
  print(f"the Interest rate is: {Interest}")        
  print(f"the compounded times is: {times_compounded}")        
  print(f"the time is: {time}")  

  response = input("Is the given information correct? (Y/N): ")


  if response.upper() == "N":
    print("Alright, let's try again")
    continue

  elif response.upper() == "Y": 
    print("lets continue")


    while Principal <= 0 :
        Principal = float(input("Enter the initial deposit: "))

    while Interest <= 0 :
        Interest = float(input("Enter the rate: "))
   
    while times_compounded <= 0 :
        times_compounded = int(input("How many times is it compounded?: "))
  
    while time <= 0 :
       time = int(input("How many years have passed by?: "))

    interest =  Interest/100
    Total = float(Principal *(pow((1+interest/times_compounded), time*times_compounded)))

    print(f"The total capital after {time} years is {Total:,.2f}")
    profit = Total-Principal
    print(f"The total profit is of ${profit:,.2f}")
    break

  else:
    print("Enter Y or N")