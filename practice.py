# details = {
#     "Name": {
#         "student": "Ujjwal",
#         "roll_no": 21,
#         "personal": {
#             "mother": "Krishna Rana",
#             "father": "Pashupati rana",
#             "sister": {
#                 "sister_first": "Sushmita Rana",
#                 "sister_second": "Samraggye Rana",
#                 "sister_third": "Suhani Rana"
#             }
#         }        
#     },
#     "disease" :{
#         "disease_eighteenth": {
#         "name": "Meningitis",
#         "duration": "days to weeks",
#         "impact": "brain damage, death",
#         "treatment": {"treatment_first" : "antibiotics",
#                       "treatment_second": "supportive care"}
#     },
#     "disease_nineteenth": {
#         "name": "Polio",
#         "duration": "varies",
#         "impact": "paralysis",
#         "treatment": "supportive care \n vaccination prevention"
#     },
#     "disease_twentieth": {
#         "name": "Chickenpox",
#         "duration": "1-2 weeks",
#         "impact": "rash, fever",
#         "treatment": "supportive care, antiviral drugs if severe"
#     }
# }
# }

# response = input("Enter disease name: ").lower()

# for disease in details["disease"].values():
#     if response == disease["name"].lower():
#         print("Disease found!")
#         print("Name:", disease["name"])
#         print("Duration:", disease["duration"])
#         print("Impact:", disease["impact"])
#         print("Treatment:", disease["treatment"])
#         break
# else:
#     print("Sorry, disease not found")

# family = input("Enter family name: ").lower()

# for fam in details["Name"].values():
#     if family == fam["student"].lower():
#         print("Student found")
#         print("Name: ", fam["student"])
#         print("Mother: ", fam["mother"])
#     else:
#       print("No data")

# print('"yes" they said')
# verb = ["Saurabh", "Ujjwal", "Aakash"]

# while True:
#    response = input("Enter the name of the student: ").lower()
#    found = False
#    for name in verb:
#      if response == name.lower():
#        print(f"Are you searching for {name}?")
#        found = True
#        break
#      if found:
#         break
#    if not found:
#       print("Not found")
#    queiry = input("Do you want to search for another student?(Y/N): ").lower()
#    if queiry != "y":
#     break

student = {
    "Ujjwal": {"Grade": "Bachelor", "Age": "20", "Birthplace": "Surkhet", "Surname": "Rana", "Phone": "98765432210", "pronoun": "his"},
    "Saurabh": {"Grade": "Second-sem", "Age": "19", "Birthplace": "Morang", "Surname": "Limbu", "Phone": "1234567890","pronoun": "his"}
}

while True:
    #accepts user input
    search = input("Name of the student: ").lower()
    found = False
    #For loop starts
    for name_key, name_value in student.items():
         if search == name_key.lower():
            print(f"The student is in {name_value['Grade']} and {name_value['pronoun']} age is {name_value['Age']}."
                  f" {name_value['pronoun']} birth took place in {name_value['Birthplace']} in {name_value['Surname']} clan")
            found = True
            break
    if not found:
       print("Student Not found but if he/she has been admitted, we will add details to database soon")

    #ask user if he/she wants to perform another search operation
    queiry = input("Do you want to search for another student?(Y/N): ").lower()
    if queiry != "y":
     break