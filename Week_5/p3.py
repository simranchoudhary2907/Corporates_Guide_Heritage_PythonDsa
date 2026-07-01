arr = []

size = int(input("Enter the size of the array: "))

for i in range(size):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

    result = []
    seen = set()

    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)

print(f"Array with duplicates removed: {result}")
    