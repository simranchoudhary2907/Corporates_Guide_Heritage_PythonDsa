# a) Squares from 1 to 15
squares = [x**2 for x in range(1, 16)]

# b) Even numbers from 1 to 50
evens = [x for x in range(1, 51) if x % 2 == 0]

# c) Words with more than 4 characters
words = ['hello', 'world', 'python', 'is', 'great']
long_words = [word for word in words if len(word) > 4]

# d) Flatten nested list
matrix = [[1,2,3], [4,5,6], [7,8,9]]
flat_list = [num for row in matrix for num in row]

# e) List of tuples (number, square)
tuples_list = [(x, x**2) for x in range(1, 9)]

print("Squares:", squares)
print("Evens:", evens)
print("Long words:", long_words)
print("Flattened list:", flat_list)
print("Tuples:", tuples_list)