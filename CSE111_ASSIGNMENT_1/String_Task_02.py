# Solution to Task 2

conditions = [False, False]
user = input("Sir, please enter your desired text: ")
for i in user:
    if i.isalpha():
        conditions[0] = True
    elif i.isdigit():
        conditions[1] = True
print("MIXED" if conditions[0] and conditions[1] else "WORD" if conditions[0] else "NUMBER" if conditions[1] else "Invalid")


# Aproach 2

checker = 0
user = input("Sir, please enter your desired text: ")
for i in user:
    checker += 1 if i.isalpha() else -1 if i.isdigit() else 0
print("WORD" if checker == len(user) else "NUMBER" if checker == -len(user) else "MIXED")


# Approach 3:

user_input = input("Sir, please enter your desired text: ")
print("NUMBER" if user_input.isdigit() else "WORD" if user_input.isalpha() else "MIXED")
