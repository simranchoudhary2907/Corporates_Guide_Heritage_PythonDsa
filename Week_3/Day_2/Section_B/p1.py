def binary_search_recursive(arr, target, low, high):

    # Base Case
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid

    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)

    else:
        return binary_search_recursive(arr, target, low, mid - 1)


arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23

print(binary_search_recursive(arr, target, 0, len(arr)-1))