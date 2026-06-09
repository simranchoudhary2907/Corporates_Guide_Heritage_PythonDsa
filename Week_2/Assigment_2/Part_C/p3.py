# 3A: Time Comparison

import time

# For Loop
start = time.time()

squares = []
for i in range(1, 1000001):
    squares.append(i * i)

end = time.time()
print("For Loop:", end - start)

# List Comprehension
start = time.time()

squares = [i * i for i in range(1, 1000001)]

end = time.time()
print("List Comprehension:", end - start)

# Generator Expression
start = time.time()

squares = (i * i for i in range(1, 1000001))
sum(squares)

end = time.time()
print("Generator:", end - start)



# 3B: First n Numbers Divisible by 3 and 7

# Using For Loop

n = 5
count = 0

for num in range(21, 1000):
    if num % 21 == 0:
        print(num)
        count += 1

    if count == n:
        break


# Using While Loop

n = 5
count = 0
num = 21

while count < n:
    print(num)
    num += 21
    count += 1

# Using List Comprehension

n = 5

numbers = [i for i in range(21, 1000) if i % 21 == 0]

print(numbers[:n])


# Challenge 3C: Matrix Multiplication

A = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

B = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

result = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(3):
    for j in range(3):
        for k in range(3):
            result[i][j] += A[i][k] * B[k][j]

for row in result:
    print(row)

# List Comprehension

result = [
    [
        sum(A[i][k] * B[k][j] for k in range(3))
        for j in range(3)
    ]
    for i in range(3)
]

for row in result:
    print(row)