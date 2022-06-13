# Solution to Task 4

result = ""
word = input("Sir, please enter your desired word: ")
word1 = input("Sir, please enter your desired word: ")
for i in word:
    if i in word1:
        result += i
for i in word1:
    if i in word:
        result += i
print(result if len(result) > 0 else 'Nothing in common')


# Approach 2

word = input("Sir, please enter your desired word: ")
word1 = input("Sir, please enter your desired word: ")
result = [i for i in word+word1 if (i in word1 and i in word)]
print("".join(result) if len(result) > 0 else 'Nothing in common')

