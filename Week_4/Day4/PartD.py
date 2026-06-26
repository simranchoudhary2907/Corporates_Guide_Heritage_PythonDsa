# 1. Longest Substring Without Repeating Characters
def length_of_longest_substring(s):
    seen = set()

    left = 0
    longest = 0

    for right in range(len(s)):

        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])

        longest = max(longest, right - left + 1)

    return longest


print(length_of_longest_substring("abcabcbb"))
print(length_of_longest_substring("bbbbb"))
print(length_of_longest_substring("pwwkew"))


# 2. First Non-Repeating Character
def first_non_repeating(s):

    freq = {}

    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    for ch in s:
        if freq[ch] == 1:
            return ch

    return ""


print(first_non_repeating("leetcode"))
print(first_non_repeating("aabb"))

# 3. Group Anagrams Together

def group_anagrams(words):

    groups = {}

    for word in words:
        key = "".join(sorted(word))

        if key not in groups:
            groups[key] = []

        groups[key].append(word)

    return list(groups.values())


words = ["eat","tea","tan","ate","nat","bat"]

print(group_anagrams(words))

# 4. Implement Your Own HashTable (Chaining)

class HashTable:

    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)

        bucket = self.table[index]

        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return

        bucket.append([key, value])

    def get(self, key):
        index = self.hash_function(key)

        bucket = self.table[index]

        for pair in bucket:
            if pair[0] == key:
                return pair[1]

        return None

    def delete(self, key):
        index = self.hash_function(key)

        bucket = self.table[index]

        for i, pair in enumerate(bucket):
            if pair[0] == key:
                del bucket[i]
                return True

        return False


# Test
ht = HashTable()

ht.insert("apple", 100)
ht.insert("banana", 200)
ht.insert("grapes", 300)

print(ht.get("apple"))
print(ht.get("banana"))

ht.delete("banana")

print(ht.get("banana"))