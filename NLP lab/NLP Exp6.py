from nltk.util import bigrams

text = "Artificial Intelligence is transforming the world"

words = text.split()

bigram_list = list(bigrams(words))

print("Original Sentence:")
print(text)

print("\nGenerated Bigrams:")

for bg in bigram_list:
    print(bg)
