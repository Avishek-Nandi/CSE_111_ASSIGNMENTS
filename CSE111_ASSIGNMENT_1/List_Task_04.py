# Solution to Task 4 (List)

number, times = [int(i) for i in input().strip().split()]
print(len([int(j) for j in input().strip().split() if int(j) + times <= 5])//3)

# Approach 2 (DOESN'T WORK)

# print(len([int(j) for j in input().strip().split(" ") if int(j) + [int(i) for i in input().strip().split(" ")][1] >= 5])//3)
