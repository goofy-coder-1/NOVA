#collection = single "variable" used to store multiple values
# List = [] ordered and changeable. Duplicates OK
# Set = {} unordered and immutable, but Add/REmove OK. No duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER

# fruits = ["apple", "orange", "banana", "coconut"]

 # print(fruits[0::3])

# fruits[0] = "pineapple"
# fruits.append("Guava")
# fruits.remove("Guava")
# fruits.insert(3, "cocomelon")
# fruits.sort()
# fruits.reverse()
# print(fruits)
# print(fruits.index("orange"))

fruits = ["apple", "orange", "banana", "coconut"]

print("apple found in fruits" if "apple" in fruits else "nothing found")
