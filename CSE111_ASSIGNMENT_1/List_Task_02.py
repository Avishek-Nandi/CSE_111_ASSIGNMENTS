# Solution to Task 2 (List)

list_of_inputs = []
highest = -float('inf')
highest_list = None

[list_of_inputs.append([int(j) for j in input().split()]) for i in range(int(input()))]

for i in list_of_inputs:
    total = 0
    for j in i:
        total += j
    if total > highest:
        highest = total
        highest_list = i

print(highest)
print(highest_list)