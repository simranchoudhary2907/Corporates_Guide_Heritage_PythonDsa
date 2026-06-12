# a) Create sets A and B
A = {2, 4, 6, 8, 10, 12}
B = {3, 6, 9, 12, 15}

print("Set A:", A)
print("Set B:", B)

# b) Set operations
print("\nUnion:", A | B)
print("Intersection:", A & B)
print("Difference (A-B):", A - B)
print("Difference (B-A):", B - A)
print("Symmetric Difference:", A ^ B)

# c) Subset, Superset, Disjoint checks
print("\nIs A a subset of B?", A.issubset(B))
print("Is B a superset of A?", B.issuperset(A))
print("Are A and B disjoint?", A.isdisjoint(B))

# d) Add and Remove elements
A.add(14)
B.discard(3)  # Safe removal

print("\nAfter modifications:")
print("Set A:", A)
print("Set B:", B)

# e) Remove duplicates from list using set
nums = [5, 1, 3, 5, 2, 1, 4, 3, 5, 2, 6]

unique_nums = set(nums)

print("\nOriginal List:", nums)
print("Unique Elements:", unique_nums)

# f) Create a frozenset
frozen_A = frozenset(A)

print("\nFrozen Set:", frozen_A)

# Demonstrate immutability
try:
    frozen_A.add(16)
except AttributeError as e:
    print("Cannot modify frozenset:", e)