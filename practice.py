details = {
    "Name": {
        "student": "Ujjwal",
        "roll_no": 21,
        "personal": {
            "mother": "Krishna Rana",
            "father": "Pashupati rana",
            "sister": {
                "sister_first": "Sushmita Rana",
                "sister_second": "Samraggye Rana",
                "sister_third": "Suhani Rana"
            }
        }        
    },
    "disease" :{
        "disease_eighteenth": {
        "name": "Meningitis",
        "duration": "days to weeks",
        "impact": "brain damage, death",
        "treatment": {"treatment_first" : "antibiotics",
                      "treatment_second": "supportive care"}
    },
    "disease_nineteenth": {
        "name": "Polio",
        "duration": "varies",
        "impact": "paralysis",
        "treatment": "supportive care \n vaccination prevention"
    },
    "disease_twentieth": {
        "name": "Chickenpox",
        "duration": "1-2 weeks",
        "impact": "rash, fever",
        "treatment": "supportive care, antiviral drugs if severe"
    }
}
}

response = input("Enter disease name: ").lower()

for disease in details["disease"].values():
    if response == disease["name"].lower():
        print("Disease found!")
        print("Name:", disease["name"])
        print("Duration:", disease["duration"])
        print("Impact:", disease["impact"])
        print("Treatment:", disease["treatment"])
        break
else:
    print("Sorry, disease not found")

family = input("Enter family name: ").lower()

for fam in details["Name"].values():
    if family == fam["student"].lower():
        print("Student found")
        print("Name: ", fam["student"])
        print("Mother: ", fam["mother"])
    else:
      print("No data")