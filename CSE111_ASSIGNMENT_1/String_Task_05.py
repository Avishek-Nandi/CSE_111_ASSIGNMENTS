# Solution to Task 5

password = input("Sir, please input your desired password: ")

digit_library = "0123456789"
special_library = "_$#@"

lowercase = False
uppercase = False
digit = False
special = False

for char in password:
    if ord("A") <= ord(char) <= ord("Z"):
        uppercase = True
    elif ord("a") <= ord(char) <= ord("z"):
        lowercase = True
    elif char in digit_library:
        digit = True
    elif char in special_library:
        special = True

if uppercase and lowercase and digit and special:
    print("OK")
if not uppercase:
    print("Uppercase missing", end=", ")
if not lowercase:
    print("Lowercase missing", end=", ")
if not digit:
    print("Digit missing", end=", ")
if not special:
    print("Special character missing")

