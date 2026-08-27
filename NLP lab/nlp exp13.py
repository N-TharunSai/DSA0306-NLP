import nltk

grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the' | 'a'
N -> 'cat' | 'dog'
V -> 'sees' | 'likes'
""")

sentence = input("Enter sentence: ").lower().split()

parser = nltk.ChartParser(grammar)

for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
