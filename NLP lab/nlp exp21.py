import spacy

nlp = spacy.load("en_core_web_sm")

text = input("Enter sentence: ")

doc = nlp(text)

print("\nNoun Phrases and Semantic Information:")

for chunk in doc.noun_chunks:
    print("Noun Phrase:", chunk.text)
    print("Root:", chunk.root.text)
    print("Root Dependency:", chunk.root.dep_)
    print("Root POS:", chunk.root.pos_)
    print()
