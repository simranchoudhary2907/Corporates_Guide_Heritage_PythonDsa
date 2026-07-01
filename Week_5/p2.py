arr = []
size = int(input("Enter the size of the array: "))
for i in range(size):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

    smallest = arr[0]
    largest = arr[0]

for i in range(size):
    if arr[i] < smallest:
        smallest = arr[i]
    elif arr[i] > largest:
        largest = arr[i]
    
print(f"Smallest element so far: {smallest}")
print(f"Largest element so far: {largest}")
    
