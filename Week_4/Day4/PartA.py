def freq_counter(arr):
    freq = {}

    # Count frequency of each element
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    return freq


# Test
arr = [1, 2, 3, 2, 1, 1, 4]

frequency = freq_counter(arr)

print("Frequency Dictionary:", frequency)

# Find most frequent element
max_freq = max(frequency.values())

for key, value in frequency.items():
    if value == max_freq:
        print("Most Frequent Element:", key)

# Find elements appearing exactly once
print("Elements appearing exactly once:")

for key, value in frequency.items():
    if value == 1:
        print(key)