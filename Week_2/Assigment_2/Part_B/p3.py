# Part - A

i = 1
fact = 1
n = int(input("Enter a number: "))
while i <= n:
    fact *= i
    i += 1
print("The factorial of", n, "is", fact)

# Part - B

n = int(input("Enter a number: "))
a = 0
b = 1
i = 2

while i <= n+2:
    print(a, end=" ")
    c = a + b
    a = b
    b = c

    i += 1
    # print(b, end=" ")

