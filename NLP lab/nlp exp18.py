import re

def tokenize(expression):
    pattern = r'∀|∃|¬|∧|∨|→|\(|\)|,|[A-Za-z][A-Za-z0-9_]*'
    return re.findall(pattern, expression)


def validate(tokens):
    if "(" in tokens and ")" in tokens:
        return True
    return False


expression = input("Enter FOPC expression: ")

tokens = tokenize(expression)

print("\nTokens:")
print(tokens)

if validate(tokens):
    print("Expression is syntactically valid.")
else:
    print("Expression is invalid.")
