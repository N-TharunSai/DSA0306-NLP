import nltk

grammar = nltk.CFG.fromstring("""
S -> NP_SG VP_SG
S -> NP_PL VP_PL

NP_SG -> 'the' 'boy'
NP_PL -> 'the' 'boys'

VP_SG -> 'runs'
VP_PL -> 'run'
""")

sentence = input("Enter sentence: ").lower().split()

parser = nltk.ChartParser(grammar)

valid = False

for tree in parser.parse(sentence):
    valid = True
    print("Agreement is correct.")
    print(tree)

if not valid:
    print("Agreement is incorrect.")
