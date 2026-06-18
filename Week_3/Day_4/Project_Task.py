from collections import deque

# -----------------------------
# Part 1: Balanced Parentheses
# -----------------------------
def is_balanced(expression):
    stack = []

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in expression:

        if char in "([{":
            stack.append(char)

        elif char in ")]}":

            if not stack:
                return False

            top = stack.pop()

            if top != pairs[char]:
                return False

    return len(stack) == 0


# -----------------------------
# Part 2: Queue Simulation
# -----------------------------
def queue_simulation():

    queue = deque()

    while True:

        print("\n--- Ticket Counter ---")
        print("1. Add Customer")
        print("2. Serve Customer")
        print("3. Show Queue")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":

            name = input("Customer Name: ")
            queue.append(name)

            print(f"{name} added to queue.")

        elif choice == "2":

            if queue:
                served = queue.popleft()
                print(f"{served} has been served.")
            else:
                print("Queue is empty.")

        elif choice == "3":

            if queue:
                print("Current Queue:")
                for person in queue:
                    print(person)
            else:
                print("Queue is empty.")

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice.")


# -----------------------------
# Main Program
# -----------------------------
expression = input("Enter an expression: ")

if is_balanced(expression):
    print("Balanced Parentheses")
else:
    print("Not Balanced")

queue_simulation()