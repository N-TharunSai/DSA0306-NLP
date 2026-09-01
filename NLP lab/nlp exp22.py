import re

text = input("Enter text: ")

sentences = text.split(".")

last_noun = None

print("\nReference Resolution:")

for sentence in sentences:

    words = sentence.strip().split()

    for word in words:

        clean_word = re.sub(r'[^\w]', '', word)

        if clean_word.lower() in [
            "he", "she", "it", "they"
        ]:

            if last_noun:
                print(
                    clean_word,
                    "->",
                    last_noun
                )

        elif clean_word.lower() not in [
            "the", "a", "an", "is", "was",
            "and", "to", "in"
        ]:

            if clean_word[0].isupper():
                last_noun = clean_word
