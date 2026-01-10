# name = input("Enter your full name:  ")

# # result = len(name)
# # print(result)

# # find = name.find("u")
# # print(find)

# # name = name.capitalize()
# # print(name)

# name = name.upper()
# print(name)

# result = name.isalpha()
# print(result)

# print(help(str))
# print(name.capitalize())
# print(len(name))

# gpa1 = input("Enter your gpa: ")
# gpa = int(gpa1)
# print(gpa+36)

while True:
        grade_Physics = input("Your gpa in Physics: ")
        if grade_Physics.count(".")>1:
            print("grade must not be in Alphabet")
        elif not grade_Physics[0].isdigit():
            print("Gpa can't be alphabet")
        elif not grade_Physics[2].isdigit():
            print("Gpa can't be alphabet")
        elif not grade_Physics[3].isdigit():
            print("Gpa can't be alphabet")
        elif grade_Physics[0] in ["4", "5", "6", "7", "8", "9"]:
            print("invalid gpa")
        elif len(grade_Physics) > 4 :
            print("Invalid gpa (only two decimals are accepted after dot)")
        else:
            print(f"{grade_Physics} gpa is stored \n")
            break
