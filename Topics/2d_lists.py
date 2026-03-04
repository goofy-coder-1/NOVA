# fruits =     ["aple", "banana", "coconut", "orange"]
# vegetables = ["celery", "cauliflower", "potatoes", "carrots"]
# meats =      ["chicken", "fish", "mutton", "pork"]

# groceries = [fruits, vegetables, meats]

# # print(groceries[2][2])

# for collection in groceries:
#     for food in collection:
#         print(food, end = " ")
#     print()

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", "0", "+"))

for x in num_pad:
    for y in x:
        print(y, end = " ")
    print()