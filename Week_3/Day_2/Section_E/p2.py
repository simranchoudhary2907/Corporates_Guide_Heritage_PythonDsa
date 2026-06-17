def longest_subarray(arr, K):

    left = 0
    current_sum = 0
    max_len = 0

    for right in range(len(arr)):

        current_sum += arr[right]

        while current_sum > K:

            current_sum -= arr[left]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


arr = [1,2,3,4,5]
K = 9

print(longest_subarray(arr, K))