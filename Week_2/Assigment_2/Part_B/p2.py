n = int(input("Enter a number: "))

for num in range(1, n+1):
    output = ""

    if num % 3 == 0:
        output += "Fizz"

    if num % 5 == 0:
        output += "Buzz"

    if num % 7 == 0:
        output += "Bang"

    print(output or num)