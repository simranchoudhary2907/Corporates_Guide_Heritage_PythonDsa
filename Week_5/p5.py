arr = []

size = int(input("Enter the size of the array: "))

for i in range(size):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

largest = arr[0]
second_largest = arr[0]

for i in range(1, size):
    if arr[i] > largest:
        second_largest = largest
        largest = arr[i]
    elif arr[i] > second_largest and arr[i] != largest:
        second_largest = arr[i]

print("Largest element:", largest)
print("Second Largest element:", second_largest)