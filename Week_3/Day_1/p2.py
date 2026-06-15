text = "python is easy and python is powerful"

freq = {}

for word in text.split():
    freq[word] = freq.get(word, 0) + 1

print(freq)