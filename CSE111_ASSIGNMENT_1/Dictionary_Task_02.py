# Solution to Task 2 (Dictionary)

num_dict = {}
print("Enter numbers:")
while True:
    user = input()
    if user == "STOP":
        break
    num_dict[user] = 1 if user not in num_dict else num_dict[user] + 1

[print(f"{i} - {j} times") for i, j in num_dict.items()]
