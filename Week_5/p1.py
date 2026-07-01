#if we want to used array with predefined values

# arr = [1,2,3,4,5]

#if we want to take input from user we can use the below code
arr = []
size = int(input("Enter the size of the array: "))
for i in range(size):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

start = 0
end = len(arr) - 1
while start < end:
    temp = arr[start]
    arr[start] = arr[end]
    arr[end] = temp

    start += 1
    end -= 1

print("Reversed array:", arr)


# Time Complexity: O(n)
# Space Complexity: O(1) (in-place reversal)