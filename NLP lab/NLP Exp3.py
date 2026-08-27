import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')

word = input("Enter a word: ")

ps = PorterStemmer()
lm = WordNetLemmatizer()

print("Original Word :", word)
print("Stemmed Word :", ps.stem(word))
print("Lemmatized Word :", lm.lemmatize(word))
