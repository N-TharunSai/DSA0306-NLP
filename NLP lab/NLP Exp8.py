from collections import defaultdict

# Simple training data
training_data = [
    [("I", "PRP"), ("like", "VBP"), ("Python", "NNP")],
    [("I", "PRP"), ("like", "VBP"), ("NLP", "NNP")],
    [("Python", "NNP"), ("is", "VBZ"), ("useful", "JJ")],
    [("NLP", "NNP"), ("is", "VBZ"), ("interesting", "JJ")]
]

word_tag_counts = defaultdict(lambda: defaultdict(int))

for sentence in training_data:
    for word, tag in sentence:
        word_tag_counts[word][tag] += 1

def stochastic_tag(sentence):
    result = []

    for word in sentence.split():
        if word in word_tag_counts:
            tag = max(word_tag_counts[word],
                      key=word_tag_counts[word].get)
        else:
            tag = "NN"
        result.append((word, tag))

    return result

text = input("Enter a sentence: ")

print("\nStochastic POS Tags:")
for word, tag in stochastic_tag(text):
    print(word, "->", tag)
