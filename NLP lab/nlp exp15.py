# Transformation-Based POS Tagging

def transformation_based_tagging(words):

    # Initial tagging
    tagged_words = []

    for word in words:
        tagged_words.append([word, "NOUN"])

    # Transformation rules
    for item in tagged_words:

        word = item[0].lower()

        # Rule 1: Words ending in -ing are verbs
        if word.endswith("ing"):
            item[1] = "VERB"

        # Rule 2: Words ending in -ly are adverbs
        elif word.endswith("ly"):
            item[1] = "ADVERB"

        # Rule 3: Common determiners
        elif word in ["the", "a", "an"]:
            item[1] = "DETERMINER"

        # Rule 4: Common verbs
        elif word in ["is", "am", "are", "was", "were"]:
            item[1] = "VERB"

        # Rule 5: Words ending in -ous are adjectives
        elif word.endswith("ous"):
            item[1] = "ADJECTIVE"

    return tagged_words


text = input("Enter a sentence: ")

words = text.split()

result = transformation_based_tagging(words)

print("\nWord\t\tPOS Tag")
print("-" * 25)

for word, tag in result:
    print(f"{word:15}{tag}")
    
