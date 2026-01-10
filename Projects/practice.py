# practice file

# Dictionary with treatment info
diseases = {
    "disease_first": {
        "name": "Cancer",
        "duration": "varies",
        "impact": "possible death",
        "treatment": "chemotherapy, surgery, radiation"
    },
    "disease_second": {
        "name": "Tumor",
        "duration": "1 year",
        "impact": "possible death",
        "treatment": "surgery, medication"
    },
    "disease_third": {
        "name": "Dumbness",
        "duration": "lifetime",
        "impact": "unknown",
        "treatment": "none"
    },
    "disease_fourth": {
        "name": "Diabetes",
        "duration": "lifetime",
        "impact": "organ damage",
        "treatment": "insulin, diet control"
    },
    "disease_fifth": {
        "name": "Hypertension",
        "duration": "lifetime",
        "impact": "heart attack, stroke",
        "treatment": "medication, lifestyle changes"
    },
    "disease_sixth": {
        "name": "Malaria",
        "duration": "weeks",
        "impact": "possible death",
        "treatment": "antimalarial drugs"
    },
    "disease_seventh": {
        "name": "Tuberculosis",
        "duration": "months to years",
        "impact": "lung damage, death",
        "treatment": "antibiotics for 6-9 months"
    },
    "disease_eighth": {
        "name": "Alzheimer's",
        "duration": "years",
        "impact": "memory loss, cognitive decline",
        "treatment": "supportive care, medications for symptoms"
    },
    "disease_ninth": {
        "name": "Parkinson's",
        "duration": "lifetime",
        "impact": "movement issues, cognitive problems",
        "treatment": "medications, physiotherapy"
    },
    "disease_tenth": {
        "name": "HIV/AIDS",
        "duration": "lifetime",
        "impact": "immune system failure",
        "treatment": "antiretroviral therapy (ART)"
    },
    "disease_eleventh": {
        "name": "Asthma",
        "duration": "lifetime",
        "impact": "breathing difficulty",
        "treatment": "inhalers, avoiding triggers"
    },
    "disease_twelfth": {
        "name": "Influenza",
        "duration": "1-2 weeks",
        "impact": "fever, body ache",
        "treatment": "rest, fluids, antiviral drugs"
    },
    "disease_thirteenth": {
        "name": "Cholera",
        "duration": "days to weeks",
        "impact": "severe dehydration",
        "treatment": "oral rehydration, antibiotics"
    },
    "disease_fourteenth": {
        "name": "Dengue",
        "duration": "1-2 weeks",
        "impact": "bleeding, shock",
        "treatment": "supportive care, fluids"
    },
    "disease_fifteenth": {
        "name": "Ebola",
        "duration": "2-21 days",
        "impact": "organ failure, death",
        "treatment": "supportive care, experimental drugs"
    },
    "disease_sixteenth": {
        "name": "Hepatitis B",
        "duration": "chronic in some cases",
        "impact": "liver damage",
        "treatment": "antiviral medications, liver monitoring"
    },
    "disease_seventeenth": {
        "name": "Measles",
        "duration": "7-14 days",
        "impact": "rash, fever, complications",
        "treatment": "supportive care, vaccination prevention"
    },
    "disease_eighteenth": {
        "name": "Meningitis",
        "duration": "days to weeks",
        "impact": "brain damage, death",
        "treatment": "antibiotics, supportive care"
    },
    "disease_nineteenth": {
        "name": "Polio",
        "duration": "varies",
        "impact": "paralysis",
        "treatment": "supportive care, vaccination prevention"
    },
    "disease_twentieth": {
        "name": "Chickenpox",
        "duration": "1-2 weeks",
        "impact": "rash, fever",
        "treatment": "supportive care, antiviral drugs if severe"
    }
}

template = "Name: {name}\n Duration: {duration}\n Impact: {impact} \nTreatment: {treatment}"

while True:
    condition = input("What condition are you suffering from?: ")
  
    search = False  
    for disease in diseases.values():
        if disease["name"].lower() == condition.lower():
           print(f"You are talking about {disease['name']}.\nThe impact of this disease are {disease['impact'].upper()} and lasts for {disease['duration']}.\nTreatment are {disease['treatment']}")
           search = True
           break
    if not search:
        print("We don't have the information you are looking for")

    response = input("Do you want to do another search?(y/n): ").lower()
    if response.lower() != "y":
            break

        
        
 
