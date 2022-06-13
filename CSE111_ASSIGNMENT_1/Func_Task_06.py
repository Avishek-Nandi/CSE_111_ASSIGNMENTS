# Solution to Task 6 (Functions)

def capitalizer(sentence):
    sentence = list(sentence)

    for i in range(len(sentence)):
        if i == 0:
            sentence[i] = sentence[i].upper()
        elif i == len(sentence)-1:
            break
        elif sentence[i] in ".!?":
            if sentence[i+1] not in " .!?":
                sentence.insert(i+1, " ")
            sentence[i+2] = sentence[i+2].upper()
        elif sentence[i] == "i" and sentence[i+1] in " .!?" and sentence[i-1] == " ":
            sentence[i] = "I"

    print("".join(sentence))


if __name__ == "__main__":
    capitalizer(input("Enter Text: ").strip("' ()"))
