def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # Print array after each complete pass
        print(f"Pass {i + 1}: {arr}")

        # If no swapping happened, array is already sorted
        if not swapped:
            break

    return arr


arr = [29, 10, 14, 37, 13]
print("Final Sorted Array:", bubble_sort(arr))