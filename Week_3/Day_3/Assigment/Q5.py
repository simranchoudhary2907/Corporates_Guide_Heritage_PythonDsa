# Part A – one pass + full sort


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        print(f"Pivot placed at index {pi}: {arr}")

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def partition(arr, low, high):
    pivot = arr[high]   # last element as pivot
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# Input (Q5 array)
arr = [15, 3, 9, 8, 5, 2, 7, 1, 6]

quick_sort(arr, 0, len(arr) - 1)

print("Final Sorted Array:", arr)


#Part B: Worst Case Demonstration Code

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# Worst case input (sorted array)
arr = [1, 2, 3, 4, 5]

quick_sort(arr, 0, len(arr) - 1)

print("Worst Case Sorted Array:", arr)