def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)


# Test Cases
print(is_anagram("listen", "silent"))
print(is_anagram("triangle", "integral"))
print(is_anagram("apple", "pale"))
print(is_anagram("rat", "tar"))

# Bonus Version (Ignore spaces and uppercase)

def is_anagram(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    return sorted(s1) == sorted(s2)


# Test
print(is_anagram("Listen", "Silent"))
print(is_anagram("Dormitory", "Dirty Room"))
print(is_anagram("Conversation", "Voices Rant On"))