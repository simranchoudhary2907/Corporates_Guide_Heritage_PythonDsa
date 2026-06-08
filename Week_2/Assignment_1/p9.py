correct_pin = 1234
balance = 5000

pin = int(input("Enter PIN: "))

if pin == correct_pin:

    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")

    choice = int(input("Enter choice: "))

    match choice:

        case 1:
            print("Balance =", balance)

        case 2:
            amount = float(input("Enter amount: "))

            if amount <= balance:
                balance -= amount
                print("Withdrawal Successful")
                print("New Balance =", balance)
            else:
                print("Insufficient Funds")

        case 3:
            amount = float(input("Enter amount: "))
            balance += amount
            print("Deposit Successful")
            print("New Balance =", balance)

        case _:
            print("Invalid Option")

else:
    print("Incorrect PIN")