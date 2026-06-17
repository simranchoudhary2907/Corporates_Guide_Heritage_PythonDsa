def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print("Step:", arr)

    return arr


arr = [64, 25, 12, 22, 11, 90, 3]
print("Selection Sort:", selection_sort(arr))

# Minimum swaps in Selection Sort?

# Minimum swaps = 0

# Why?
# If array is already sorted
# Selection Sort only swaps when needed
# So best case = no swaps at all

# In general:

# Max swaps = n−1
# Min swaps = 0