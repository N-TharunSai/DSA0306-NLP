from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

text = input("Enter multiple sentences: ")

sentences = [
    s.strip()
    for s in text.split(".")
    if s.strip()
]

if len(sentences) < 2:
    print("Enter at least two sentences.")
else:

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(sentences)

    scores = []

    for i in range(len(sentences) - 1):

        score = cosine_similarity(
            vectors[i],
            vectors[i + 1]
        )[0][0]

        scores.append(score)

    average = sum(scores) / len(scores)

    print("\nCoherence Score:",
          round(average, 3))

    if average >= 0.3:
        print("Text is relatively coherent.")
    else:
        print("Text has low coherence.")
