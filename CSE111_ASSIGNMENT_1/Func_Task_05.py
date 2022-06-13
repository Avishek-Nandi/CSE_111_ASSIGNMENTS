# Solution to Task 5 (Functions)

def is_palindrome(word):
    palindrome = True
    for i in range(len(word)//2):
        if word[i] != word[-(i+1)]:
            palindrome = False
    print("Palindrome" if palindrome else "Not a palindrome")


if __name__ == "__main__":
    is_palindrome(input("Enter the word you want to check: ").replace(" ", ""))
