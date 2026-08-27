import re

def rule_based_tag(sentence):
    words = sentence.split()
    result = []

    for word in words:
        if re.match(r".*ing$", word):
            tag = "VBG"
        elif re.match(r".*ed$", word):
            tag = "VBD"
        elif re.match(r".*ly$", word):
            tag = "RB"
        elif word.lower() in ["the", "a", "an"]:
            tag = "DT"
        elif word.lower() in ["is", "am", "are", "was", "were"]:
            tag = "VB"
        else:
            tag = "NN"

        result.append((word, tag))

    return result

text = input("Enter a sentence: ")

print("\nRule-Based POS Tags:")
for word, tag in rule_based_tag(text):
    print(word, "->", tag)
