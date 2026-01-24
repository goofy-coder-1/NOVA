#Program to find out the fruit and veggies

fruits = (
    "apple", "banana", "orange", "mango", "grape",
    "strawberry", "blueberry", "kiwi", "pineapple", "watermelon",
    "papaya", "peach", "pear", "plum", "cherry",
    "pomegranate", "fig", "lychee", "guava", "apricot",
    "coconut", "dragonfruit", "raspberry", "blackberry", "passionfruit"
)

vegetables = (
    "carrot", "broccoli", "cauliflower", "spinach", "kale",
    "lettuce", "cabbage", "tomato", "cucumber", "bell pepper",
    "onion", "garlic", "potato", "sweet potato", "eggplant",
    "zucchini", "pumpkin", "radish", "beetroot", "peas",
    "corn", "asparagus", "mushroom", "celery", "okra"
)

items = []

def find_function(item, fruits, vegetables):
    if item in fruits:
        return "fruits"
    elif item in vegetables:
        return "Vegetables"
    else:
       return "No data found"


response = int(input("How many items do you want to enter?: "))

for i in range(response):
    item = input(f"Enter the item {i + 1}: ").lower()
    items.append(item)

for i in items:
   category = find_function(i, fruits, vegetables)

   if category == "Vegetables":
       print(f"{i} was found on veggies section")
   elif category == "fruits":
       print(f"{i} was found on fruits section")
   else:
       print(f"No data on {i}")


