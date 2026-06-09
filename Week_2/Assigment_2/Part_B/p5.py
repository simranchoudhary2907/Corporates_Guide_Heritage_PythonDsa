# Part A

num = int(input("Enter a number (0 to stop): "))

count = 0
total = 0
maximum = num
minimum = num

while num != 0:
    count += 1
    total += num

    if num > maximum:
        maximum = num

    if num < minimum:
        minimum = num

    num = int(input("Enter a number (0 to stop): "))

print("Count =", count)
print("Sum =", total)
print("Maximum =", maximum)
print("Minimum =", minimum)

# Part B

n = int(input("Enter a number: "))
count = 0

for num in range(2, n +1):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")
        count += 1

print("\nTotal Prime Numbers =", count)

# part C

num = int(input("Enter a number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed Number =", reverse)