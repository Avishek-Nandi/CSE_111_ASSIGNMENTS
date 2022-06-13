# Solution to Task 1

cap = 0
smol = 0
user = input("Sir, please enter your desired text: ")
for i in user:
    if "a" <= i <= "z":
        smol += 1
    elif ord("A") <= ord(i) <= ord("Z"):
        cap += 1
if cap > smol:
    print(user.upper())
else:
    print(user.lower())

# Approach 2

checker = 0
user = input("Sir, please enter your desired text: ")
for i in user:
    checker += 1 if ord("A") <= ord(i) <= ord("Z") else -1 if ord("a") <= ord(i) <= ord("z") else 0
print(user.upper() if checker > 0 else user.lower())
