scores = [55, 72, 88, 43, 91, 67, 55, 76]

# a) Append 80
scores.append(80)
print("After append:", scores)

# b) Insert 100 at index 3
scores.insert(3, 100)
print("After insert:", scores)

# c) Remove first occurrence of 55
scores.remove(55)
print("After remove:", scores)

# d) Sort in ascending order
scores.sort()
print("Ascending order:", scores)

# e) Sort in descending order
scores.sort(reverse=True)
print("Descending order:", scores)

# f) Count occurrences of 55 in original list
original_scores = [55, 72, 88, 43, 91, 67, 55, 76]
print("Count of 55:", original_scores.count(55))

# g) Find index of 88
print("Index of 88:", original_scores.index(88))

# h) Pop last element
popped_value = scores.pop()
print("Popped value:", popped_value)
print("Remaining list:", scores)