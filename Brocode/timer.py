import time
import winsound

my_time = int(input("Enter the time in seconds: "))

for x in reversed(range(0, my_time+1)):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    
    #Prints time
    print(f"{hours:02}:{minutes:02}:{seconds:02}")

    #code for sounds when only 10 seconds remain
    if x <= 10 and x > 0:
        winsound.Beep(800, 300)
        time.sleep(0.7)
    else:
        time.sleep(1)

winsound.Beep(1000, 2000)


