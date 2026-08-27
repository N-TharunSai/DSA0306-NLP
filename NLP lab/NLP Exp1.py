import re

text = input("Enter a sentence: ")
pattern = input("Enter the word to search: ")

match = re.search(pattern, text)

if match:
    print("Pattern Found!")
    print("Matched Word :", match.group())
    print("Starting Position :", match.start())
    print("Ending Position :", match.end())
else:
    print("Pattern Not Found!")
