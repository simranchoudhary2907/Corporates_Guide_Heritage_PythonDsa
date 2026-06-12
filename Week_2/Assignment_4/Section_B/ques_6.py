import string

# a) Define two paragraphs

paragraph1 = """
Python is a powerful programming language.
It is easy to learn and widely used.
Python supports object oriented programming.
Many developers enjoy using Python.
"""

paragraph2 = """
Programming is an important skill in technology.
Python and Java are popular programming languages.
Many companies use Python for data analysis.
Learning programming improves problem solving ability.
"""

# b) Function to tokenize text into unique lowercase words

def tokenize(text):
    text = text.lower()

    # Remove punctuation
    for ch in string.punctuation:
        text = text.replace(ch, "")

    return set(text.split())


words1 = tokenize(paragraph1)
words2 = tokenize(paragraph2)

print("Unique Words in Paragraph 1:")
print(words1)

print("\nUnique Words in Paragraph 2:")
print(words2)

# c) Set operations

print("\nWords in BOTH paragraphs:")
print(words1 & words2)

print("\nWords ONLY in Paragraph 1:")
print(words1 - words2)

print("\nWords ONLY in Paragraph 2:")
print(words2 - words1)

print("\nAll unique words (Union):")
print(words1 | words2)

print("\nWords in one but not the other (Symmetric Difference):")
print(words1 ^ words2)


# d) Function to find common letters

def common_letters(word1, word2):
    return set(word1.lower()) & set(word2.lower())

print("\nCommon letters between 'python' and 'programming':")
print(common_letters("python", "programming"))


# e) Find 5 most common words across both paragraphs

def word_frequency(text1, text2):
    combined = (text1 + " " + text2).lower()

    for ch in string.punctuation:
        combined = combined.replace(ch, "")

    words = combined.split()

    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    return freq


freq = word_frequency(paragraph1, paragraph2)

# Sort by frequency (descending)
top5 = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:5]

print("\nTop 5 Most Common Words:")
for word, count in top5:
    print(word, ":", count)