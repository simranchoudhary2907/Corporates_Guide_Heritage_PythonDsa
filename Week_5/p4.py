arr = []

size = int(input("Enter the size of the array: "))

for i in range(size):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

frequency = {}

for element in arr:
    if element in frequency:
        frequency[element] += 1
    else:
        frequency[element] = 1

print("\nFrequency of each element:")
for key, value in frequency.items():
    print(key, "→", value)