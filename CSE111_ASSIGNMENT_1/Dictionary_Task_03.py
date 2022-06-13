# Solution to Task 3 (Dict)

r_dict = {}
for i in input().split(","):
    j, k = [m.strip() for m in i.strip().split(":")]
    r_dict[k] = [j] if k not in r_dict else r_dict[k]+[j]
print(r_dict)

