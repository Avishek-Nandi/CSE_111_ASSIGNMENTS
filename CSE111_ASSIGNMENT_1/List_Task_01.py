# Solution to Task 1 (List)

list_of_numbers = []
print("Enter numbers:")
while True:
    user = input()
    if user == "STOP":
        break
    else:
        list_of_numbers.append(user)

temp = []
for i in list_of_numbers:
    if i not in temp:
        print(f"{i}-{list_of_numbers.count(i)} times")
        temp.append(i)