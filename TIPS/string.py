#string methods and related tips

# text =  input("Enter your text: ")

# print(text.capitalize()) -> makes the first character capital

#print(text.casefold()) -> converts everything into lowercase

#print(text.center(20, "-")) -> centers the Input

# print(f"You typed hello {text.count('hello')} times") ->
#  This string methods help to count how many times a specific characte popped up in text

# print(text.encode()) -> this help decode string into binary

# print(text.endswith("al")) -> search if the word ends with secific char

# print(text.expandtabs(10)) -> expands space between two words, just write how much space you want in the expandtabs() part

# print(text.find("h")) -> helps to find out the specific character and its index position

# print(format()) -> helps to put formats specified values in string
# name = "Ujjwal"

# response = "My name is {}".format(name)
# print(response)


#format.map() and its usage
# information = {
#     "name": "Ujjwal",
#     "age": 20,
#     "city": "Kathmandu"
# }

# template = "Name : {name}\nAge: {age}\nCity: {city}"

# output = template.format_map(information)
# print(output)

# print(text.index("1")) -> helps to find out at what index an specific character is present at

# print(text.isalnum()) -> shows true is the characters are alphabet or numeric

# print(text.isalpha()) -> verifies if all the characters are in alphabet

# print(text.isascii()) -> verifies if the characters input are ascii characters or not

# print(text.isdecimal()) -> verifies if the input is decimal or not 

# print(text.isdigit()) -> verifies if the number is digit or not

# print(text.isidentifier()) ->Ensures strings can safely be used as variable names, function names, or class attributes, especially when names are generated dynamically or provided by users.

# print(text.lower()) -> Returns the input in lower case 

# print(text.isnumeric()) -> verifies if all the characters are numeric 

# print(text.isprintable()) -> tells if the input is printable or not 

# print(text.isspace()) -> tells if the input is just left empty (will show false if there is even a single string)

# print(text.ljust(5, "-")) -> pads on the right, keeps text on the left

# print(text.rjust(5, "-")) -> pads on the left, keeps text on the right 

# print(text.title()) -> This verifies if the first string of each word is capitalized or not 

# print(text.lstrip()) #-> removes any space from the left side 

# print(text.find("h")) -> helps to find at which index a specific character is present 

# print(text.rpartition("sir")) -> returns a tuple where string is parted 

# print(text.split(",")) -> splits the string at the specified seperator and returns a list 

# print(text.splitlines()) -> Splits the string at line breaks and returns a list 

# print(text.startswith("The")) -> verifies if something actually starts with the intended character 

# print(text.swapcase()) #-> This swaps the uppercase into lower and vice versa

diseases = {
    "disease_first" :{
         "name": "Cancer",
         "duration": "varies",
         "impact": "possible death"
        },
    "disease_second" :{
         "name": "Tumor",
         "duration": "1 year",
         "impact": "possible death"
        },
    "disease_third" :{
         "name": "Dumbness",
         "duration": "lifetime",
         "impact": "unknown"
        }
}

format = "Disease : {name}\n Duration: {duration}\n Impact: {impact}\n"

for disease in diseases.values():
    print(format.format_map(disease))




      