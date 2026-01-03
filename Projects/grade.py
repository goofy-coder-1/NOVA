#code to calculate grade of student

print("Program to find out the grade of students")
print("-----------------------------------------")

while True:
    student = input("Enter your username: ")

    if student.isdigit():
        print("username can't be digit only")
    elif student.isspace():
        print("Name must not be empty")
    elif not student[0].isupper():
        print("first letter must be capital")
    elif len(student) < 6:
        print("username can't be less than 6 characters.")
    else : 
        print("Username stored!")
        break

level = input("Which level of study are you in?: \n" \
              "(H for High School)\n" \
              "(U for undergraduate): ").upper()
#Function to calculate grade of high schoolers
if level == "H":
    while True:
        grade_Physics = input("Your gpa in Physics: ")
        if grade_Physics.count(".")>1:
            print("grade must not be in Alphabet")
        elif not grade_Physics[0].isdigit():
            print("Gpa can't be alphabet")
        elif not len(grade_Physics) == 4 :
            print("Invalid gpa (gpa must only contain 4 character including '.')")
        elif not grade_Physics[2].isdigit():
            print("Gpa can't be alphabet")
        elif not grade_Physics[3].isdigit():
            print("Gpa can't be alphabet")
        elif grade_Physics[0] in ["5", "6", "7", "8", "9"]:
            print("invalid gpa")
        else:
            print("Physics gpa is stored \n")
            break
    while True:
        grade_Chemistry = input("Your gpa in Chemistry: ")
        if grade_Chemistry.count(".")>1:
            print("grade must not be in Alphabet")
        elif not grade_Chemistry[0].isdigit():
            print("Gpa can't be alphabet")
        elif not len(grade_Chemistry) == 4 :
           print("Invalid gpa (gpa must only contain 4 character including '.')")
        elif not grade_Chemistry[2].isdigit():
            print("Gpa can't be alphabet")
        elif not grade_Chemistry[3].isdigit():
            print("Gpa can't be alphabet")
        elif grade_Chemistry[0] in ["5", "6", "7", "8", "9"]:
            print("invalid gpa")
        else:
            print("Chemistry gpa is stored \n")
            break
    while True:
        grade_Math = input("Your gpa in Math: ")
        if grade_Math.count(".")>1:
            print("grade must not be in Alphabet")
        elif not grade_Math[0].isdigit():
            print("Gpa can't be alphabet")
        elif not len(grade_Math) == 4 :
           print("Invalid gpa (gpa must only contain 4 character including '.')")
        elif not grade_Math[2].isdigit():
            print("Gpa can't be alphabet")
        elif not grade_Math[3].isdigit():
            print("Gpa can't be alphabet")
        elif grade_Math[0] in ["5", "6", "7", "8", "9"]:
            print("invalid gpa")
        else:
            print("Math gpa is stored \n")
            break
    while True:
        grade_Biology = input("Your gpa in Biology: ")
        if grade_Biology.count(".")>1:
            print("grade must not be in Alphabet")
        elif not len(grade_Biology) == 4 :
            print("Invalid gpa (gpa must only contain 4 character including '.')")
        elif not grade_Biology[0].isdigit():
            print("Gpa can't be alphabet")
        elif not grade_Biology[2].isdigit():
            print("Gpa can't be alphabet")
        elif not grade_Biology[3].isdigit():
            print("Gpa can't be alphabet")
        elif grade_Biology[0] in ["5", "6", "7", "8", "9"]:
            print("invalid gpa")
        else:
            print("Biology gpa is stored \n")
            break

    Physics = float(grade_Physics)
    Chemistry = float(grade_Chemistry)
    math = float(grade_Math)
    Biology = float(grade_Biology)
    total = math+Biology+Physics+Chemistry
    gpa = total/4
    print(f"{student}'s total gpa is: {gpa:.02f}")
    if gpa > 3.6 :
        print("The student has secured grade A+")
    elif 3.6 > gpa >3.2:
        print("The student has secured grade A")
    elif 2.8 < gpa <3.2:
        print("The student has secured grade B+")
    elif 2.4 < gpa < 2.8:
        print("The student has secured grade B")
    else: 
        print("Failed")

        #Function for the students of undergraduate
elif level == "U":
    while True:
        grade_C_programming = input("Your gpa in C Programming: ")
        if grade_C_programming.count(".")>1:
            print("grade must not be in Alphabet")
        elif not len(grade_C_programming) == 4 :
           print("Invalid gpa (gpa must only contain 4 character including '.')")
        elif not grade_C_programming[0].isdigit():
            print("Gpa can't be alphabet")
        elif not grade_C_programming[2].isdigit():
            print("Gpa can't be alphabet")
        elif not grade_C_programming[3].isdigit():
            print("Gpa can't be alphabet")
        elif grade_C_programming[0] in ["5", "6", "7", "8", "9"]:
            print("invalid gpa")
        else:
            print("C Programming gpa is stored \n")
            break
    while True:
        grade_DL = input("Your gpa in DL: ")
        if grade_DL.count(".")>1:
            print("grade must not be in Alphabet")
        elif not len(grade_DL) == 4 :
            print("Invalid gpa (gpa must only contain 4 character including '.')")
        elif not grade_DL[0].isdigit():
            print("Gpa can't be alphabet")
        elif not grade_DL[2].isdigit():
            print("Gpa can't be alphabet")
        elif not grade_DL[3].isdigit():
            print("Gpa can't be alphabet")
        elif grade_DL[0] in ["5", "6", "7", "8", "9"]:
            print("invalid gpa")
        else:
            print("Digital Logic gpa is stored \n")
            break
    while True:
        grade_Math = input("Your gpa in Math: ")
        if grade_Math.count(".")>1:
            print("grade must not be in Alphabet")
        elif not len(grade_Math) == 4 :
           print("Invalid gpa (gpa must only contain 4 character including '.')")
        elif not grade_Math[0].isdigit():
            print("Gpa can't be alphabet")
        elif not grade_Math[2].isdigit():
            print("Gpa can't be alphabet")
        elif not grade_Math[3].isdigit():
            print("Gpa can't be alphabet")
        elif grade_Math[0] in ["5", "6", "7", "8", "9"]:
            print("invalid gpa")
        else:
            print("Math gpa is stored \n")
            break
    while True:
        grade_Microprocessor = input("Your gpa in Microprocessor: ")
        if grade_Microprocessor.count(".")>1:
            print("grade must not be in Alphabet")
        elif not len(grade_Microprocessor) == 4 :
           print("Invalid gpa (gpa must only contain 4 character including '.')")
        elif not grade_Microprocessor[0].isdigit():
            print("Gpa can't be alphabet")
        elif not grade_Microprocessor[2].isdigit():
            print("Gpa can't be alphabet")
        elif not grade_Microprocessor[3].isdigit():
            print("Gpa can't be alphabet")
        elif grade_Microprocessor[0] in ["5", "6", "7", "8", "9"]:
            print("invalid gpa")
        else:
            print("Microprocessor gpa is stored \n")
            break

    C = float(grade_C_programming)
    DL = float(grade_DL)
    math = float(grade_Math)
    Microprocessor = float(grade_Microprocessor)
    total = math+C+DL+Microprocessor
    gpa = total/4
    print(f"{student}'s total gpa is: {gpa:.02f}")
    if gpa > 3.7 :
        print("The student has secured grade A+")
    elif 3.7 > gpa >3.4:
        print("The student has secured grade A")
    elif 3 < gpa <3.4:
        print("The student has secured grade B+")
    elif 2.8 < gpa < 3:
        print("The student has secured grade B")
    else: 
        print("Failed")
else:
    print("Invalid Input")
