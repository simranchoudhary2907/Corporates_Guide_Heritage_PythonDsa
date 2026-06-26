def two_sum(nums, target):
    hashmap = {}

    for i, num in enumerate(nums):

        # Complement is the number needed so that:
        # current number + complement = target
        complement = target - num

        # If complement already exists, answer found
        if complement in hashmap:
            return [hashmap[complement], i]

        # Store current number with its index
        hashmap[num] = i


# Test Cases
print(two_sum([2,7,11,15], 9))
print(two_sum([3,2,4], 6))
print(two_sum([3,3], 6))