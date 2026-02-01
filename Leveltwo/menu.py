menu = []

while True:
    take = input("Enter the name of item (or q to quit): ").strip().lower()
    if take == 'q' or take == 'Q':
        break
    else:
        menu.append(take)

while True:
    found =  input("What item are you looking for(q to quit): ").lower().strip()
    if found == 'q' or found == 'Q':
       break

    is_found = False

    for item in menu:
      if found in item:
          is_found = True
          break
      
      
    if is_found:
        print("Item found")
    else:
        print("Item not found")
