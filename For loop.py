

list_numbers = [1, 34, 34, 9, 87, 46, 84, 100, 44, 98, 847]

user_input = int(input("Enter a value: "))

for ln in list_numbers:
    if ln == user_input:
        print("we got a match")
        break
    else:
        print("No match")
print("Hey i am outside the loop")
