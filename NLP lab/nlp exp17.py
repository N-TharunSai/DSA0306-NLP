import nltk

nltk.download("wordnet")

from nltk.corpus import wordnet

word = input("Enter a word: ")

synsets = wordnet.synsets(word)

print("\nSynsets:")

for syn in synsets[:5]:
    print("Synset:", syn.name())
    print("Definition:", syn.definition())
    print("Examples:", syn.examples())
    print()
