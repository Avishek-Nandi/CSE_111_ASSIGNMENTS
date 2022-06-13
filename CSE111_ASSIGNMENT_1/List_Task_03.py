# Solution to Task 3 (List)

listu = []

print("Enter numbers:")

while True:
    user = input()
    if user == "STOP":
        break
    else:
        listu.append([int(i) for i in user.strip().split()])

listd = [[(i[j+1] - i[j]) if (i[j+1] - i[j] >= 0) else (i[j+1] - i[j])*-1 for j in range(len(i)-1)]for i in listu]

for i in listd:
    mini, maxi = sorted(i)[0], sorted(i)[-1]
    print("UB Jumper") if [i for i in range(mini, maxi+1)] == sorted(i) else print("Not UB Jumper")

