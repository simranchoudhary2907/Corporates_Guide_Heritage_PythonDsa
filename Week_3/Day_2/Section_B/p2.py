# Recursive Solution

def factorial(n):

    # Base Case
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


print(factorial(5))

# Extension: Sum of Digits Using Recursion

def digit_sum(n):

    # Base Case
    if n < 10:
        return n

    return (n % 10) + digit_sum(n // 10)


print(digit_sum(1234))