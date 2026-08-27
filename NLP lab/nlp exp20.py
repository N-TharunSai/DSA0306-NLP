from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "Python is a programming language",
    "Python is useful for data science",
    "Machine learning uses Python",
    "Football is a popular sport"
]

query = input("Enter search query: ")

vectorizer = TfidfVectorizer()

matrix = vectorizer.fit_transform(documents + [query])

similarity = cosine_similarity(
    matrix[-1],
    matrix[:-1]
).flatten()

ranking = similarity.argsort()[::-1]

print("\nDocument Ranking:")

for index in ranking:
    print(
        "Document", index + 1,
        "Score:", round(similarity[index], 3)
    )
    print(documents[index])
