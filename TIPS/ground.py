
school = {
   "hello": {"name": "Ujjwal", "place": "Surkhet"},
   "hello2": {"name": "Saurabh", "place": "Kathmandu"},
   "hello3": {"name": "Bhanu", "place": "Kerabari"},
   "hello4": {"name": "Prithivi", "place": "Gorkha"},
   "hello5": {"name": "Apradhi", "place": "Nakhhu"},
   "hello6": {"name": "British_Laude", "place": "Lundon"}
}

# response = input("Enter the name of the person: ").lower()
# found = False
# for first_layer_key, first_layer_value in school.items(): 
#     for second_layer_key, second_layer_value in first_layer_value.items():
#         if response == str(second_layer_value).lower():
#             print("student found")
#             print(f"The student you are talking about is from {first_layer_value['place']}")
#             found = True
#             break
#     if found:
#           break
# else:
#     print("student not found")

lists = {"1","2","3","4", "2"}
lists.remove("3")
print(lists)