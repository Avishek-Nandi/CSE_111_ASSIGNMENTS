# Solution to Task 1 (Dictionary)

user = [i.split(":") for i in input().split(",")]
dicty = {}
for i in user:
    dicty[i[0].strip()] = int(i[1]) if i[0].strip() not in dicty else dicty[i[0].strip()] + int(i[1])
print(dicty, f'Values: {sorted(set(dicty.values()))}', sep="\n")

