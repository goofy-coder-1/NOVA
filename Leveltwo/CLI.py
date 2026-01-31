# help("keywords")

# False               class               from                or
# None                continue            global              pass    
# True                def                 if                  raise   
# and                 del                 import              return  
# as                  elif                in                  try     
# assert              else                is                  while   
# async               except              lambda              with    
# await               finally             nonlocal            yield   
# break               for                 not

for i in range(5):           # i = 0, 1, 2, 3, 4, 5
    for j in range(i + 1):   # j = 0 to i
        print("*", end="")   # end="" prevents new line
    print()                  # move to next line after inner loop
