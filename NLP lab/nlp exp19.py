import nltk

nltk.download("wordnet")
nltk.download("punkt")

from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize


def lesk(sentence, ambiguous_word):

    context = set(word_tokenize(sentence.lower()))

    best_synset = None
    max_overlap = 0

    for synset in wordnet.synsets(ambiguous_word):

        definition_words = set(
            word_tokenize(synset.definition().lower())
        )

        overlap = len(context & definition_words)

        if overlap > max_overlap:
            max_overlap = overlap
            best_synset = synset

    return best_synset


sentence = input("Enter sentence: ")
word = input("Enter ambiguous word: ")

result = lesk(sentence, word)

if result:
    print("\nSelected Sense:")
    print(result.name())
    print("Definition:", result.definition())
else:
    print("No suitable sense found.")
