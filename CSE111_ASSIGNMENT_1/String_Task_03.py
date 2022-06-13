# Solution to Task 3

toggle = False; result = ""
user = input("Sir, please enter your desired word: ")
for i in user:
    if i.isupper():
        toggle = True if not toggle else False
        continue
    if toggle:
        result += i
print(result if len(result) > 0 else "BLANK")

# Approach 2

user = input("Sir, please enter your desired word: ")
i, f = [i for i in range(len(user)) if user[i].isupper()]
print("BLANK" if (f-i) == 1 else user[i+1:f])
