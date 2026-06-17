def insertion_sort(arr):
    comparisons = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # count comparisons in while loop
        while j >= 0:
            comparisons += 1   # each comparison counted

            if arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break

        arr[j + 1] = key

    return arr, comparisons


# Part A: Already sorted
arr1 = [3, 5, 7, 9, 11]
sorted_arr1, comp1 = insertion_sort(arr1)
print("Part A Sorted:", sorted_arr1)
print("Part A Comparisons:", comp1)

print("----------------------")

# Part B: Reverse sorted
arr2 = [11, 9, 7, 5, 3]
sorted_arr2, comp2 = insertion_sort(arr2)
print("Part B Sorted:", sorted_arr2)
print("Part B Comparisons:", comp2)