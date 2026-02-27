import time
import winsound



while True:

    number = int(input("Enter the number: "))
    if number % 2 == 0:
       print("Number is even")
    else:
       print("Number is odd")

    choice = input("Do you want to exit?(y/n): ").lower()
    if choice != 'n':
       print("Ending the program")
       time.sleep(3)
       winsound.Beep(700, 900)
       winsound.Beep(700, 900)
       winsound.Beep(700, 900)
       winsound.Beep(1000, 1000)
       print("program closed")
       break

