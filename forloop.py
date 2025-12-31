# for x in reversed(range (1, 11, 2)):
#     print(x)

# print("Happy new year")

import time

# for x in reversed(range(1, 11)):
#     if x == 5:
#         print("Half time, be ready")
#     else:
#       print(x)
#       print("Times's ticking")
#       time.sleep(2)

# print("Time over")

set_time = int(input("Set timer: "))

for x in reversed(range(1, set_time)):
   seconds = x % 60
   minutes = int(x/60)%60
   hours = int(x/3600)
   print(f"{hours:02}:{minutes:02}:{seconds:02}") 
   time.sleep(1)
print("Ooops! Time ended")