"""
CP1404 - Practical 5
Word Occurrences
Estimate: 18 minutes
Actual:   10 minutes
"""

string = input("Text: ")
word_to_count = {}

for word in string.split():
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1
        pass

max_key_length = max(len(key) for key in word_to_count)

for key in sorted(word_to_count):
    print(f"{key:{max_key_length}} : {word_to_count[key]}")

