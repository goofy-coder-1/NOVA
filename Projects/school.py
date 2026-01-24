#School Database
#List = []
# tuple = ()
# set = {}

Student = {
    "Grade_ten": {
        "student_one": {
            "Name": "John Cena", "Student_id": "MALE1019", "Major": "Optional Math", "Role": "Class Monitor",
            "Parents": { "Mother": "Sandhya Cena", "Father": "Ram Bahadur Cena"}
        },
        "student_two": {
            "Name": "Roman", "Student_id": "MALE1018", "Major": "Optional Math", "Role": "Class Clown",
            "Parents": { "Mother": "HHH", "Father": "harCena" }
        },
        "student_three": {
            "Name": "Sushila Karki", "Student_id": "FEMALE1021", "Major": "Biology", "Role": "Substitute leader",
            "Parents": {"Mother": "Hinata Hyuga", "Father": "Naruto Uzumaki"}
        },
        "student_four": {
            "Name": "Prithivi Narayan", "Student_id": "MALE1081", "Major": "Digital logic", "Role": "King",
            "Parents": { "Mother": "Harimaya ", "Father": "Uniq Poet"}
        }
    },
    "Grade_XI": {
        "student_one": {
            "Name": "Saurabh", "Student_id": "MALE1119", "Major": "Physics", "Role": "Class Monitor",
            "Parents": { "Mother": "Srijana Tamang", "Father": ""}
        },
        "student_two": {
            "Name": "Random Girl", "Student_id": "FEMALE1118E", "Major": "Math", "Role": "Unknown",
            "Parents": { "Mother": "Random Aama", "Father": "Random Buwa" }
        },
        "student_three": {
            "Name": "Beautiful Girl", "Student_id": "FEMALE1121", "Major": "Physics", "Role": "",
            "Parents": {"Mother": "Nanithaku", "Father": "Godatta Prasad"}
        },
        "student_four": {
            "Name": "Donald Trump", "Student_id": "MALE1090", "Major": "WAR", "Role": "PEDO",
            "Parents": { "Mother": "Justin Bieber ", "Father": "Sacar"}
        }
    }
}

while True:
    response = input("Enter the name of student: ").strip().lower()
    found = False
    for grade_keys, grade_value in Student.items():
        for student_key, student_value in grade_value.items():
            if response == student_value["Name"].lower():
               print(f"Student found in {grade_keys}")
               print("-------Student details----------")
               print(f"{student_value['Name']}'s student id is {student_value['Student_id']}") 
               print(f"{student_value['Name']}'s Father is {student_value['Parents']['Father']}") 
               print(f"{student_value['Name']}'s Mother is {student_value['Parents']['Mother']}") 
               print(f"{student_value['Name']}'s Major is {student_value['Major']}") 
               print("--------------------------------")
               print("--------------------------------")
               found = True
               break
            if found:
             break
    if not found:
        print("not found in any grade")
    
    answer = input("Do you want to continue(Y/N): ").lower()
    if answer == "y":
      continue
    else:
      break