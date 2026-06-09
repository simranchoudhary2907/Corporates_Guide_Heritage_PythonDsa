history = []

while True:
    print("\n1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Power")
    print("6.Quit")

    choice = input("Enter Choice: ")

    if choice == "6":
        break

    if choice not in ["1", "2", "3", "4", "5"]:
        print("Invalid Choice")
        continue

    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))

    if choice == "1":
        result = num1 + num2
        operation = f"{num1} + {num2} = {result}"

    elif choice == "2":
        result = num1 - num2
        operation = f"{num1} - {num2} = {result}"

    elif choice == "3":
        result = num1 * num2
        operation = f"{num1} * {num2} = {result}"

    elif choice == "4":
        if num2 == 0:
            print("Cannot divide by zero")
            continue

        result = num1 / num2
        operation = f"{num1} / {num2} = {result}"

    elif choice == "5":
        result = num1 ** num2
        operation = f"{num1} ^ {num2} = {result}"

    print(operation)
    history.append(operation)

print("\nHistory:")
for item in history:
    print(item)