def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    # Divide
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    print(f"Merging {left} + {right}")

    # Conquer (merge step)
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Input array
arr = [8, 3, 5, 4, 2, 7, 1, 6]

# Function call
print("Sorted Array:", merge_sort(arr))