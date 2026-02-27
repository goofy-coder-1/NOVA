import random
import string

chars = " " +string.punctuation + string.digits + string.ascii_letters

chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print(f"chars: {chars}")
# print(f"key  : {key}")

#Encrytp
plain_text = input("Enter a message: ")
cipher = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher += key[index]

print(f"Original message: {plain_text}")
print(f"encrypted Message: {cipher}")

cipher_text = input("What's the encrypted message?: ")
message = ""

for letter in cipher_text:
    index = key.index(letter)
    message += chars[index]

print(f"code message: {cipher_text}")
print(f"Normal Message: {message}")

