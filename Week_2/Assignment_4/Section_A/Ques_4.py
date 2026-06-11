import string

# a) Paragraph
text = """
Python is a high-level programming language. Python is easy to learn and easy to use.
Python is used for web development, data science, and automation.
Python helps developers build applications quickly and efficiently.
Many students learn Python because Python is simple and powerful.
"""

# b) Convert to lowercase and remove punctuation
text = text.lower()

for p in string.punctuation:
    text = text.replace(p, "")

# Split into words
words = text.split()

# c) Count word frequency using get()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("Word Frequency:")
print(frequency)

# d) Top 5 most frequent words
sorted_words = sorted(
    frequency.items(),
    key=lambda x: x[1],
    reverse=True
)

print("\nTop 5 Frequent Words:")
for word, count in sorted_words[:5]:
    print(word, ":", count)

# e) Words appearing exactly once
print("\nWords Appearing Once:")
for word, count in frequency.items():
    if count == 1:
        print(word)

# f) Dictionary comprehension for words appearing 2+ times
filtered_dict = {
    word: count
    for word, count in frequency.items()
    if count >= 2
}

print("\nWords Appearing 2+ Times:")
print(filtered_dict)