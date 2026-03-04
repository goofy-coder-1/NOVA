#string indexing
# indexing = accessing elements of a sequence using [] (indexing operators)


debit_number = "1234-5678-90123-1525"

print(debit_number[0])
print(debit_number[:4])
print(debit_number[5:9])

first_four = debit_number[0:4]
last_four = debit_number[-4:]

print(f"Your debit card numbe is {first_four}-XXXX-XXXXX-{last_four}")